# Backsystem: Payment Backend Logic and Setup Guide

Welcome to Backsystem! This Django-based payment backend system is designed to facilitate various payment operations and transactions. This README provides a comprehensive guide on setting up the project, configuring its components, and utilizing its functionalities.

## Project Structure

- **backsystem**: Django project directory containing project-wide settings and configurations.
- **core**: Django app for core functionalities and utilities.
- **userauths**: Django app for user authentication and management.
- **account**: Django app for managing user accounts, transactions, and payment-related functionalities.

## Setup Instructions

1. **Clone the repository**: `git clone https://github.com/Douglous-Sobei/pay_online`
2. **Navigate to the project directory**: `cd pay_online`
3. **Install project dependencies**: `pip install -r requirements.txt`
4. **Perform database migrations**: `python manage.py migrate`
5. **Create a superuser** for accessing the Django admin: `python manage.py createsuperuser`
6. **Collect static files**: `python manage.py collectstatic`
7. **Run the development server**: `python manage.py runserver`

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

Feel free to reach out if you encounter any issues or need further assistance with the deployment process.
