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

Firstly, Open CMD in Windows OS

Activate virtual environment (create new if not exist)

Create if not exist => $ `python -m venv venv`

$ `venv\Scripts\activate.bat`

$ `pip install -r requirements.txt`


### Step2:

run

$ `python manage.py migrate`

$ `python manage.py makemigrations`

$ `python manage.py migrate`

$ `python manage.py runserver`



### Step3:

Visit to admin login => http://127.0.0.1:8000/admin/


![image](https://user-images.githubusercontent.com/32696360/222915433-32d7e376-8c8b-4fa8-8a1c-0b5287dd73e1.png)



## Guide

### Student Dashbood 

#### Main Page : http://127.0.0.1:8000/feedback/s_main/?Dashboard

![image](https://user-images.githubusercontent.com/32696360/226169463-8389b08f-da1a-4c42-8c3c-4fe825fa7a5f.png)

#### Feedback page : http://127.0.0.1:8000/feedback/s_main/?Feedback

![image](https://user-images.githubusercontent.com/32696360/226169547-7b7e2c8c-a9ad-4ff8-b0ec-152a77896245.png)

#### Profile : http://127.0.0.1:8000/feedback/s_main/?Profile

![image](https://user-images.githubusercontent.com/32696360/226169576-3321aca9-26ec-4318-b5c5-9ea7b9465228.png)

#### Logout : http://127.0.0.1:8000/feedback/s_main/?Logout

![image](https://user-images.githubusercontent.com/32696360/226169595-65159872-59a0-426c-9d2e-3323cd6df4a6.png)




