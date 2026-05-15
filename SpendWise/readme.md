# 💸 SpendWise

SpendWise is a modern expense tracking web application built with Flask, SQLAlchemy, TailwindCSS, and Chart.js.

The application allows users to:
- Add expenses
- Edit expenses
- Delete expenses
- Filter expenses by date and category
- Export filtered expenses to CSV
- Visualize spending data using charts

---

# 🚀 Features

## ✅ Expense Management
- Add new expenses
- Edit existing expenses
- Delete expenses

## ✅ Filtering System
Filter expenses by:
- Start date
- End date
- Category

## ✅ CSV Export
Export filtered expense data into a CSV file.

## ✅ Data Visualization
Interactive charts powered by Chart.js:
- Pie chart for category distribution
- Bar chart for daily spending

## ✅ Validation & Error Handling
- Date validation
- Positive amount validation
- Category validation
- Flash messages for errors/success

## ✅ Clean Architecture
The project is modularized using:
- routes.py
- services.py
- models.py
- extensions.py

---

# 🛠️ Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- TailwindCSS
- Chart.js

---

# 📁 Project Structure

```text
SpendWise/
│
├── app.py
├── routes.py
├── services.py
├── models.py
├── extensions.py
├── requirements.txt
├── README.md
│
├── instance/
│   └── spendwise.db
│
└── templates/
    ├── base.html
    ├── index.html
    └── edit.html
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd SpendWise
```

## 2. Create virtual environment

```bash
python -m venv .venv
```

## 3. Activate virtual environment

### Windows
```bash
.venv\Scripts\activate
```

### Linux / macOS
```bash
source .venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the application

```bash
python app.py
```

---

# 🌐 Access the App

Open your browser and go to:

```text
http://127.0.0.1:5000
```

---

# 📦 Requirements

```text
Flask
Flask-SQLAlchemy
SQLAlchemy
Werkzeug
```

---

# 📊 Charts

SpendWise includes:
- Expense distribution by category
- Daily spending visualization

Powered by Chart.js.

---

# 🧠 Learning Goals

This project demonstrates:
- Flask routing
- SQLAlchemy ORM
- CRUD operations
- Jinja templating
- Form validation
- Type hinting
- Modular project structure
- CSV exporting
- Frontend integration with TailwindCSS and Chart.js

---

# 👨‍💻 Author

Created by Bogdan Bodescu.
