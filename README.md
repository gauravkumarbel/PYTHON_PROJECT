🖥️ Server Health Monitor

A lightweight Python-based Server Health Monitoring Tool that checks important system resources such as CPU, RAM, disk usage, network activity, running processes, and system uptime.

This project is designed as a beginner-friendly DevOps project for learning Python, Linux, Git, GitHub, CI/CD, Docker, and Kubernetes.

🚀 Features

✅ CPU usage monitoring

✅ RAM usage monitoring

✅ Disk usage monitoring

✅ Network traffic monitoring

✅ Running process count

✅ System uptime monitoring

✅ Health status reporting

✅ Simple Python implementation

✅ Suitable for Linux servers

🔄 Can be extended with Docker, Jenkins, and Kubernetes

🛠️ Technologies Used

Python 3

psutil

Linux

Git

GitHub

Planned DevOps integrations:

GitHub Actions

Docker

Jenkins

Kubernetes

📁 Project Structure
server-health-monitor/
│
├── server_monitor.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .github/
    └── workflows/
        └── ci.yml

⚙️ Installation
1. Clone the repository
git clone https://github.com/gauravkumarbel/PYTHON_PROJECT.git

2. Enter the project directory
cd server-health-monitor

3. Install dependencies
pip3 install -r requirements.txt


Or:

pip3 install psutil

▶️ Run the Application

Run the Python script:

python3 server_monitor.py


Example output:

================================
       SERVER HEALTH MONITOR
================================

CPU Usage       : 25%
RAM Usage       : 58%
Disk Usage      : 47%
Network Sent    : 125 MB
Network Received: 430 MB
Processes       : 182
Uptime          : 14.5 hours

Status          : HEALTHY
================================

📦 requirements.txt
psutil

🔍 Health Status

The application can classify the server based on resource usage.

Resource	Normal	Warning	Critical
CPU	< 70%	70–90%	> 90%
RAM	< 70%	70–90%	> 90%
Disk	< 70%	70–90%	> 90%

These thresholds can be customized according to your environment.

🐧 Linux Commands

The project can be used alongside standard Linux monitoring commands:

top
free -h
df -h
uptime


Python provides a programmatic way to collect similar system information using psutil.

🔄 DevOps Roadmap

This project can be extended into a complete DevOps pipeline:

Developer
    ↓
Git Push
    ↓
GitHub
    ↓
GitHub Actions
    ↓
Run Tests
    ↓
Build Docker Image
    ↓
Docker Registry
    ↓
Jenkins / CI/CD
    ↓
Kubernetes
    ↓
Application Deployment

Planned Improvements

 Add automated tests with pytest

 Add GitHub Actions CI

 Add Dockerfile

 Build Docker image

 Add Jenkins pipeline

 Deploy to Kubernetes

 Add Prometheus metrics

 Add Grafana dashboard

 Add email/Slack alerts

 Add logging

 Add configuration through environment variables

🎯 Learning Objectives

This project helps practice:

Python scripting

Linux system administration

System monitoring

Git and GitHub

CI/CD concepts

Docker containerization

Jenkins automation

Kubernetes deployment

Monitoring and observability

👨‍💻 Author

Your GAURAV KUMAR

GitHub: https://github.com/gauravkumarbel

📄 License

This project is open source and available under the MIT License.
