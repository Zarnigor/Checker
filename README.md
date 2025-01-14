# Checker Project

## Overview
The Checker Project is a Django-based web application designed to utilize PostgreSQL as the database backend and REST APIs for communication. This document provides guidance on setting up the project and configuring the environment variables.

## Requirements
- Python (>=3.8)
- Django (>=3.2)
- PostgreSQL (>=12)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd checker_project
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file in the project root directory and add the following content:
   ```env
   SECRET_KEY=django_secret_key
   POSTGRES_DB=checker_project
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   ```

   Make sure to replace the default values with your own configuration if needed.

5. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

   The application will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Features
- PostgreSQL database integration
- REST API endpoints for data access

## Environment Variables
The project requires the following environment variables to be set in the `.env` file:

| Variable         | Description                              |
|------------------|------------------------------------------|
| `SECRET_KEY`     | Django's secret key for security         |
| `POSTGRES_DB`    | Name of the PostgreSQL database          |
| `POSTGRES_USER`  | Username for the PostgreSQL database     |
| `POSTGRES_PASSWORD` | Password for the PostgreSQL user       |
| `POSTGRES_HOST`  | Host address of the PostgreSQL server    |
| `POSTGRES_PORT`  | Port number for the PostgreSQL server    |

## Notes
- Ensure that your `.env` file is not shared publicly or included in version control.
- Use strong passwords and secure configurations for production environments.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

