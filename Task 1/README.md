# Flask API for Managing App Details

This project is a Python-based API built using Flask to manage app details. It provides the following endpoints:

1. **POST /add-app**: Add app details to the database.
2. **GET /get-app/{id}**: Retrieve app details by ID.
3. **DELETE /delete-app/{id}**: Remove an app by ID.

## Requirements

- Python 3.7 or higher
- Flask (Python package)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <https://github.com/gurinder-25/Adstack-Assessment>
   cd <https://github.com/gurinder-25/Adstack-Assessment/tree/main/Task%201>
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install flask
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the API**:
   The API will be available at `http://127.0.0.1:5000/`.

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

- The current implementation uses an in-memory database (Python dictionary). Persistent storage (e.g., SQLite or PostgreSQL) will be integrated in Task 2.
- Run the application in debug mode for development purposes. Disable it in production.


## Author
[Gurinder Singh]
