Todowoo Project | A Task Management Web Application

![Python](https://img.shields.io/badge/Language-Python-brightgreen.svg)  ![Django](https://img.shields.io/badge/Framework-Django-brightgreen.svg) 

## Table of Content
  * [Project Overview](#Problem-statment)
  * [Features](#Features)
  * [Technologies](#Technologies)
  * [How to run the project](#How-to-run)
  * [Admin Login](#Admin-Login)

  
## Problem Statment

Todowoo is a robust task management application designed with role-based access control (RBAC) to separate user functionalities:

Admin Users: Access admin page to view all users tasks.
Site Users: Manage personal tasks with user-specific functionalities.
Both roles are strictly segregated to ensure secure and role-specific experiences.

  
## Features

* Role-Based Access Control: Securely separates access for admin users and site users.
* Task Management: Add, edit, and delete tasks.
* User-Friendly Interface: Developed using Bootstrap for an intuitive experience
  

## Technologies

Backend: Python, Django
Frontend: HTML, CSS, Bootstrap
  
  
  
## How to run
  
**Step-1:** Download the files in the repository.<br>

**Step-2:** Get into the downloaded folder, open command prompt in that directory and install all the dependencies using following command.<br>
```python
pip install django
```
**Step-3:** After successfull installation of the dependencies, Open the Command Prompt in the \todowoo-project\todowoo-pro directory.<br>

**Step-4:** Run the command<br> 
```python
python manage.py runserver
```

**Step-5:** Open your browser and navigate to http://127.0.0.1:8000/<br> 

## Admin Login

after Step 3 in above instruction 

**step-3.1** Run the command<br> 
```python
python manage.py createsuperuser
``` 
**step-3.2** Enter username, Password and Email Id<br>

Then continue in step-4.


  