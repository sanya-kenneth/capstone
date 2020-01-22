# capstone

[![Build Status](https://travis-ci.com/sanya-kenneth/capstone.svg?branch=master)](https://travis-ci.com/sanya-kenneth/capstone)

This project enables teachers to post questions and have those questions answered by students.

#### Heroku url  ` ==> `   `https://fsndcapstone.herokuapp.com`

## Tech Stack
our tech stack consists of the following technologies:
- Python Flask - we use the flask framework for our backend
- PostgreSQL - we use PostgreSQL as our database
- SQLAlchemy - our ORM of choice is SQLAlchemy 

## project Structure
```
.
├── app.py # File contains factory function for creating the app in different environments.
├── auth.py # File contains functions that handle authentication and authorization
├── config.py # File contains configuration information required to run the app in different environments 
├── controllers.py # File contains the core logic for the app
├── models.py # File contains all the models for the app
├── run.py # The app is initialised here
├── utitlities.py # File contains utility functions for the app 
├── views.py # File contains all endpoints for the app
├── procfile # File contains configuration information required to run the app on `heroku`
├── .travis.yml # File contains configuration information required for CI with Travis 
├── .gitignore # File contains a list of files and folders to ignore 
├── migrations/ # folder containing migration files
└── test_app.py # File contains tests for the app
```

## Development Setup

Clone this repository on your machine.

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ python3 -m venv venv
  $ . bin/venv/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run the development server:
  ```
  $ python run.py
  ```

4. Run project tests
  ```
  $ pytest
  ```

## Roles:
 
 - teacher
 - student

 ## Permissions

 ### teacher
 - `add:question`
 - `delete:question`
 - `edit:question`
 - `read:question`
 - `read:answer`
 - `read:answers`
 - `read:questions`

 ### student
 - `add:answer`
 - `read:answer`
 - `read:answers`
 - `read:question`
 - `read:questions`

## Endpoints

| Endpoint        | Permission | Functionality |
| --------        | -------------- |     --------- |
| `GET /questions`| `read:questions` | Fetch all questions |
| `GET /question/<question_id>`| `read:question` | Fetch a specific question |
| `GET /answers` | `read:answers` |Get all answers |
| `GET /answers/<answer_id>`| `read:answer` | Fetch a single answer |
| `POST /questions`| `add:question` | Create a question |
| `POST /question/<question_id>/answers`| `add:answer` | Create an answer |
| `PATCH /question/<question_id>`| `edit:question` | Update a specific question |
| `DELETE /question/<question_id>`| `delete:question` | Delete a specific question |


## Setup Auth0

1. Create a new Auth0 Account

2. Select a unique tenant domain

3. Create a new Regular Web application

4. Create a new API
   - Enable `RBAC` under settings
   - Enable `Add Permissions in the Access Token` under settings

5. Create new API permissions
 - `add:question`
 - `delete:question`
 - `edit:question`
 - `read:question`
 - `read:answer`
 - `read:answers`
 - `read:questions`
 - `add:answer`
 - `read:answer`
 - `read:answers`
 - `read:question`
 - `read:questions`

 6. Create new roles
 - student
 - teacher

 7. Assign permissions for the roles(Use the permissions section of this readme as a guide).

 8. In the auth.py file, replace the following with details from your Auth0 account:
 - `AUTH0_DOMAIN` : use the domain from your Auth0 account
 - `API_AUDIENCE` : use API audience information from your Auth0 account 