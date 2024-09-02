# Django Product Data Management API

This project is a Django-based API for managing product data, user authentication with JWT, and interactive API documentation using Swagger and ReDoc. The API includes endpoints for user sign-up, login, token refresh, data loading, and summary report generation.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Server](#running-the-server)
  - [Accessing API Documentation](#accessing-api-documentation)
  - [Data Loading and Cleaning](#data-loading-and-cleaning)
  - [Generating the Summary Report](#generating-the-summary-report)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Sign-Up, Login, and JWT-based Authentication**
- **Product Data Management**
- **Data Cleaning with Missing Value Handling**
- **Summary Report Generation**
- **Interactive API Documentation with Swagger and ReDoc**

## Requirements

- Python 3.x
- Django 3.x
- PostgreSQL (or another relational database)

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment
Create a virtual environment to manage your project's dependencies:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the necessary dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt
```
### 4. Configure the Database
Edit the settings.py file in your project directory to configure the database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage

### Running the Server

The server will start at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Accessing API Documentation

The API documentation can be accessed via the following URLs:

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

These interactive interfaces allow you to explore and test the API endpoints.

### Data Loading and Cleaning

To load and clean product data from a CSV file, use the custom management command:

```bash
python manage.py load_products --file path/to/your/file.csv
```
### Generating the Summary Report
To generate a summary report of the product data, use the custom management command:

```bash
python manage.py generate_report
```
