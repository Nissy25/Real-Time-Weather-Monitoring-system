# Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

### Table of contents

1.Project Overview

2.Features  

3.Technologies Used

4.Prerequisites

5.Installation

6.Running the Code

7.Design Choices

8.API Documentation

9.How the Weather Monitoring System Works

10.Testing

11.Contributing

12.Conclusion

---
### Project Overview

This Real-Time Weather Monitoring System ingests live weather data from various sources, processes the data in real time, and stores it in a time-series database (PostgreSQL with TimescaleDB). It provides REST API endpoints to query weather data, view real-time metrics, and access aggregated weather statistics such as temperature, humidity, and wind speed. The system is scalable, containerized using Docker, and provides real-time rollups and aggregates for efficient querying.

---
### Features
- Real-Time Weather Data Fetching: The system fetches live weather data from the OpenWeatherMap API for multiple Indian metros.
- Periodic Data Retrieval: The system fetches weather data at regular intervals (e.g., every 5 minutes).
- Daily Weather Rollups:

  a) Average Temperature: Computes the average temperature throughout the day.

  b) Maximum Temperature: Tracks the highest temperature recorded.

  c) Minimum Temperature: Tracks the lowest temperature recorded.

  d) Dominant Weather Condition: Determines the most frequent weather condition  based on occurance.
- Historical Weather Trends: Stores daily weather summariesin a database for historical analysis and trends.
- Visualization of Weather Data: Data visualization to represent daily weather summaries and trends.
---
### Technologies Used

- Python: Required for the application and Fast API.
- Fast API: For building the REST API.
- Pandas: For data processing and aggregations.
- SQL Alchemy: ORM for PostgreSQL interactions.
- PostgreSQL: With TimescaleDB for time-series data storage.
---
### Prerequisites:
- Python: Ensure Python is installed on your system.

- OpenWeatherMap API Key: You will need a free API key from [OpenWeatherMap](https://openweathermap.org/) to fetch weather data.

- Virtual Environment: For managing dependencies.
---
### Installation
- Clone the repository to your local machine.
```
git clone https://github.com/yourusername/Real-Time-Weather-Monitoring-system.git
cd Real-Time-Weather-Monitoring-system
```
- Install Python

  [Download the latest version of Python](https://www.python.org/downloads/)

- Create a Virtual Environment
```
python -m venv venv
```
- Install Dependencies
  Create a requirements.txt file with the necessary dependencies
```
fastapi==0.68.0
uvicorn==0.15.0
psycopg2-binary==2.9.1
sqlalchemy==1.4.22
pandas==1.3.3
```
Activate the Virtual Environment
- For Windows
```
.\venv\Scripts\activate
```

- For Mac/Linux
```
source venv/bin/activate
```
- Set Up PostgreSQL with TimescaleDB

  Ensure that PostgreSQL and TimescaleDB are installed.
- [Install PostgreSQL](https://www.postgresql.org/download/)
- [Install TimescaleDB]( https://docs.timescale.com/install/latest/)
---
### Running the Code

Run the application using the following command
```
uvicorn app.main:app --reload
```
This will start the FastAPI application at http://127.0.0.1:8000

#### Docker Setup

- The application can be run inside a Docker container for easier setup.

- Build and Run Docker Containers: Use Docker Compose to build and run the containers
```
 docker-compose up --build

```
---
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

---
### API Documentation

The weather monitoring system provides several API endpoints for ingesting and querying weather data.

1.POST /api/weather/ingest: Ingest real-time weather data.

2.GET /api/weather/latest: Retrieve the latest weather data from the database.

3.GET /api/weather/aggregate: Query aggregated weather data (e.g., hourly, daily).

You can explore the API documentation using Swagger UI by navigating to:
```
http://localhost:8000/docs
```
---
### How the Weather Monitoring System Works

The Weather Monitoring System is designed to provide users with real-time weather information and alerts. Below is an overview of its functionality and workflow:

##### 1. Data Retrieval

The system utilizes the **OpenWeatherMap API** to fetch current weather data based on user-specified locations. The API provides various data points, including temperature, humidity, wind speed, and weather conditions. 

#####  2. User Input

Users can input their desired location (city name or geographic coordinates) through the user interface or API endpoints. This input is then used to make requests to the OpenWeatherMap API.

##### 3. API Request and Response

When a user requests weather information, the system constructs an API request and sends it to OpenWeatherMap. The API returns a JSON response containing the relevant weather data for the specified location.

##### 4. Data Processing

  Upon receiving the API response, the system processes the data to extract the necessary information, such as:
- Current temperature
- Weather conditions (e.g., clear, rainy, cloudy)
- Humidity levels
- Wind speed and direction

##### 5. Data Storage

The processed weather data can be stored in a database for historical reference and analytics. This allows users to access past weather data and identify trends over time.

##### 6. Alerts Configuration

Users can configure alerts for specific weather conditions (e.g., extreme temperatures, heavy rainfall). The system monitors the current weather data against the user-defined criteria and sends notifications when conditions meet the specified thresholds.

##### 7. User Interface

The system provides a user-friendly interface, allowing users to:
- View current weather conditions.
- Access historical weather data.
- Set up and manage alerts.
- Interact with the application via an API.

##### 8. Continuous Updates

The system is designed to update weather information at regular intervals (e.g., every few minutes) to ensure users receive the most current data. This feature is crucial for maintaining accurate and relevant weather monitoring.By following this workflow, the Weather Monitoring System effectively provides users with real-time weather updates and customizable alerts, enhancing their awareness and preparedness for varying weather conditions.

---
### Testing

To test the system, you can either use Postman or curl for sending HTTP requests to the API:

1.Ingest Weather Data: Use curl to send a POST request for ingesting weather data.

2.Get Latest Weather Data: Use curl to retrieve the latest weather data.

3.Query Aggregated Data: Use curl to query aggregated weather data (e.g., hourly rollups).

---
### Contributing

1.Fork the repository.

2.Create a new branch for your feature or bug fix.

3.Commit your changes and push them to your fork.

4.Submit a pull request for review.

---

### Conclusion

The Weather Monitoring System serves as a powerful tool for users to stay informed about weather conditions in real time. By leveraging the OpenWeatherMap API, this project not only provides accurate and timely weather data but also allows for customizable alerts tailored to individual preferences. As weather patterns continue to change and affect our daily lives, having access to reliable weather information becomes increasingly important.We encourage developers and contributors to build upon this foundation, adding features and improvements that can further enhance the system's capabilities. 
