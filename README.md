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

