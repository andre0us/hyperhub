# HyperHub

HyperHub is a Python-based utility for data recovery and system restore on Windows, designed to prevent data loss by enabling users to create and manage backups and system restore points.

## Features

- **Create Backups:** Easily create backups of specified directories to prevent data loss.
- **Restore Backups:** Restore your data from previously created backups.
- **List Backups:** View all available backups to manage your data efficiently.
- **Create System Restore Points:** Utilize PowerShell to create system restore points for your Windows system, allowing easy recovery from system changes or failures.

## Requirements

- Python 3.x
- Windows operating system
- Administrative privileges for creating system restore points

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Ensure you have Python 3 installed on your system.

## Usage

```bash
python hyperhub.py
```

You can modify the `hyperhub.py` file to include specific directories for backup or restore. Example usage includes:

- Creating a backup:

  ```python
  hyperhub.create_backup("C:\\path\\to\\your\\data")
  ```

- Restoring a backup:

  ```python
  hyperhub.restore_backup("backup_20231015_123456", "C:\\path\\to\\restore")
  ```

- Listing available backups:

  ```python
  hyperhub.list_backups()
  ```

- Creating a system restore point:

  ```python
  hyperhub.create_system_restore_point()
  ```

## Logging

All operations are logged in `hyperhub.log` for troubleshooting and tracking purposes.

## Disclaimer

This program requires administrative privileges to create system restore points. Use with caution, as improper use may result in data loss or system instability. Always ensure you have current backups before proceeding with restore operations.

## License

This project is licensed under the MIT License - see the LICENSE file for details.