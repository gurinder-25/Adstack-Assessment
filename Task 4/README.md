# Basic Networking Script for Virtual Android System

This project demonstrates connecting the Virtual Android System (from Task 3) to a backend Flask API (from Task 1). The script establishes an HTTP connection, sends mock data, and logs the server's response.

## Features

1. **HTTP Connection**:
   - Uses the Flask API endpoint (`POST /add-app`) to send data.
2. **Mock Data**:
   - Includes device ID, OS version, device model, and available memory.
3. **Server Response Logging**:
   - Logs the server's response after sending the mock data.

## Requirements

- Python 3.7 or higher
- Flask server running from Task 1
- Python library: `requests`

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gurinder-25/Adstack-Assessment
   cd Adstack-Assessment/Task 4
   ```

2. **Install dependencies**:
   ```bash
   pip install requests
   ```

3. **Ensure the Flask server is running**:
   - Start the server from Task 1:
     ```bash
     python app.py
     ```
   - The server should run at `http://127.0.0.1:5000/`.

4. **Run the Networking Script**:
   - Execute the script:
     ```bash
     python networking_script.py
     ```

## Script Overview

### Mock Data Sent to Server

```json
{
    "app_name": "Virtual Device Info",
    "version": "Android 12",
    "description": "Model: VirtualPixel 4, Memory: 2048 MB"
}
```

### Server Response

1. **Success**:
   ```json
   {
       "message": "App added successfully",
       "app": {
           "id": 1,
           "app_name": "Virtual Device Info",
           "version": "Android 12",
           "description": "Model: VirtualPixel 4, Memory: 2048 MB"
       }
   }
   ```

2. **Error (e.g., Server Not Running)**:
   ```bash
   ERROR: Failed to send data to server: HTTPConnectionPool(host='127.0.0.1', port=5000): Max retries exceeded
   ```

## Notes

- Ensure the Flask server is running before executing the script.
- Replace `SERVER_URL` in `networking_script.py` if the Flask API is hosted on a different URL or port.
- This script uses HTTP POST for simplicity. Extend it to other methods (e.g., GET, DELETE) as needed.

## Author
Gurinder Singh
