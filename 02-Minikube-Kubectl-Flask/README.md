# Exercise 2: Minikube, kubectl & Flask

## Overview

This exercise demonstrates how to containerize a Python Flask application using Docker and deploy it on a local Kubernetes cluster using Minikube and kubectl.

The application runs inside a Kubernetes Pod and is exposed externally using a NodePort Service.

## Technologies Used

- **Python** — application development
- **Flask** — lightweight web framework
- **Docker** — containerization
- **Kubernetes** — container orchestration
- **Minikube** — local Kubernetes cluster
- **kubectl** — Kubernetes command-line tool

## Project Structure

```text
02-Minikube-Kubectl-Flask/
├── app.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── flask-app-running.png
└── README.md
```

## Application Details

The Flask application exposes a root endpoint (`/`) on port `15000` and returns the following response:

```text
Hello from Flask on Kubernetes!
```

## Prerequisites

Ensure the following are installed and configured:

- Docker Desktop
- Minikube
- kubectl
- Visual Studio Code (optional)

## Steps to Run the Application

### 1. Start Docker Desktop

Open Docker Desktop and wait for the Docker engine to start.

### 2. Start Minikube

```bash
minikube start --driver=docker
```

Verify the Kubernetes node:

```bash
kubectl get nodes
```

### 3. Build the Docker Image

Navigate to this exercise directory and build the image:

```bash
docker build -t flask-k8s:latest .
```

### 4. Load the Image into Minikube

```bash
minikube image load flask-k8s:latest
```

### 5. Deploy the Application

Apply the Kubernetes Deployment configuration:

```bash
kubectl apply -f deployment.yaml
```

### 6. Expose the Application

Create the Kubernetes Service:

```bash
kubectl apply -f service.yaml
```

### 7. Verify the Deployment

Check the Deployment:

```bash
kubectl get deployments
```

Check the Pods:

```bash
kubectl get pods
```

Check the Service:

```bash
kubectl get services
```

Check application logs:

```bash
kubectl logs deployment/flask-deployment
```

### 8. Access the Application

Run:

```bash
minikube service flask-service
```

This opens the Flask application in a browser through the Minikube service tunnel.

Expected response:

```text
Hello from Flask on Kubernetes!
```

## Kubernetes Configuration

- **Deployment:** `flask-deployment`
- **Replicas:** 1
- **Container image:** `flask-k8s:latest`
- **Container port:** `15000`
- **Service:** `flask-service`
- **Service type:** NodePort
- **NodePort:** `30000`

The Deployment manages the application Pod, while the Service provides network access to the application.

## Screenshot

The file `flask-app-running.png` contains a screenshot of the successfully running Flask application.

## Cleanup

After completing the exercise, stop Minikube:

```bash
minikube stop
```

This stops the local Kubernetes cluster without deleting the exercise files or GitHub repository.

## Result

Successfully built a Docker image for a Flask application, deployed it on a local Kubernetes cluster using Minikube and kubectl, exposed it through a NodePort Service, and verified the application through a web browser.
