# Rule Engine Assignment

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
