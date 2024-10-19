# Rule Engine Assignment and Weather Monitoring System

## Overview

This project implements a Rule Engine that evaluates user-defined rules based on various attributes, such as age, salary, and experience. The engine uses an Abstract Syntax Tree (AST) for parsing and evaluating conditions.

## Features

- Create rules using a simple string syntax.
- Evaluate rules against user data.
- Support for combining multiple rules using logical operators (AND, OR).
- Comprehensive error handling for invalid rule strings and data formats.

## Technologies Used

- **Backend:** Flask
- **Database:** PostgreSQL
- **Frontend:** React
- **Python Libraries:** `Flask`, `psycopg2-binary`

## Prerequisites

1. Python 3.8 or higher
2. PostgreSQL 17 or higher

## Bonus Features
Error handling for invalid rule strings.
Validations for attribute catalogs.
Modification of existing rules.
Additional Notes
For more advanced usage, consider extending the rule language with user-defined functions.
## Installation

### Step 1: Clone the Repository
git clone https://github.com/AbdulDayyan1/Assignments.git
cd Assignments/rule_engine
Step 2: Set Up the Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Step 3: Database Setup
Ensure PostgreSQL is running.
Create the database:
sql
CREATE DATABASE rule_engine;
Run the SQL schema provided in the rule_engine_schema.sql to set up the necessary tables.
Step 4: Run the Application
python app.py
Step 5: Frontend Setup
Open a new terminal and navigate to the frontend directory.
Run the React application (ensure you have Node.js installed):
npm install
npm start
Usage
Creating Rules: Send a POST request to /api/rules with a JSON body containing the name and rule_string.
Evaluating Rules: Send a POST request to /api/evaluate with a JSON body containing user_data (in JSON format) and rule_ids (comma-separated IDs of the rules to evaluate).
Testing
The application includes unit tests that ensure the functionality of rule creation, combination, and evaluation.


Weather Monitoring System

Overview
The Weather Monitoring System is a real-time data processing application that monitors weather conditions using the OpenWeatherMap API. It provides users with detailed weather information, including daily summaries, temperature visualizations, and alerts for specific weather conditions.

Features
Real-time weather data retrieval
Daily weather summaries including average, maximum, and minimum temperatures
Visual representation of temperature changes using line charts
User-friendly interface built with React
Prerequisites
Before you begin, ensure you have the following installed:

Node.js (v14 or later)
Python (v3.6 or later)
PostgreSQL (v12 or later)
API Key
To use the OpenWeatherMap API, you will need an API key. You can get your API key by signing up at OpenWeatherMap. Once you have your key, replace the placeholder in weather.py with your actual API key.

API_KEY = "0d5776e26aa6c0960bf7499b5a3e3ee7" #this is my api key you can use yours 
Project Structure
bash
Copy code
WeatherMonitoringSystem/
│
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── weather.py             # Weather data retrieval and processing
│
└── frontend/
    ├── WeatherMonitoringSystem.js  # Main React component for the frontend
    └── index.js                # Entry point for the React application
Setup Instructions
Backend Setup
Navigate to the backend directory:


cd backend
Install the required Python packages:

pip install flask requests psycopg2
Run the backend server:

python app.py
Frontend Setup
Navigate to the frontend directory:

cd frontend
Install the required Node.js package

npm install
Start the frontend application:

npm start
Running the Application
Once both the backend and frontend servers are running, you can access the Weather Monitoring System by visiting http://localhost:3000 in your web browser.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
OpenWeatherMap API for providing weather data.
React for building the frontend interface.
Flask for the backend API development.
