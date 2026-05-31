# Python Backend Fundamentals & CLI Suite

Welcome to my backend development portfolio! This repository contains a suite of Python command-line interface (CLI) applications designed to demonstrate core software engineering concepts, data persistence methods, and database management.

## 🚀 Projects Included

### 1. OOP-Based ATM Simulation (`/01_atm_simulation`)
A terminal banking application emphasizing Object-Oriented Programming (OOP) principles and file handling.
* **Key Skills:** Python Classes, JSON Data Persistence, Deep Dict/List Mapping, User Authentication State Management.
* **Data Layer:** Flat-file system (`json` module).

### 2. Relational Contact Directory (`/02_sqlite_contact_manager`)
A lightweight database utility for storing, querying, and managing structured user contact information.
* **Key Skills:** SQL Parameterized Queries (SQL Injection Prevention), Exception Handling (`sqlite3.Error`), Pattern Matching via `LIKE`.
* **Data Layer:** Relational Database (`sqlite3` module).

---

## 🛠️ Core Competencies Demonstrated
* **Data Security:** Implemented parameterized SQL bindings to block malicious data injections.
* **Robust Error Handling:** Designed defensive `try-except` blocks protecting the applications from unexpected user inputs and runtime failures.
* **State & Scope Management:** Safe scoping of user sessions post-authentication.

## 📦 How to Run Locally
Clone the repository and run either application from your terminal:
```bash

# To run the ATM project
python 01_atm_simulation/atm_project.py

# To run the Contact Manager project
python 02_sqlite_contact_manager/contact_manager.py
