import csv
import random
import time
import update_CSV
from setup_logging import logger
 
class SensorTask:
    CSV_FILE = "patient_data.csv"
    FIELDNAMES = ['id', 'name', 'bp', 'heartrate', 'contact', 'family_contact']
 
    def initialize_csv(self):
        try:
            with open(self.CSV_FILE, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.FIELDNAMES)
                writer.writeheader()
                writer.writerows([
                    {'id': '001', 'name': 'Aman', 'bp': 120, 'heartrate': 80, 'contact': 'mohd.aman@hcltech.com', 'family_contact': 'madduri.suryateja@hcltech.com'},
                    {'id': '002', 'name': 'Surya', 'bp': 100, 'heartrate': 89, 'contact': 'hritik.jindal@hcltech.com', 'family_contact': 'mohd.aman@hcltech.com'},
                    {'id': '003', 'name': 'Rohan', 'bp': 115, 'heartrate': 72, 'contact': 'madduri.suryateja@hcltech.com', 'family_contact': 'hritik.jindal@hcltech.com'}
                ])
            logger.info("Patient CSV initialized successfully.")
        except Exception as e:
            logger.error(f"Error initializing patient CSV: {e}")
            raise
 
    def update_csv(self):
        try:
            update_CSV.changeData("patient_data.csv", "id", "001", "bp", random.randint(140, 180))
            update_CSV.changeData("patient_data.csv", "id", "001", "heartrate", random.randint(40, 60))
            logger.info("Patient data updated successfully.")
        except Exception as e:
            logger.error(f"Error updating patient CSV: {e}")
            raise
 