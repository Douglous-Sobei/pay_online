# Pay Online: Payment Backend Logic and Setup Guide

Welcome to Payonline! This Django-based payment backend system is designed to facilitate various payment operations and transactions. This README provides a comprehensive guide on setting up the project, configuring its components, and utilizing its functionalities.

## Project Structure
- **bank system**: Django project directory containing project-wide settings and configurations.
- **core**: Django app for core functionalities and utilities.
- **userauths**: Django app for user authentication and management.
- **account**: Django app for managing user accounts, transactions, and payment-related functionalities.

## Setup Instructions
1. **Clone the repository**: 
    ```bash
    git clone https://github.com/Douglous-Sobei/pay_online
    ```
   This will clone the project repository to your local machine.

2. **Navigate to the project directory**: 
    ```bash
    cd pay_online
    ```
   Move into the project directory where the code is located.

3. **Install project dependencies**: 
    ```bash
    pip install -r requirements.txt
    ```
   This command installs all the required Python packages specified in the `requirements.txt` file.

4. **Perform database migrations**: 
    ```bash
    python manage.py migrate
    ```
   Run database migrations to create database tables and apply any schema changes.

5. **Create a superuser** for accessing the Django admin: 
    ```bash
    python manage.py createsuperuser
    ```
   Follow the prompts to create a superuser account with administrative privileges.

6. **Collect static files**: 
    ```bash
    python manage.py collectstatic
    ```
   Collect static files from all installed apps and copy them to the `STATIC_ROOT` directory.

7. **Run the development server**: 
    ```bash
    python manage.py runserver
    ```
   Start the development server to run the Django application locally.

## Deployment

The project is deployed on Railway, using PostgreSQL for the database. Static files are hosted on AWS S3 for efficient delivery and management.

### Configuration Steps

1. **Setup Railway Environment**:
   - Create an account on Railway ([railway.app](https://railway.app)) if you haven't already.
   - Install the Railway CLI by following the instructions provided in the Railway documentation.

2. **Create PostgreSQL Database**:
   - Create a new PostgreSQL database instance on Railway.
   - Update the `DATABASES` setting in `settings.py` with the PostgreSQL database credentials provided by Railway.

3. **Deploy to Railway**:
   - Initialize a new Railway project in the project directory using the Railway CLI.
   - Deploy the project to Railway using the `railway up` command.

4. **Host Static Files on AWS S3**:
   - Set up an AWS S3 bucket for hosting static files.
   - Configure the AWS credentials in the project settings or using environment variables.
   - Collect static files and upload them to the AWS S3 bucket.

5. **Update Allowed Hosts**:
   - Add the domain provided by Railway to the `ALLOWED_HOSTS` setting in `settings.py`.

6. **Finalize Deployment**:
   - Restart the Railway service to apply the configuration changes.
   - Access the deployed application using the provided domain or URL.

### Contact Information

- **Name**: Douglous Sobei
- **Email**: [douglousmangoyi@gmail.com](mailto:douglousmangoyi@gmail.com)
- **Phone**: [+254701132861](tel:+254701132861)
- **LinkedIn**: [Douglous Mangoyi](https://www.linkedin.com/in/douglous-mangoyi/)

Feel free to reach out if you encounter any issues or need further assistance with the deployment process.

