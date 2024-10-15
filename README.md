# Grocery-app

This distribution contains all the components from both the [OpenTelemetry Collector](https://github.com/open-telemetry/opentelemetry-collector) repository and the [OpenTelemetry Collector Contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib) repository. This distribution includes open source and vendor supported components.

## Project Overview
The Grocery-app is a Flask web application deployed on Kubernetes using Minikube. It utilizes a custom Docker image for deployment and integrates comprehensive monitoring through Datadog. This setup allows for infrastructure monitoring, Application Performance Monitoring (APM), database monitoring, and the collection of application logs, providing a robust solution for real-time application insights.

<img width="250" height="250" alt="Add Item" src="https://github.com/user-attachments/assets/7e5854af-7fea-4c51-b4fc-b0fe4fe959e3"><img width="250" height="250" alt="Confirmation Message" src="https://github.com/user-attachments/assets/dbd257f1-f29c-4967-a783-53ee4d0bfe9e"><img width="250" height="250" alt="View List" src="https://github.com/user-attachments/assets/0890d539-9753-42bc-8d65-eae6ec42dfee">



## Prerequisites
Before setting up the Grocery-app, ensure that the following tools are installed and configured on your machine:
- Docker
- Kubernetes
- Minikube
- Helm (for Datadog Operator installation)

