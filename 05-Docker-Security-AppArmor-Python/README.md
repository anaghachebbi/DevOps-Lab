# Docker Security with AppArmor and Python

## Objective

Secure a containerized Flask application using Docker and AppArmor, and use the Docker SDK for Python to configure and inspect container security options.

## Technologies Used

- Python 3.8
- Flask
- Docker and Docker SDK for Python
- AppArmor
- Ubuntu on WSL2
- Git and GitHub

## Project Structure

```text
05-Docker-Security-AppArmor-Python/
├── app.py
├── Dockerfile
├── requirements.txt
├── my-apparmor-profile
├── apply_apparmor.py
├── test_restricted_actions.py
├── screenshots/
└── README.md
```

## Flask Application

The Flask application runs on port 5000 and returns a welcome message at `/`.

## Build the Docker Image

```powershell
docker build -t flask-apparmor .
```

## Run the Application

```powershell
docker run -d --name flask-apparmor-test -p 5000:5000 flask-apparmor
```

Open http://localhost:5000 to verify the application.

Stop and remove the test container:

```powershell
docker rm -f flask-apparmor-test
```

## Docker SDK for Python

Install the dependency:

```powershell
python -m pip install docker
```

Run the profile configuration script:

```powershell
python apply_apparmor.py
```

Run the restricted-action tests:

```powershell
python test_restricted_actions.py
```

## AppArmor Profile

The `my-apparmor-profile` file contains rules intended to restrict access to sensitive directories, limit binary execution, and control capabilities.

## Environment Limitation and Test Results

This exercise was developed on Windows using Docker Desktop with WSL2 and Ubuntu 22.04.

Docker accepted the configured `apparmor=my-apparmor-profile` security option, but the environment did not expose AppArmor as an active security module to Docker. The restricted-action tests consequently succeeded in reading `/etc/passwd` and executing `/bin/bash`.

**AppArmor enforcement has not been verified in this environment.** These results must not be interpreted as proof that the profile successfully blocks restricted actions. Actual enforcement requires a compatible Linux environment with AppArmor active and the profile loaded.

## Screenshots

The `screenshots/` directory contains evidence collected during the exercise. Add the Docker build, Flask response, profile configuration, and test outputs as available.

## Learning Outcome

This exercise covers Flask containerization, Docker SDK usage, container security configuration, and testing restricted operations. Successful AppArmor enforcement remains to be verified in a compatible Linux environment.
