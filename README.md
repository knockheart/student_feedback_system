# Student Feedback System

## Scope

* Metadata contains all College, University, Branch & Semister information.
* Created Custom user with inbuild user for custom validation.
* Create feedback events for students from professors, staff, etc.


## Migrate SQL DDL

`python manage.py makemigrations accounts`

`python manage.py sqlmigrate accounts 0001`

`python manage.py migrate`

# ?

* Load initial data
* Add fingerprint auth


## Run Project

### Step1:

Activate virtual environment (create new if not exist)

Create if not exist => $ `python -m venv venv`

$ `venv\Scripts\activate.bat`


### Step2:

run

$ `python manage.py migrate`

$ `python manage.py makemigrations`

$ `python manage.py migrate`

$ `python manage.py runserver`



### Step3:

Visit to admin login => http://127.0.0.1:8000/admin/


![image](https://user-images.githubusercontent.com/32696360/222915433-32d7e376-8c8b-4fa8-8a1c-0b5287dd73e1.png)
