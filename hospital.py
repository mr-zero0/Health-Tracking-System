import csv
import math
from setup_logging import logger
 
file2 = "hospital.csv"
fieldnames = ['Id', "Hospital_Name", "Address", "Mail", "x", "y"]
 
def initiate():
    try:
        with open(file2, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows([
                {'Id': '101', "Hospital_Name": 'AIIMS', "Address": 'Delhi', "Mail": 'mail@mail.com', "x": 43, "y": 20},
                {'Id': '102', "Hospital_Name": 'Fortis', "Address": 'Noida', "Mail": 'mail@mail.com', "x": -54, "y": 43},
                {'Id': '103', "Hospital_Name": 'Apollo', "Address": 'Delhi', "Mail": 'mail@mail.com', "x": 74, "y": -67.8},
                {'Id': '104', "Hospital_Name": 'Max', "Address": 'Gurgaon', "Mail": 'mail@mail.com', "x": -31, "y": -48.05}
            ])
        logger.info("Hospital CSV initialized successfully.")
        # a = 5/0
    except Exception as e:
        logger.error(f"Error while initializing hospital CSV: {e}")
        raise
 
def get_location():
    try:
        loc = []
        with open(file2, 'r', newline='') as file:
            reader = csv.DictReader(file)
            loc = [[read['x'], read['y']] for read in reader]
        logger.info("Hospital locations retrieved.")
        return loc
    except Exception as e:
        logger.error(f"Error retrieving hospital locations: {e}")
        raise
 
def nearest_hospital(patient_location_x, patient_location_y):
    try:
        hospital_loc = get_location()
        distances = [distance(float(i[0]), float(i[1]), patient_location_x, patient_location_y) for i in hospital_loc]
        nearest_index = distances.index(min(distances))
        logger.info(f"Nearest hospital found at index: {nearest_index}")
        return get_hospital_eMail(nearest_index)
    except Exception as e:
        logger.error(f"Error finding nearest hospital: {e}")
        raise
 
def get_hospital_eMail(index):
    try:
        with open(file2, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for idx, row in enumerate(reader):
                if idx == index:
                    logger.info(f"Hospital eMail found: {row['Mail']}")
                    return row['Mail']
    except Exception as e:
        logger.error(f"Error retrieving hospital eMail: {e}")
        raise
 
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)