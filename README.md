#BMI Calculator Project

A web-based Body Mass Index (BMI) Calculator built using the Django framework.
This application allows users to calculate their BMI based on height and weight, categorize the result, and view BMI history records.

##Project Overview

###The BMI Calculator helps users evaluate their body weight category by calculating BMI using the standard formula:

BMI = weight (kg) / height (m²)

Based on the BMI value, the system categorizes the user into:

Underweight

Normal

Overweight

Obese

The application also provides a simple interface for entering data and viewing BMI results.


##Features

User-friendly BMI calculation interface

Calculates BMI instantly from user input

Displays BMI category

Stores BMI records in database

History page to view previous BMI records

Web-based interface built with Django templates

Lightweight SQLite database integration

##Technologies Used

###Backend:

Python

Django

###Frontend:

HTML

CSS

Django Templates

###Database:

SQLite (default Django database)

###Development Environment:

PyCharm

#Project Structure
**IBM
│
├── bmi_project
│   ├── bmi_app
│   │   ├── migrations
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │
│   ├── bmi_project
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   ├── wsgi.py
│   │
│   ├── templates
│   │   ├── index.html
│   │   ├── history.html
│   │
│   ├── db.sqlite3
│   └── manage.py**
#Installation and Setup

Follow these steps to run the project locally.

1. Clone the repository
git clone https://github.com/your-username/IBM-BMI-Calculator.git
2. Navigate to the project folder
cd bmi_project
3. Create virtual environment
python -m venv .venv

##Activate it:

##Windows:

.venv\Scripts\activate
4. Install dependencies
pip install django
5. Run database migrations
python manage.py migrate
6. Run the development server
python manage.py runserver
7. Open the application

Open your browser and go to:

http://127.0.0.1:8000
#Usage

Enter your height and weight.

Click Calculate BMI.

The application displays:

BMI value

BMI category

Navigate to the History page to view previous BMI records.

#Example BMI Categories
BMI Range	Category
Below 18.5	Underweight
18.5 – 24.9	Normal
25 – 29.9	Overweight
30 and above	Obese
Future Enhancements

#Possible improvements for the project:

1.Add user authentication system
2.Store BMI records per user
3.Add BMI visualization charts
4.Implement responsive UI using Bootstrap
5.Add BMI recommendations and health tips
