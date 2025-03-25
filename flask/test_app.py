import pytest
from app import app, db, Grocery


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


def test_post_index_creates_grocery_and_redirects(client):
    response = client.post("/", data={
        "name": "TestUser",
        "items": "Apples, Milk"
    }, follow_redirects=False)

    assert response.status_code == 302
    expected_url = "/success/TestUser/Apples,%20Milk"
    assert expected_url in response.headers["Location"]

    grocery = Grocery.query.first()
    assert grocery is not None
    assert grocery.name == "TestUser"
    assert grocery.items == "Apples, Milk"
