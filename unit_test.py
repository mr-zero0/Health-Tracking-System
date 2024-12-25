import unittest
import hospital
import police
import sensor_task
import server
from client import EmbeddedClient
import os
 
class TestHealthMonitoringSystem(unittest.TestCase):  
    def test_01_hospital_csv_creation(self):
        hospital.initiate()
        self.assertTrue(os.path.exists("hospital.csv"), "Hospital CSV file was not created.")
 
    def test_02_police_csv_creation(self):
        police.initiate()
        self.assertTrue(os.path.exists("police.csv"), "Police CSV file was not created.")
 
    def test_03_patient_data_csv_creation(self):
        sensor = sensor_task.SensorTask()
        sensor.initialize_csv()
        self.assertTrue(os.path.exists("patient_data.csv"), "Patient data CSV file was not created.")
 
    def test_04_alert_sending(self):
        client1 = EmbeddedClient(sender_email='Sender_mail@mail.com', app_password='**** **** **** ****')
        self.assertIsNone(client1.send_alert('Name', 'x=23 y=54', 'BP=48 HR=90',
                                           'mail@mail.com', 'mail@mail.com', 'mail@mail.com'),
                        "Alert sending failed.")
 
    def test_05_anomaly_detection(self):
        server1 = server.EmbeddedServer()
        self.assertTrue(server1.is_anomalous(85, 55), "Anomaly detection failed.")
 
    def test_06_nearest_police_station(self):
        self.assertEqual(police.nearest_police(10, 10), 'mail@mail.com', "Nearest police station calculation failed.")
 
    def test_07_nearest_hospital(self):
        self.assertEqual(hospital.nearest_hospital(10.0, 10), 'mail@mail.com', "Nearest hospital calculation failed.")
 
    #Negative Test Cases
    def test_08_hospital_csv_creation(self):
        hospital.initiate()
        self.assertFalse(not os.path.exists("hospital.csv"), "Hospital CSV file was not created.")
 
    def test_09_police_csv_creation(self):
        police.initiate()
        self.assertFalse(os.path.exists("police2.csv"), "Police CSV file was not created.")
 
    def test_10_patient_data_csv_creation(self):
        sensor = sensor_task.SensorTask()
        sensor.initialize_csv()
        self.assertFalse(os.path.exists("patient.csv"), "Patient data CSV file was not created.")
 
    def test_11_anomaly_detection(self):
        server1 = server.EmbeddedServer()
        self.assertFalse(server1.is_anomalous(100, 80), "Anomaly detection failed.")
 
    def test_12_nearest_police_station(self):
        self.assertNotEqual(police.nearest_police(-44.5, -60), 'mail@mail.com', "Nearest police station calculation failed.")
 
    def test_13_nearest_hospital(self):
        self.assertNotEqual(hospital.nearest_hospital(-42, 50.2), 'mail@mail.com', "Nearest hospital calculation failed.")
 
    #Failed Cases
    def test_14_alert_sending_false_case(self):
        client1 = EmbeddedClient(sender_email='Sender_mail@mail.com', app_password='**** **** **** ****')
        self.assertIsNotNone(client1.send_alert('Name', 'x=23 y=54', 'BP=48 HR=90',
                                           'mail@mail.com', 'mail@mail.com', 'mail@mail.com'),
                        "Alert sending failed.")
    def test_15_nearest_hospital_false_case(self):
        self.assertEqual(hospital.nearest_hospital(-900, 10), 'mail@mail.com', "Nearest hospital false case failed.")
   
    #Error Case
    def test_16_nearest_hospital_error_case(self):
        self.assertNotEqual(hospital.nearest_hospital('asdf', 50.2), 'mail@mail.com', "Nearest hospital calculation failed.")
 
 
    #Tester Case
    def test_17_nearest_hospital(self):
        self.assertNotEqual(hospital.nearest_hospital(-42, 50.2), 'mail@mail.com', "Nearest hospital calculation failed.")
 
if __name__ == '__main__':
    # Run the tests and log results to a file
    with open('test_result.txt', 'w') as result_file:
        runner = unittest.TextTestRunner(stream=result_file, verbosity=2)
        unittest.main(testRunner=runner, exit=False)