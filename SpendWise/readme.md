# 💸 SpendWise

SpendWise is a personal expense tracking web application built with **Python**, **Flask**, **SQLAlchemy**, **SQLite**, **Jinja2**, **TailwindCSS**, and **Chart.js**.

The application helps users manage and visualize their expenses through an intuitive dashboard interface.

---

# ✨ Features

## 📌 Expense Management (CRUD)

- ➕ Create expenses
- 📖 View all expenses
- ✏️ Edit existing expenses
- ❌ Delete expenses

---

## 🔍 Filtering System

Users can filter expenses by:

- 📅 Start date
- 📅 End date
- 🗂️ Category

---

## 📊 Charts & Analytics

- 🥧 Pie chart for expenses by category
- 📈 Daily spending chart

---

## 📁 CSV Export

- Export filtered expenses to CSV files

---

## ✅ Validation & Error Handling

- Positive amount validation
- Date validation
- Category validation
- Required field validation
- Flash success/error messages

---

# 🛠️ Technologies Used

## Backend

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite

## Frontend

- HTML5
- TailwindCSS
- Jinja2
- Chart.js

---

# 📂 Project Structure

```text
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
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/spendwise.git
```

---

## 2️⃣ Navigate to the project folder

```bash
cd spendwise
```

---

## 3️⃣ Create a virtual environment

### Windows

```bash
python -m venv .venv
```

---

## 4️⃣ Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

---

## 5️⃣ Install dependencies

```bash
pip install flask flask-sqlalchemy
```

---

# ▶️ Running the Application

Start the Flask development server:

```bash
python app.py
```

Open your browser and access:

```text
http://127.0.0.1:5000
```

---

# 🗄️ Database

The application uses **SQLite** for storing expense data.

Database file:

```text
spendwise.db
```

The database and tables are automatically created when the application starts.

---

# 📤 CSV Export

SpendWise supports exporting filtered expenses as CSV files.

The exported file includes:

- Description
- Amount
- Category
- Date

---

# 🖼️ Application Pages

## 🏠 Dashboard

Features included:

- Expense table
- Filtering system
- Expense statistics
- Charts
- Total expenses
- CSV export

---

## ✏️ Edit Expense Page

Allows users to:

- Modify expense information
- Validate input fields
- Save changes

---

# 🚀 Future Improvements

Possible future features:

- 🔐 User authentication
- 💰 Monthly budgets
- 🔁 Recurring expenses
- 🌙 Dark/light mode switch
- 🔎 Expense search
- 📊 Advanced sorting
- 📄 PDF reports
- 📱 Responsive mobile improvements
- 🐳 Docker support

---

# 🎯 Learning Objectives

This project was built to practice:

- Flask routing
- SQLAlchemy ORM
- CRUD operations
- Database filtering
- Form validation
- Jinja2 templating
- Data visualization with Chart.js
- CSV export functionality
- Full-stack web development fundamentals

---

# 👨‍💻 Author

**Bogdan Bodescu**

---

# 📜 License

This project was created for educational purposes.
