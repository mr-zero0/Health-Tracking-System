import threading
import time
import csv
import logging
from server import EmbeddedServer
from client import EmbeddedClient
from sensor_task import SensorTask
from linked_list import LinkedList
import police
import hospital
 
 
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 
# Initialization
logging.info("Program Execution Begins.")
logging.info("---------------------------------------")
 
# Initialize databases and static data
police.initiate()
hospital.initiate()
 
hospital_list = LinkedList()
police_list = LinkedList()
family_list = LinkedList()
 
hospital_list.insert('City Hospital', 'mail@mail.com', (5, 15))
police_list.insert('City Police', 'mail@mail.com', (12, 25))
family_list.insert('Name', 'mail@mail.com', (0, 0))
 
if __name__ == "__main__":
    sensor_task = SensorTask()
    client = EmbeddedClient(sender_email='Sender_mail@mail.com', app_password='**** **** **** ****')
 
    # Initialize CSV
    sensor_task.initialize_csv()
 
    # Start server in a separate thread
    server = EmbeddedServer()
    server_thread = threading.Thread(target=server.run)
    server_thread.start()
 
    # CSV update thread
    def update_csv_thread():
        while True:
            try:
                sensor_task.update_csv()
                #update_CSV.changeData("patient_data.csv", "id", "001", "bp", 60)
                logging.info("CSV updated successfully.")
                time.sleep(10)  # Adjust interval for updates
            except Exception as e:
                logging.error("Error updating CSV: %s", e)
 
    csv_thread = threading.Thread(target=update_csv_thread)
    csv_thread.daemon = True
    csv_thread.start()
 
    # Alert generation thread
    def alert_generation_thread():
        while True:
            try:
                patient_location = input("Enter patient location (x,y): ")
                x, y = map(float, patient_location.split(','))
                logging.info("Patient location received: (%f, %f)", x, y)
 
                p_email = police.nearest_police(x, y)
                h_email = hospital.nearest_hospital(x, y)
 
                with open(SensorTask.CSV_FILE, mode="r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        bp = int(row['bp'])
                        heartrate = int(row['heartrate'])
                        if server.is_anomalous(bp, heartrate):
                            threading.Thread(
                                target=client.send_alert,
                                args=(row['name'], patient_location, f"BP={bp}, HR={heartrate}", h_email, p_email, family_list.head.email)
                            ).start()
                            logging.info("Alert sent for patient: %s", row['name'])
 
            except ValueError as ve:
                logging.error("Invalid input for patient location: %s", ve)
            except Exception as e:
                logging.error("Error processing patient data: %s", e)
            time.sleep(10)
 
    alert_thread = threading.Thread(target=alert_generation_thread)
    alert_thread.daemon = True
    alert_thread.start()
 
    # Main loop for program termination
    try:
        while True:
            user_input = input("Do you want to continue? (yes/no): ").strip().lower()
            if user_input == 'no':
                logging.info("User opted to stop the program.")
                break
    except Exception as e:
        logging.error("Error in main loop: %s", e)
    finally:
        server.stop()
        server_thread.join()
        logging.info("Server stopped and thread joined.")
    logging.info("Program Execution Ends.")
    logging.info("---------------------------------------")
 