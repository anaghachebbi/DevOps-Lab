# Exercise 9: Jenkins Multistage Pipeline

## Objective

To create and execute a Jenkins declarative pipeline that automates the build, testing, deployment, and application testing stages of a Python Flask application.

## Technologies Used

- Jenkins
- Docker
- Python
- Flask
- Git and GitHub

## Project Structure

```text
09-Jenkins-Multistage-Pipeline/
├── Jenkinsfile
├── README.md
├── python-flask-app/
│   ├── app.py
│   ├── requirements.txt
│   └── test_app.py
└── screenshots/
    ├── 01-python-dependencies.png
    ├── 02-jenkins-dashboard.png
    └── 03-jenkins-pipeline-success.png
```

## Pipeline Stages

1. **Build:** Creates an isolated Python virtual environment and installs the application dependencies.
2. **Test:** Runs the application's unit tests.
3. **Deploy:** Copies the Flask application into a deployment directory.
4. **Run Application:** Starts the Flask application.
5. **Test Application:** Runs the unit tests again to verify the application.

## Execution

1. Start the Jenkins container.
2. Open Jenkins in the browser.
3. Configure the `Python-MultiStage-Pipeline` job to use this repository's `Jenkinsfile`.
4. Run the job using **Build Now**.
5. Check the Console Output to verify the pipeline result.

## Result

The Jenkins multistage pipeline executed successfully, completing all configured stages.

## Screenshots

The `screenshots/` directory contains evidence of dependency installation, the Jenkins dashboard, and the successful pipeline execution.
