import csv
import math
from setup_logging import logger
 
file1 = "police.csv"
fieldnames = ['Id', "Station_Name", "Address", "Mail", "x", "y"]
 
def initiate():
    try:
        with open(file1, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows([
                {'Id': '001', "Station_Name": 'Noida PS', "Address": 'abc district', "Mail": 'mail@mail.com', "x": 40, "y": 23},
                {'Id': '002', "Station_Name": 'Gurugram PS', "Address": 'pqr district', "Mail": 'mail@mail.com', "x": -44, "y": 53},
                {'Id': '003', "Station_Name": 'Chennai PS', "Address": 'xyz district', "Mail": 'mail@mail.com', "x": 64, "y": -67.8},
                {'Id': '004', "Station_Name": 'Bangalore PS', "Address": 'klm district', "Mail": 'mail@mail.com', "x": -31, "y": -48.05}
            ])
        logger.info("Police CSV initialized successfully.")
    except Exception as e:
        logger.error(f"Error while initializing police CSV: {e}")
        raise
 
def get_location():
    try:
        loc = []
        with open(file1, 'r', newline='') as file:
            reader = csv.DictReader(file)
            loc = [[read['x'], read['y']] for read in reader]
        logger.info("Police locations retrieved.")
        return loc
    except Exception as e:
        logger.error(f"Error retrieving police locations: {e}")
        raise
 
def add():
    try:
        with open(file1, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            temp_l = [input(f"Enter {field}: ") for field in fieldnames]
            writer.writerow(dict(zip(fieldnames, temp_l)))
        logger.info("New police station added.")
    except Exception as e:
        logger.error(f"Error adding new police data: {e}")
        raise
 
def nearest_police(patient_location_x, patient_location_y):
    try:
        police_loc = get_location()
        distances = [distance(float(i[0]), float(i[1]), patient_location_x, patient_location_y) for i in police_loc]
        nearest_index = distances.index(min(distances))
        logger.info(f"Nearest police station found at index: {nearest_index}")
        return get_police_email(nearest_index)
    except Exception as e:
        logger.error(f"Error finding nearest police station: {e}")
        raise
 
def get_police_email(index):
    try:
        with open(file1, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for idx, row in enumerate(reader):
                if idx == index:
                    logger.info(f"Police email found: {row['Mail']}")
                    return row['Mail']
    except Exception as e:
        logger.error(f"Error retrieving police email: {e}")
        raise
 
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)