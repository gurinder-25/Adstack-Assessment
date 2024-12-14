# Flask API for Managing App Details (with SQLite Integration)

This project is a Python-based API built using Flask and SQLite to manage app details. It provides endpoints to add, retrieve, and delete app details. The database integration is implemented using SQLAlchemy.

## Features
1. **POST /add-app**: Add app details to the database.
2. **GET /get-app/{id}**: Retrieve app details by ID.
3. **DELETE /delete-app/{id}**: Remove an app by ID.

## Requirements

- Python 3.7 or higher
- Flask
- Flask-SQLAlchemy

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone www.github.com/gurinder-25/Adstack-Assessment
   cd Adstack-Assessment/Task 2
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install flask flask-sqlalchemy
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the API**:
   The API will be available at `http://127.0.0.1:5000/`.

6. **(Optional) Populate Sample Data**:
   - Run the script to add sample data to the database:
     ```bash
     python populate_db.py
     ```
   - This will add three sample apps to the database.

## API Endpoints

### 1. Add App Details
**Endpoint**: `POST /add-app`

**Request Body** (JSON):
```json
{
    "app_name": "Sample App",
    "version": "1.0",
    "description": "This is a sample app."
}
```

**Response**:
- **201 Created**:
  ```json
  {
      "message": "App added successfully",
      "app": {
          "id": 1,
          "app_name": "Sample App",
          "version": "1.0",
          "description": "This is a sample app."
      }
  }
  ```
- **400 Bad Request**:
  ```json
  {
      "error": "Invalid data, all fields (app_name, version, description) are required"
  }
  ```

### 2. Get App Details by ID
**Endpoint**: `GET /get-app/{id}`

**Response**:
- **200 OK**:
  ```json
  {
      "app": {
          "id": 1,
          "app_name": "Sample App",
          "version": "1.0",
          "description": "This is a sample app."
      }
  }
  ```
- **404 Not Found**:
  ```json
  {
      "error": "No app found with ID {id}"
  }
  ```

### 3. Delete App by ID
**Endpoint**: `DELETE /delete-app/{id}`

**Response**:
- **200 OK**:
  ```json
  {
      "message": "App deleted successfully",
      "app": {
          "id": 1,
          "app_name": "Sample App",
          "version": "1.0",
          "description": "This is a sample app."
      }
  }
  ```
- **404 Not Found**:
  ```json
  {
      "error": "No app found with ID {id}"
  }
  ```

## Notes

- Ensure the database file `apps.db` is in the same directory as `app.py` when running the application.
- Use the `sample_data.py` script to add initial sample data for testing.
- Run the application in debug mode for development purposes. Disable it in production.

## Author
Gurinder Singh
