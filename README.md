# Tz

TZ is a CRUD (Create, Read, Update, Delete) application that allows users to manage tasks. It is built using Django, and includes features such as user authentication, database persistence (using PostgreSQL), automated testing with GitHub Actions, containerization with Docker, and linting with Flake8. The application is deployed on Railway, which provides a PostgreSQL database for storing data.

# Installation
To install and run the tz application on your local development environment, follow these steps:

1. git clone https://github.com/yourusername/project-name.git

Change to the project directory:

2. Copy code
3. cd project-name

Build and run the Docker container:

4. Copy code
5. docker-compose up

The application will be started with the following commands:

`python manage.py wait_for_db &&`

`python manage.py makemigrations &&`

`python manage.py migrate &&`

`python manage.py runserver 0.0.0.0:8000`

Access the application in your web browser:

http://127.0.0.1/scheduler/main/

Endpoints
The following endpoints are available in the TZ application:

> 127.0.0.1:8000/scheduler/main/: This endpoint displays the main page with a list of objects.

> 127.0.0.1:8000/scheduler/main/<int:pk>/: This endpoint displays the page for a single object by its ID.

> 127.0.0.1:8000/scheduler/create-record/: This endpoint displays the create object page.

> 127.0.0.1:8000/scheduler/update-record/<int:pk>/: This endpoint displays the change page for a single object by its ID.

> 127.0.0.1:8000/scheduler/delete-record/<int:pk>/: This endpoint displays the page for deleting a single object by its ID.

> 127.0.0.1:8000/scheduler/login/: This endpoint displays the login page.

> 127.0.0.1:8000/scheduler/logout/: This endpoint displays the logout page.

> 127.0.0.1:8000/scheduler/register/: This endpoint displays the registration page.

> 127.0.0.1:8000/scheduler/update_user/: This endpoint displays the page for changing user data.

> 127.0.0.1:8000/scheduler/password/: This endpoint displays the page for changing user password.

> 127.0.0.1:8000/scheduler/password/change/done/: This endpoint displays the password change confirmation page.

Testing
The Project Name application is fully test wrapped, ensuring the quality and reliability of the code. To run the tests, you can use the following command:

`docker-compose run --rm app sh -c "python manage.py test"`

Linting
The Project Name application follows linting best practices using Flake8. To run the linting checks, you can use the following command:

`docker-compose run --rm app flake8`

# Deployment
The Project Name application is deployed on Railway, which provides a PostgreSQL database for storing data. To deploy the application, follow the instructions provided by Railway for deploying a Dockerized Django application.

# Contributing
If you would like to contribute to the Project Name application, please follow the standard practices for contributing to open source projects. Fork the repository, create a feature branch, make changes, and submit a pull request for review.


License
The Project Name application is open source and available under the MIT License.