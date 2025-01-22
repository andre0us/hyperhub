import os
import shutil
import logging
from datetime import datetime
import subprocess

# Configure logging
logging.basicConfig(filename='hyperhub.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

class HyperHub:
    def __init__(self, backup_dir='C:\\HyperHubBackups'):
        self.backup_dir = backup_dir
        os.makedirs(self.backup_dir, exist_ok=True)
        logging.info("Initialized HyperHub with backup directory: %s", self.backup_dir)

    def create_backup(self, target_dir):
        """Creates a backup of the specified directory."""
        try:
            if not os.path.exists(target_dir):
                raise ValueError(f"The target directory {target_dir} does not exist.")

            backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            backup_path = os.path.join(self.backup_dir, backup_name)

            shutil.copytree(target_dir, backup_path)
            logging.info("Backup created at %s", backup_path)
            print(f"Backup successfully created at {backup_path}")
        except Exception as e:
            logging.error("Failed to create backup: %s", e)
            print(f"Error creating backup: {e}")

    def restore_backup(self, backup_name, restore_path):
        """Restores a backup to the specified directory."""
        try:
            backup_path = os.path.join(self.backup_dir, backup_name)

            if not os.path.exists(backup_path):
                raise ValueError(f"The backup {backup_name} does not exist.")

            if os.path.exists(restore_path):
                raise ValueError(f"The restore path {restore_path} already exists.")

            shutil.copytree(backup_path, restore_path)
            logging.info("Backup %s restored to %s", backup_name, restore_path)
            print(f"Backup successfully restored to {restore_path}")
        except Exception as e:
            logging.error("Failed to restore backup: %s", e)
            print(f"Error restoring backup: {e}")

    def list_backups(self):
        """Lists all available backups."""
        try:
            backups = os.listdir(self.backup_dir)
            if not backups:
                print("No backups available.")
                logging.info("No backups available.")
            else:
                print("Available backups:")
                for backup in backups:
                    print(backup)
                    logging.info("Available backup: %s", backup)
        except Exception as e:
            logging.error("Failed to list backups: %s", e)
            print(f"Error listing backups: {e}")

    def create_system_restore_point(self):
        """Creates a system restore point."""
        try:
            # Using PowerShell to create a system restore point
            subprocess.run(["powershell", "-Command",
                            "Checkpoint-Computer -Description 'HyperHub Restore Point' -RestorePointType 'MODIFY_SETTINGS'"],
                           check=True)
            logging.info("System restore point created successfully.")
            print("System restore point created successfully.")
        except subprocess.CalledProcessError as e:
            logging.error("Failed to create system restore point: %s", e)
            print(f"Error creating system restore point: {e}")

if __name__ == "__main__":
    hyperhub = HyperHub()
    # Example usage:
    # hyperhub.create_backup("C:\\path\\to\\your\\data")
    # hyperhub.restore_backup("backup_20231015_123456", "C:\\path\\to\\restore")
    # hyperhub.list_backups()
    # hyperhub.create_system_restore_point()