# Employee Management System

CLI application written in **Python** for managing employees in a company.  
The program allows adding, searching, modifying, deleting and displaying employees, as well as performing salary calculations.

Employee data is stored in a **JSON file**, ensuring persistence between program executions.

---

# Features

The application provides the following functionalities:

1. Add employee  
2. Search employee by CNP  
3. Modify employee data  
4. Delete employee  
5. Display all employees  
6. Calculate total company salary cost  
7. Calculate total department salary cost  
8. Generate employee payroll (salary slip)  
9. Display employees by seniority  
10. Display employees by department  
11. Exit application  

---

# Project Structure

```
employee-management-system/
│
├── main.py           # Entry point of the application
├── operations.py     # Core business logic and CRUD operations
├── utils.py          # Validation functions and payroll calculations
├── storage.py        # JSON file read/write handling
├── angajati.json     # Data storage file
└── README.md         # Project documentation
```

---

# Employee Data Model

Each employee is stored as a JSON object with the following structure:

```
{
    "cnp": "1960523456789",
    "nume": "Popescu",
    "prenume": "Ion",
    "varsta": 28,
    "salariu": 5000.0,
    "departament": "IT",
    "senioritate": "mid"
}
```

---

# Data Validation

The application validates user input to ensure data integrity:

- CNP must contain **exactly 13 digits**
- Minimum employee age: **18**
- Maximum employee age: **80**
- Minimum salary: **4050**
- Seniority must be one of:
  - `junior`
  - `mid`
  - `senior`
- Names must contain **only letters, spaces or hyphens**

---

# Payroll Calculation

The payroll (salary slip) is calculated using the following formula:

- **CAS** = 10% of gross salary  
- **CASS** = 25% of gross salary  
- **Tax** = 10% of (gross − CAS − CASS)

Final net salary:

```
net = brut - CAS - CASS - tax
```

---

# How to Run the Application

## Requirements

- Python **3.10+**

## Run the program

```
python main.py
```

Follow the CLI menu to interact with the system.

---

# Example Menu

```
===================== MENIU =====================
1) Adăugare angajat
2) Căutare angajat
3) Modificare date angajat
4) Ștergere angajat
5) Afișare angajați
6) Calcul cost total salarii companie
7) Calcul cost total salarii departament
8) Calcul fluturaș salarial
9) Afișare după senioritate
10) Afișare după departament
11) Ieșire
=================================================
```

---

# Technologies Used

- Python
- JSON for persistent storage
- CLI (Command Line Interface)

---

# Design Principles

The project follows modular architecture:

- **main.py** → application entry point and menu handling  
- **operations.py** → business logic and employee operations  
- **utils.py** → validation and payroll calculations  
- **storage.py** → data persistence layer  

This separation improves:

- readability  
- maintainability  
- scalability  

---
