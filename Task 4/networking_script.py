import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class VirtualAndroidNetworking:
    def __init__(self, server_url):
        self.server_url = server_url
        self.device_info = {
            "device_id": "VIRTUAL12345",
            "os_version": "Android 12",
            "device_model": "VirtualPixel 4",
            "available_memory": "2048 MB"
        }

    def send_device_info(self):
        endpoint = f"{self.server_url}/add-app"
        mock_data = {
            "app_name": "Virtual Device Info",
            "version": self.device_info["os_version"],
            "description": (
                f"Model: {self.device_info['device_model']}, "
                f"Memory: {self.device_info['available_memory']}"
            )
        }

        try:
            logging.info(f"Sending mock data to server: {mock_data}")
            response = requests.post(endpoint, json=mock_data)
            response.raise_for_status()
            logging.info(f"Server Response: {response.json()}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send data to server: {e}")

if __name__ == "__main__":
    # Replace with your Flask server URL
    SERVER_URL = "http://127.0.0.1:5000"

    # Initialize networking class
    virtual_network = VirtualAndroidNetworking(SERVER_URL)

    # Send device info to server
    virtual_network.send_device_info()
