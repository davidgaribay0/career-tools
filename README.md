# Career Tools

## What is this?

- This is a small django application. 
- In its current iteration it is only utilizing the admin functionality.
- The objective of it is to keep myself organized when applying for jobs.
- There are a few models catered towards the goal of tracking Companies, JobApplications, Events (such as emails, interviews, etc), and Profiles.
- This way I can stay organized, do research on companies, write down notes, and put my best foot forward when applying to positions. 
- All data entered stays private on your computer.

## Requirements 
- python 3.11 (https://www.python.org)

## How to install

- run `git clone git@github.com:davidgaribay0/career-tools.git`
- create a venv and activate it (https://docs.python.org/3/library/venv.html)
- run `pip install -r requirements.txt` (install dependencies)
- run `python3 manage.py makemigrations;pythong3 manage.py migrate` to initizialize a local database (sqlite)
- run `python3 manage.py createsuperuser` (this step will create a local user account)
- run `python3 manage.py runserver` (this will start the application)
- login to your newly created account using the following url: `localhost:8000/admin/`

## Application

### Adding a company
![companies.png](screenshots%2Fcompanies.png)

### Adding a job application
![job_application_details.png](screenshots%2Fjob_application_details.png)

### Viewing Information
![table_view.png](screenshots%2Ftable_view.png)

