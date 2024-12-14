# Adstacks Media Python Intern Assignment

This repository contains the solutions for the Python Intern Assignment provided by **Adstacks Media**. The assignment is divided into four tasks, testing proficiency in Python programming, backend development, database management, virtual Android system simulation, and networking concepts.

---

## Repository Structure

```
GurinderSingh_PythonInternAssignment/
├── Task1/
│   ├── app.py             # Flask API code for Task 1
│   ├── README.md          # Instructions for Task 1
├── Task2/
│   ├── app.py             # Updated Flask API with database integration
│   ├── populate_db.py     # Script to populate sample data
│   ├── README.md          # Instructions for Task 2
├── Task3/
│   ├── virtual_android.py # Virtual Android System Simulation script
│   ├── README.md          # Instructions for Task 3
├── Task4/
│   ├── networking_script.py # Networking script to send mock data
│   ├── README.md            # Instructions for Task 4
```

---

## Task Summaries

### **Task 1: Backend Development**
- Developed a Flask-based API with the following endpoints:
  - `POST /add-app`: Adds app details.
  - `GET /get-app/{id}`: Retrieves app details by ID.
  - `DELETE /delete-app/{id}`: Deletes an app by ID.
- **Folder**: `Task1`
- **Technologies**: Flask

### **Task 2: Database Management**
- Integrated SQLite with the Flask API using SQLAlchemy.
- Added a script to populate sample data into the database.
- **Folder**: `Task2`
- **Technologies**: Flask, SQLAlchemy

### **Task 3: Virtual Android System Simulation**
- Simulated a virtual Android environment in Python.
- Features:
  - Launch system simulation.
  - Simulate app installation.
  - Log system information (OS version, device model, available memory).
- **Folder**: `Task3`
- **Technologies**: Python

### **Task 4: Basic Networking**
- Connected the virtual Android system to the backend server.
- Sent mock device data to the API.
- Logged the server’s response.
- **Folder**: `Task4`
- **Technologies**: Python, `requests` library

---

## How to Use

### Clone the Repository
```bash
git clone https://github.com/gurinder-25/Adstack-Assessment
cd Adstack-Assessment
```

### Navigate to Each Task Folder
- **Task 1**: `cd Task1`
- **Task 2**: `cd Task2`
- **Task 3**: `cd Task3`
- **Task 4**: `cd Task4`

Refer to each folder's `README.md` for detailed instructions on running and testing the respective scripts.

---

## Author
**Gurinder Singh**

Feel free to reach out for any queries or clarifications!

---

## Acknowledgment
This repository was created as part of the Python Intern Assignment for **Adstacks Media**.
