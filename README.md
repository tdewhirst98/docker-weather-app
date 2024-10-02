# Weather App (Dockerized)

This is a simple weather application that fetches weather data using the OpenWeatherMap API. The app is containerized using Docker, making it easy to set up and run.

## Prerequisites

- [Docker](https://www.docker.com/) installed on your machine
- OpenWeatherMap API Key

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app

### 2. Create a `.env` File

In the root of the project directory, create a `.env` file to store your API key and other configurations.

```bash
touch .env


### 3. Update Latitude and Longitude in `weather-app.py`

In the `weather-app.py` file, update the `lat` and `long` variables with your desired location's latitude and longitude:

```python
lat = 'your_latitude'
long = 'your_longitude'


### 4. Build the Docker Image

To build the Docker image, run the following command in the project directory:

```bash
docker build -t weather-app .

### 5. Run the Docker Container

Run the app inside a Docker container by using the following command:

```bash
docker run -d --env-file .env --name weather-app-container weather-app

### 6. View Logs

To view the logs and see the output from the weather app, use the following command:

```bash
docker logs weather-app-container
