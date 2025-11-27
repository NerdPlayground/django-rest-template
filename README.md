# Django REST Application Template
This template is used to setup the base for your Django RESTful API. It comes with the following;
- Packages
    - Python Decouple - which connects the environment variables to the application
    - Psycopg - PostgreSQL database adapter for Python
    - DJ Database URL - parses the database URLs into Django's DATABASES settings format
    - DRF Spectacular - sane and flexible OpenAPI 3 schema generation for Django REST framework
- Endpoints;
    - Application schema
    - Swagger Documentation

## Implementing the template
1. Click on `Use this template` and then `Create a new repository`
2. Clone your new repository into an empty directory
3. Setup your virtual environment
    - Create the virtual environment; `python -m venv <virtual environment name>`
    - Activate the environment; `source <virtual environment name>/Scripts/activate`
    - To deactivate the environment; `deactivate`
4. Setup your PostgreSQL Database using [pgAdmin4](https://www.postgresql.org/download/);
    - Open the application and click on Servers
    - Select a PostgreSQL server and create a database in it
    - Add the following in your env_setup.py file; `USER`, `HOST` and `PORT` (retrieved from the server properties in the **Connection** tab) along with the `NAME` and `PASSWORD` of your database
5. Build the application; `bash build.sh` which will install the application packages, generate the database URL, submit your project's default databases to the server and collect static files
6. Run your application; `python manage.py runserver`