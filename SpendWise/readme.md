SpendWise

SpendWise is a personal expense tracker web application built with Python, Flask, SQLAlchemy, SQLite, Jinja2, TailwindCSS, and Chart.js.

The application allows users to:

add expenses
edit expenses
delete expenses
filter expenses
visualize spending data using charts
export filtered data as CSV files
Features
Expense Management (CRUD)
Create new expenses
Read/display all expenses
Update existing expenses
Delete expenses
Filtering

Users can filter expenses by:

start date
end date
category
Charts & Analytics
Pie chart for spending by category
Daily spending chart
CSV Export
Export filtered expenses to CSV
Validation
Positive amount validation
Date validation
Category validation
Required field validation
Flash Messages

User-friendly success and error messages.

Technologies Used
Backend
Python 3
Flask
Flask-SQLAlchemy
SQLAlchemy
SQLite
Frontend
HTML5
TailwindCSS
Jinja2
Chart.js
Project Structure
spendwise/
│
├── static/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── edit.html
│
├── app.py
├── requirements.txt
├── README.md
└── spendwise.db
Installation
1. Clone the repository
git clone https://github.com/your-username/spendwise.git
2. Navigate to the project folder
cd spendwise
3. Create a virtual environment
Windows
python -m venv .venv
Activate virtual environment
.venv\Scripts\activate
4. Install dependencies
pip install flask flask-sqlalchemy
Running the Application

Start the Flask development server:

python app.py

Open your browser and go to:

http://127.0.0.1:5000
Database

The application uses SQLite for data persistence.

Database file:

spendwise.db

SQLAlchemy automatically creates the database and tables at startup.

CSV Export

The application supports exporting filtered expenses as CSV files.

Export includes:

Description
Amount
Category
Date
Screenshots
Dashboard
Expense table
Filters
Charts
Total expenses
Edit Expense
Expense editing form
Validation messages
Future Improvements

Possible future features:

User authentication
Monthly budgets
Recurring expenses
Dark/light theme switch
Expense search
Sorting by amount/date/category
PDF reports
Dashboard statistics
Docker support
Learning Objectives

This project was created to practice:

Flask routing
SQLAlchemy ORM
CRUD operations
Database filtering
HTML templating with Jinja2
Form handling and validation
Data visualization with Chart.js
CSV export
Full-stack web development basics
Author

Bogdan Bodescu

License

This project is for educational purposes.