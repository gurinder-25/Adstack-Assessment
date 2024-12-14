# Virtual Android System Simulation

This project simulates a virtual Android environment using Python. The script performs the following tasks:

1. Launches a virtual Android system.
2. Installs a sample app (APK file).
3. Logs system information such as OS version, device model, and available memory.

## Requirements

- Python 3.7 or higher

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gurinder-25/Adstack-Assessment
   cd Adstack-Assessment/Task 3
   ```

2. **Run the script**:
   ```bash
   python virtual_android.py
   ```

## Script Overview

### Methods in `virtual_android.py`

1. **`launch_system()`**:
   - Simulates launching a virtual Android system.
   - Logs messages indicating the launch status.

2. **`install_app(apk_name)`**:
   - Simulates installing an APK file.
   - Verifies if the file has a `.apk` extension before "installing."
   - Logs success or failure messages.

3. **`log_system_info()`**:
   - Logs the system information, including:
     - OS Version
     - Device Model
     - Available Memory

4. **`list_installed_apps()`**:
   - Lists all installed apps on the virtual Android system.
   - Logs messages indicating installed apps or if no apps are installed.

## Sample Run

### Script Execution Output

1. Launching the system:
   ```
   2024-12-14 14:00:00 - Launching the virtual Android system...
   2024-12-14 14:00:05 - System launched successfully.
   ```

2. Logging system information:
   ```
   2024-12-14 14:00:10 - Retrieving system information...
   2024-12-14 14:00:10 - os_version: Android 12
   2024-12-14 14:00:10 - device_model: VirtualPixel 4
   2024-12-14 14:00:10 - available_memory: 2048 MB
   ```

3. Installing an app:
   ```
   2024-12-14 14:00:15 - Installing app: SampleApp.apk...
   2024-12-14 14:00:20 - App 'SampleApp.apk' installed successfully.
   ```

4. Listing installed apps:
   ```
   2024-12-14 14:00:25 - Listing installed apps...
   2024-12-14 14:00:25 - Installed app: SampleApp.apk
   ```

# ALSO THE ABOVE TIMESTAMPS ARE WHEN I TESTED THIS ON MY LOCAL MACHINE 


## Notes

- This script is a simulation and does not interact with actual Android emulators or devices.
- Extend the functionality using libraries like QEMU or Android Emulator Plugin if needed.
- Customize system details and app installation logic as required.

## Author
Gurinder Singh