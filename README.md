# Flask-app-docker
This repository contains a simple Flask application that runs on Docker.

## Prerequisites
- Docker installed on your machine. 

## Usage
1. Clone this repository to your local machine:
     git clone https://github.com/RSauravR/simple-flask-docker.git
   
2. Navigate to the project directory:
     cd simple-flask-docker

3. Build the Docker image:
     docker build -t flask-app:latest .
      ![image](https://github.com/RSauravR/Flask-app-docker/assets/121216190/aa4309a2-a034-4081-b064-66b2eac40dd7)
      ![image](https://github.com/RSauravR/Flask-app-docker/assets/121216190/c9fa08e2-e191-4541-a29c-7110e2dea375)


5. Run the Docker container:
     docker run -p 80:80 flask-app:latest
     ![image](https://github.com/RSauravR/Flask-app-docker/assets/121216190/15654771-7a62-490c-a61c-f5b334739d4f)


7. Access the Flask application:
   Open your web browser and go to http://localhost:80
                        or
   In aws open your instances ip http://ip_address:80
   ![image](https://github.com/RSauravR/Flask-app-docker/assets/121216190/148152b0-ba57-4ffa-9bf3-2d6fd05343d5)
   ![image](https://github.com/RSauravR/Flask-app-docker/assets/121216190/46c63b52-595e-49b6-b1a5-7c957a83469b)

## Project Structure
- `app.py`: Main Flask application file.
- `requirements.txt`: File containing Python dependencies.
- `Dockerfile`: Docker configuration file to build the Docker image.

Feel free to modify the Flask application code (`app.py`) to customize your application according to your requirements.
