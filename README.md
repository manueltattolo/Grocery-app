# Grocery-app

This distribution contains all the components from both the [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector) repository and the [OpenTelemetry Collector Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib) repository. This distribution includes open source and vendor supported components.

## Project Overview
The Grocery-app is a Flask web application deployed on Kubernetes using Minikube. It utilizes a custom Docker image for deployment and integrates comprehensive monitoring through Datadog. This setup allows for infrastructure monitoring, Application Performance Monitoring (APM), database monitoring, and the collection of application logs, providing a robust solution for real-time application insights.

App visual:

<img height="250" alt="Add Item" src="https://github.com/user-attachments/assets/7e5854af-7fea-4c51-b4fc-b0fe4fe959e3"><img height="250" alt="Confirmation Message" src="https://github.com/user-attachments/assets/dbd257f1-f29c-4967-a783-53ee4d0bfe9e"><img height="250" alt="View List" src="https://github.com/user-attachments/assets/0890d539-9753-42bc-8d65-eae6ec42dfee">

Datadog monitoring including Infra, APM, Application and Infra Logs, Database Monitoring:

<img width="1507" alt="Screenshot 2024-10-15 at 12 32 35" src="https://github.com/user-attachments/assets/76cac6d9-4a5e-4a58-9d65-8f440f277a1b">
<img width="1511" alt="Screenshot 2024-10-15 at 12 34 28" src="https://github.com/user-attachments/assets/76468d89-de51-4e99-b623-855c95937a2b">
<img width="1507" alt="Screenshot 2024-10-15 at 12 35 20" src="https://github.com/user-attachments/assets/ea1fa925-7641-43de-8ad0-58444470117f">
<img width="1506" alt="Screenshot 2024-10-15 at 13 26 09" src="https://github.com/user-attachments/assets/345a591d-b879-4f42-bd34-b019e7ffefd3">

## Prerequisites
Before setting up the Grocery-app, ensure that the following tools are installed and configured on your machine:
- Docker and access to your Docker repository for pushing the image
- Kubernetes
- Minikube
- Helm (for Datadog Operator installation)

## Installation Steps
1. **Start Minikube:**
   ```bash
   minikube start
   
2. **Build the Docker image**
Navigate to the Flask app directory. Build the Docker image with tag:
```bash
docker build -t yourdockerhubusername/flask-app:latest .
```

3. **Push the Docker image to Docker Hub**
After tagging the image, push it to your Docker Hub repository:

```bash
docker push yourdockerhubusername/flask-app:latest
```

4. **Deploy the application**
Apply the Kubernetes configurations. Make sure your deployment YAML files refer to the correct image:

```bash
kubectl apply -f flask-deployment.yaml
kubectl apply -f postgresql-deployment.yaml
```

5. **Install the Datadog Agent**
First, add the Datadog Helm repository and install the Datadog Operator:

```bash
helm repo add datadog https://helm.datadoghq.com
helm install datadog-operator datadog/datadog-operator
kubectl create secret generic datadog-secret --from-literal api-key=<DATADOG_API_KEY>
```
Then, apply the Datadog agent configuration:

```bash
kubectl apply -f datadog-agent.yaml
```
6. **Access the application service in minikube**
```bash
minikube service flask-nodeport-service --url
```

**Configuration**
Ensure that the Flask application and PostgreSQL service are configured correctly with the right environment variables and settings as specified in the deployment files. Configure the Datadog agent by modifying datadog-agent.yaml if necessary, to match your monitoring and logging requirements.

**Usage**
Access the web application via the NodePort exposed by Minikube or through any configured ingress. Use the application to manage grocery lists, with functionalities to add, delete, and view items.

**Monitoring**
With Datadog integrated, you can monitor:

- Infrastructure metrics
- Application performance
- Database operations
- Real-time logs
