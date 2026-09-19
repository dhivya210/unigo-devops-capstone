# UniGo – Student Life Abroad

UniGo is a Flask-based web application designed as a student companion for international students living and studying abroad.

This project was developed as a DevOps Capstone Project. The main focus is the implementation of an end-to-end DevOps workflow including source control, automated testing, CI/CD, containerization, AWS cloud infrastructure, monitoring, and automation.

## Tech Stack

### Application
- Python
- Flask
- HTML
- CSS

### DevOps Tools
- Git
- GitHub
- Jenkins
- Docker
- Docker Hub
- AWS EC2
- Prometheus
- Node Exporter
- Grafana
- Bash
- Cron

## Application Features

- UniGo home dashboard
- Student journey page
- Health-check endpoint
- Automated Flask tests

### Application Endpoints

- `/` – Home page
- `/journey` – Student journey page
- `/health` – Application health check

## Run Locally

Clone the repository:

```bash
git clone https://github.com/dhivya210/unigo-devops-capstone.git
cd unigo-devops-capstone
```

Create a virtual environment:

```bash
python -m venv venv
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open the application in a browser:

`http://localhost:5000`

## Automated Testing

Run the tests using:

```bash
pytest
```

The project contains automated tests for:

- Home page
- Journey page
- Health endpoint

## Docker

Build the Docker image:

```bash
docker build -t unigo:1.0 .
```

Run the Docker container:

```bash
docker run -d -p 5000:5000 --name unigo-container unigo:1.0
```

Docker Hub image:

`dhivyadharshini2106/unigo:latest`

## CI/CD Pipeline

Jenkins is used to automate the CI/CD workflow.

Pipeline flow:

**GitHub → Jenkins → Test → Docker Build → Docker Push → AWS Deployment → Health Check**

The Jenkins pipeline configuration is stored in the `Jenkinsfile`.

## AWS Infrastructure

AWS EC2 is used as the cloud infrastructure for the project.

The EC2 environment is used to demonstrate cloud deployment, automation, and monitoring of the UniGo DevOps environment.

## Monitoring

Monitoring is implemented using:

- Prometheus
- Node Exporter
- Grafana

Node Exporter collects server metrics.

Prometheus collects and stores the metrics.

Grafana visualizes the collected metrics through the **UniGo DevOps Monitoring Dashboard**.

The dashboard monitors:

- Server status
- CPU usage
- Memory usage
- System metrics

## Bash and Cron Automation

Bash scripts are used for backup and cleanup automation.

The following Cron jobs automate these tasks:

```cron
0 2 * * * /home/ubuntu/unigo-scripts/backup.sh
0 3 * * 0 /home/ubuntu/unigo-scripts/cleanup.sh
```

The backup script runs every day at **02:00**.

The cleanup script runs every Sunday at **03:00**.

## DevOps Architecture

```text
Developer
   ↓
GitHub
   ↓
Jenkins CI/CD
   ↓
Automated Testing
   ↓
Docker Build
   ↓
Docker Hub
   ↓
AWS EC2

AWS EC2
   ↓
Node Exporter
   ↓
Prometheus
   ↓
Grafana Dashboard

Bash + Cron
   ↓
Backup & Cleanup Automation
```

## Project Repository Structure

```text
unigo-devops-capstone/
├── static/
├── templates/
├── tests/
├── .dockerignore
├── .gitignore
├── app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── README.md
```
CI/CD pipeline automated using Jenkins.
## Author

**Dhivyadharshini Kathiravan Sathyabama**

DevOps Capstone Project – 2026