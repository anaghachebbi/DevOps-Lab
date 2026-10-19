# Exercise 10: Multi-Node Kubernetes Cluster with Multiple Applications and ReplicaSets

## Objective

Deploy two Flask applications on a three-node Minikube Kubernetes cluster using Docker images, Kubernetes Deployments, pod anti-affinity, and NodePort Services.

## Technologies Used

- Docker
- Kubernetes
- Minikube
- Python
- Flask
- YAML
- PowerShell

## Applications

### 1. Product Catalog

- File: `product_catalog.py`
- Docker image: `product-catalog:latest`
- Deployment: `product-catalog`
- Replicas: 2
- Endpoint: `/products`
- Returns a JSON list of products.

### 2. Shopping Cart

- File: `shopping_cart.py`
- Docker image: `shopping-cart:latest`
- Deployment: `shopping-cart`
- Replicas: 3
- Endpoint: `/cart`
- Supports retrieving cart items and adding items using a POST request.

## Kubernetes Configuration

- Created a three-node Minikube cluster.
- Built and loaded both Docker images into Minikube.
- Created Kubernetes Deployments for both applications.
- Configured pod anti-affinity to distribute replicas across different nodes.
- Exposed both applications using NodePort Services.

## Verification

The following were verified successfully:

- All three Kubernetes nodes were Ready.
- Both Docker images were built and loaded.
- All five application pods were Running and distributed across the three nodes.
- Product Catalog returned product data through `/products`.
- Shopping Cart returned an empty cart and accepted a POST request to add an item.
- Kubernetes Deployments and Services were checked.

## Screenshots

The `screenshots` directory contains execution evidence:

1. `01-multinode-cluster.png` — Multi-node cluster
2. `02-docker-images.png` — Docker images
3. `03-pods-distributed-across-nodes.png` — Pods distributed across nodes
4. `04-deployments-and-services.png` — Deployments and Services
5. `05-product-catalog-test.png` — Product Catalog API test
6. `06-shopping-cart-test.png` — Shopping Cart API test

## Cleanup

When finished, stop the Minikube cluster with:

```powershell
minikube -p devops-multinode stop
```

To start it again:

```powershell
minikube -p devops-multinode start
```
