from flask import Flask, render_template, request, redirect, url_for
from flask.logging import default_handler
from flask_sqlalchemy import SQLAlchemy

import time
import structlog

app = Flask(__name__)
app.logger.removeHandler(default_handler)
app.logger.handlers.clear()
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres:admin@postgres-service:5432/grocery_db'
    )
db = SQLAlchemy(app)

structlog.configure(processors=[
    structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=True),
    structlog.processors.JSONRenderer()
    ])
log = structlog.get_logger()


class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    items = db.Column(db.String(200), nullable=False)


def create_app():
    with app.app_context():
        retries = 5
        while True:
            try:
                db.create_all()
                break
            except Exception as e:
                if retries == 0:
                    raise e
                retries -= 1
                time.sleep(1)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        items = request.form['items']
        grocery = Grocery(name=name, items=items)
        db.session.add(grocery)
        db.session.commit()
        log.info("Index page loaded")
        return redirect(url_for('success', name=name, items=items))
    return render_template('index.html')


@app.route('/success/<string:name>/<string:items>')
def success(name, items):
    log.info(
        "All items added successfully.",
        user=name,
        list=items
        )
    return render_template('success.html')


@app.route('/lists')
def lists():
    if request.method == 'POST':
        return redirect(url_for('delete_all_items'))
    try:
        groceries = Grocery.query.all()
        groceries_json = [{
            'user': grocery.name,
            'list': grocery.items
            } for grocery in groceries]
        log.info("Retrieved groceries", groceries=groceries_json)
        return render_template(
            'lists.html',
            groceries=groceries
            )
    except Exception as e:
        log.error("Error retrieving groceries: %s", str(e))
        return "An error occurred while retrieving groceries.", 500


@app.route('/delete-all-items', methods=['POST'])
def delete_all_items():
    try:
        Grocery.query.delete()
        db.session.commit()
        log.info("All items deleted successfully.")
        return redirect(url_for('lists'))

    except Exception as e:
        log.error("Error deleting items: %s", str(e))
        return "An error occurred while deleting items.", 500


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
