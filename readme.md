# Polls Project

# All Polls will be displayed on this project.

# Polls
a. Poll 1
b. Poll 2
c. Poll 3

# Installation
To install and set up this project locally:

Clone the repository to your local machine using the following command:
git clone https://github.com/Tshire-Sehole/Polls.git
cd Polls

# Running the Project on Docker

# Required conditions
Make sure that you have Docker and Docker Compose installed.

# 1. Build the Docker Image
docker build -t polls .

# 2. Run the Docker Container
docker run -d -p 8000:8000 polls

# 3. Access the Application
Go to http://localhost:8000 in your web browser.

# Using Docker Compose
# 1. Build and Run
docker-compose up --build
# 2. Access the Application
Go to http://localhost:8000 in your web browser.

# Environment Variables
If certain environment variables are needed by your programme, make a.env file in the root directory and include the necessary variables:
ENV_VAR_NAME=value

Ensure the Dockerfile or Docker Compose file references this .env file.

# Managing the Docker Containers

# Stop Containers:
docker-compose down

# Remove Containers and Images:
docker system prune -f

# Check Logs:
docker logs <container_id>

# Additional Commands

 # List Docker Images:
docker images

# List Docker Containers:
docker ps -a

# Access Container Shell:
docker exec -it <container_id> /bin/bash

# USAGE
Install the Live Server extension into VS Code and use Live Server to run polls.

# Authors of Software | Credits
Tshireletso Sehole https://www.linkedin.com/in/tshireletso-sehole-761350265?

