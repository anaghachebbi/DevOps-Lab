# Exercise 4: Docker Networking

## Objective

Create a custom Docker bridge network and run Flask, MySQL, and Redis containers on the same network to verify container connectivity.

## Technologies Used

- Docker Desktop
- Docker Bridge Networking
- Python and Flask
- MySQL 8.0
- Redis

## Implementation

1. Created a custom bridge network named `my-bridge-net`.
2. Built a Docker image for the Flask application.
3. Started the Flask, MySQL, and Redis containers on the custom network.
4. Verified container name resolution and service connectivity.
5. Tested the Flask application and health endpoint.

## Verification Results

- Flask application: Passed
- Flask health endpoint: Passed
- MySQL hostname resolution: Passed
- Redis hostname resolution: Passed
- Redis ping: `PONG`
- MySQL server readiness: `mysqld is alive`
- Container network attachment: Verified

## Screenshots

See the `screenshots/` directory for evidence of Docker network configuration and successful container connectivity.

## Files

- `app.py` — Flask application
- `requirements.txt` — Python dependencies
- `Dockerfile` — Flask image configuration
- `screenshots/` — Lab execution evidence
