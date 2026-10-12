# Exercise 3: Scaling a Flask App with Kubernetes ReplicaSets

## Overview

This exercise demonstrates how to deploy a Flask application on Kubernetes using Minikube and Docker. A Kubernetes ReplicaSet maintains the desired number of application Pods, supports scaling, and automatically replaces deleted Pods.

## Technologies Used

- Docker
- Kubernetes
- Minikube
- kubectl
- Python
- Flask
- Gunicorn

## Project Structure

```text
03-Minikube-Scaling-Flask-App-with-Replicasets/
├── app.py
├── Dockerfile
├── flashsale-replicaset.yaml
├── README.md
└── screenshots/
    ├── 01-initial-replicas.png
    ├── 02-flask-app-running.png
    ├── 03-scaled-to-five-replicas.png
    └── 04-automatic-pod-recovery.png
```

## Application Details

The Flask application provides two endpoints:

- `/` — Returns a JSON response confirming that the Flash Sale application is running, along with the container hostname.
- `/health` — Returns the application's health status.

The application listens on port `5000` and runs using Gunicorn.

## Implementation Steps

### 1. Build the Docker Image

Build the Flask application's Docker image:

```powershell
docker build -t flashsale-app:v1 .
```

Load the image into Minikube:

```powershell
minikube image load flashsale-app:v1
```

### 2. Deploy the ReplicaSet

Apply the Kubernetes configuration:

```powershell
kubectl apply -f flashsale-replicaset.yaml
```

Verify the ReplicaSet and its Pods:

```powershell
kubectl get replicaset
kubectl get pods -l app=flashsale -o wide
```

Initially, the ReplicaSet was configured to maintain three replicas.

### 3. Expose the Application

The application is exposed through a Kubernetes NodePort Service on port `30080`, forwarding traffic to container port `5000`.

Check the Service:

```powershell
kubectl get services flashsale-service
```

Access the application using:

```powershell
minikube service flashsale-service --url
```

### 4. Scale the Application

Scale the ReplicaSet from three replicas to five:

```powershell
kubectl scale replicaset flashsale-replicaset --replicas=5
```

Verify the result:

```powershell
kubectl get replicaset flashsale-replicaset
kubectl get pods -l app=flashsale -o wide
```

The ReplicaSet reached five desired, current, and ready replicas.

### 5. Demonstrate Automatic Pod Recovery

Delete one of the application Pods:

```powershell
kubectl delete pod <pod-name>
```

Replace `<pod-name>` with an actual Pod name returned by `kubectl get pods -l app=flashsale`.

Verify the replacement:

```powershell
kubectl get pods -l app=flashsale
```

The ReplicaSet automatically created a replacement Pod to maintain five replicas.

## Results

- Successfully built the Flask Docker image.
- Deployed the application on Minikube.
- Created a ReplicaSet with three initial replicas.
- Exposed the application through a Kubernetes Service.
- Scaled the ReplicaSet to five replicas.
- Verified automatic Pod replacement after deleting a Pod.
- Confirmed that the application remained accessible after recovery.

## Screenshots

The `screenshots/` directory contains evidence of the initial ReplicaSet status, the working Flask application, scaling to five replicas, and automatic Pod recovery.

## Key Learnings

- Containerizing a Flask application with Docker.
- Deploying containerized applications on Kubernetes.
- Understanding ReplicaSets and desired replica counts.
- Exposing applications using Kubernetes Services and NodePort.
- Scaling application replicas.
- Understanding Kubernetes self-healing and Pod replacement.
