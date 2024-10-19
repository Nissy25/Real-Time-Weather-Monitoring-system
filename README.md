# Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

### Table of contents

1.Introduction

2.Design choices  

3.Dependencies

4.Installation and Setup

5.Running the Application

6.Docker Setup

7.API Documentation

8.Testing

9.Contributing

10.License

### Introduction

This Real-Time Weather Monitoring System ingests live weather data from various sources, processes the data in real time, and stores it in a time-series database (PostgreSQL with TimescaleDB). It provides REST API endpoints to query weather data, view real-time metrics, and access aggregated weather statistics such as temperature, humidity, and wind speed. The system is scalable, containerized using Docker, and provides real-time rollups and aggregates for efficient querying.

### Design Choices

#### Data Ingestion:

- The system ingests real-time weather data either from a simulation script or from actual weather data sources (e.g., sensors, APIs).
- Data is inserted into the PostgreSQL database with the TimescaleDB extension enabled for efficient time-series data storage.

#### Data Aggregation:

- The system computes aggregates (e.g., MAX, MIN, AVG) over time windows such as hourly or daily, using TimescaleDB’s capabilities.
- Data is rolled up to reduce storage costs and improve query performance.

#### REST API:
- A FastAPI-based RESTful API is used for querying real-time weather data and aggregated weather statistics.
- The API supports endpoints for ingesting new data and querying historical or real-time weather data.

#### Containerization:

- The system is containerized using Docker and can be easily deployed with Docker Compose.
- PostgreSQL and FastAPI are both run in separate containers for ease of scalability and maintenance.

### Dependencies

The system requires the following dependencies to run:

- Python 3.x: Required for the application and FastAPI.

- FastAPI: For building the REST API.

- Pandas: For data processing and aggregations.

- SQLAlchemy: ORM for PostgreSQL interactions.

- PostgreSQL: With TimescaleDB for time-series data storage.

- Docker: For containerization of the entire application.

### Installation and Setup

#### Step 1: clone the repository

[Clone the repository from GitHub]()

#### Step 2: Install Dependencies

Create a requirements.txt file with the necessary dependencies.

#### Step 3: Set Up PostgreSQL with TimescaleDB

Ensure that PostgreSQL and TimescaleDB are installed.
- [Install PostgreSQL](https://www.postgresql.org/download/)
- [Install TimescaleDB]( https://docs.timescale.com/install/latest/)

### Running the Application

#### Step 1: Start the FastAPI Application
- Start the FastAPI server using uvicorn.
- This will start the FastAPI application at http://127.0.0.1:8000.

#### Step 2: Run the Weather Data Simulation
- To simulate real-time weather data ingestion, run the following script.
- This will generate and send random weather data (temperature, humidity, wind speed) to the API at regular intervals.

### Docker Setup

#### Step 1: Create a Dockerfile
- Create a Dockerfile to containerize the FastAPI application.

#### Step 2: Create a Docker Compose File
- Create a docker-compose.yml file to orchestrate PostgreSQL and FastAP.

#### Step 3: Build and Run the Containers
- Build and run the Docker containers using Docker Compose.

### API Documentation

The weather monitoring system provides several API endpoints for ingesting and querying weather data.

1.POST /api/weather/ingest: Ingest real-time weather data.

2.GET /api/weather/latest: Retrieve the latest weather data from the database.

3.GET /api/weather/aggregate: Query aggregated weather data (e.g., hourly, daily).

### Testing

To test the system, you can either use Postman or curl for sending HTTP requests to the API:

1.Ingest Weather Data: Use curl to send a POST request for ingesting weather data.

2.Get Latest Weather Data: Use curl to retrieve the latest weather data.

3.Query Aggregated Data: Use curl to query aggregated weather data (e.g., hourly rollups).

### Contributing

Contributions are welcome! Here’s how you can contribute:

1.Fork the repository.

2.Create a new branch for your feature or bug fix.

3.Commit your changes and push them to your fork.

4.Submit a pull request for review.

### License
This project is licensed under the MIT License.
