# Real-Time Operations Monitoring and Alerting

## Overview

This project demonstrates real-time monitoring of a delivery service using **Prometheus**, **Grafana**, and **Jenkins**. A Python script generates simulated delivery metrics, Prometheus collects and evaluates them, and Grafana visualizes them in a dashboard.

The project also demonstrates alerting when pending deliveries or average delivery time exceed configured thresholds.

## Technologies Used

- Python
- Prometheus
- Grafana
- Jenkins
- Docker and Docker Desktop
- Git and GitHub

## Project Structure

```text
06-Real-Time-Operations-Monitoring-and-Alerting/
├── delivery_metrics.py
├── prometheus.yml
├── alert_rules.yml
├── screenshots/
└── README.md
```

## Components

### 1. Python Metrics Generator

`delivery_metrics.py` simulates delivery activity and exposes metrics on port `8000`.

The metrics include:

- `total_deliveries`
- `pending_deliveries`
- `on_the_way_deliveries`
- `average_delivery_time`

The script generates new values every second.

### 2. Prometheus

`prometheus.yml` configures Prometheus to scrape the delivery service metrics.

Prometheus is available at `http://localhost:9090`.

The `alert_rules.yml` file defines alerts for high pending deliveries and high average delivery time.

### 3. Grafana

Grafana connects to Prometheus as its data source and displays a **Delivery Monitoring Dashboard** containing four Stat panels:

- Total Deliveries
- Pending Deliveries
- On-the-Way Deliveries
- Average Delivery Time

Grafana is available at `http://localhost:3000`.

### 4. Jenkins

A Jenkins pipeline named `Delivery-Monitoring-Pipeline` was created to verify Docker CLI availability, Docker daemon connectivity, and the Jenkins workspace.

The pipeline completed successfully. It currently verifies Docker connectivity and workspace contents; it does not automatically build or deploy the monitoring application.

## Alert Simulation

To simulate high pending deliveries, the pending-delivery range in `delivery_metrics.py` was changed from:

```python
pending = random.randint(10, 20)
```

to:

```python
pending = random.randint(50, 100)
```

After restarting the metrics script and starting Prometheus, the `HighPendingDeliveries` and `HighAverageDeliveryTime` alerts were observed in the **Firing** state.

## Running the Project

1. Start Docker Desktop.
2. Start the Prometheus and Grafana containers if they are stopped:

   ```powershell
   docker start prometheus
   docker start grafana
   ```

3. From this project directory, run the Python metrics generator:

   ```powershell
   python .\delivery_metrics.py
   ```

4. Open Prometheus at `http://localhost:9090`.
5. Open Grafana at `http://localhost:3000` and view the Delivery Monitoring Dashboard.

Keep the Python script running while monitoring the metrics. Prometheus must be configured to reach the metrics endpoint at `host.docker.internal:8000/metrics`.

## Screenshots

The `screenshots/` directory contains evidence of the metrics generator, Prometheus queries and targets, Grafana configuration and dashboard, Jenkins pipeline, and alert simulation.

## Learning Outcomes

- Exposing application metrics from Python.
- Configuring Prometheus scraping and alert rules.
- Querying and visualizing metrics with Grafana.
- Simulating alert conditions and verifying firing alerts.
- Connecting Jenkins to Docker Desktop for pipeline verification.
