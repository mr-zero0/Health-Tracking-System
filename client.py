import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from setup_logging import logger
 
class EmbeddedClient:
    def __init__(self, sender_email, app_password):
        self.sender_email = 'Sender_mail'
        self.app_password = '**** **** **** ****'
 
    def send_alert(self, patient_name, patient_location, anomaly, hospital_email, police_email, family_email):
        try:
            # Hospital alert message format
            general_subject = f"Hospital Alert: Health Emergency Alert for {patient_name}"
            general_body = (f"Dear {hospital_email},\n\n"
                            f"Patient {patient_name} has been detected with an anomaly at location {patient_location}.\n"
                            f"Anomaly: {anomaly}\n\n"
                            f"Please respond immediately to provide necessary medical assistance.\n\n"
                            f"Best regards,\n"
                            f"Health Monitoring System")
 
            # Create and send an email to the hospital
            msg_hospital = MIMEMultipart()
            msg_hospital['From'] = self.sender_email
            msg_hospital['To'] = hospital_email
            msg_hospital['Subject'] = general_subject
            msg_hospital.attach(MIMEText(general_body, 'plain'))
 
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender_email, self.app_password)
                server.send_message(msg_hospital)
            logger.info(f"Alert sent successfully to hospital: {hospital_email}")
 
            # Create a personalized alert for police
            police_subject = f"Police Alert: Urgent Alert: Health Emergency for {patient_name}"
            police_body = (f"Dear {police_email},\n\n"
                           f"There has been an emergency involving patient {patient_name} at location {patient_location}.\n"
                           f"Anomaly Detected: {anomaly}\n\n"
                           f"Please ensure immediate action and coordination with the relevant authorities.\n\n"
                           f"Best regards,\n"
                           f"Health Monitoring System")
 
            msg_police = MIMEMultipart()
            msg_police['From'] = self.sender_email
            msg_police['To'] = police_email
            msg_police['Subject'] = police_subject
            msg_police.attach(MIMEText(police_body, 'plain'))
 
            # Send the email to the police
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender_email, self.app_password)
                server.send_message(msg_police)
            logger.info(f"Alert sent successfully to police: {police_email}")
 
            # Create a customized alert for the family
            family_subject = f"Family Alert: Emergency for {patient_name}"
            family_body = (f"Dear Family of {patient_name},\n\n"
                           f"Your loved one, {patient_name}, has been detected with an anomaly at location {patient_location}.\n"
                           f"Anomaly Detected: {anomaly}\n\n"
                           f"We are taking necessary actions to ensure {patient_name}'s safety.\n\n"
                           f"Best regards,\n"
                           f"Health Monitoring System")
 
            msg_family = MIMEMultipart()
            msg_family['From'] = self.sender_email
            msg_family['To'] = family_email
            msg_family['Subject'] = family_subject
            msg_family.attach(MIMEText(family_body, 'plain'))
 
            # Send the email to the family
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender_email, self.app_password)
                server.send_message(msg_family)
            logger.info(f"Alert sent successfully to family: {family_email}")

            #Send email to all
            subject = f"Health Emergency Alert for {patient_name}"
            body = (f"Patient {patient_name} has a health emergency at location {patient_location}.\n"
                    f"Hospital notified: {hospital_email}\n"
                    f"Police notified: {police_email}\n"
                    f"Family notified: {family_email}\n")
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = ', '.join([hospital_email, police_email, family_email])
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
 
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.sender_email, self.app_password)
                server.send_message(msg)
            logger.info(f"Alert sent successfully to hospital, police, and family.")

        except Exception as e:
            logger.error(f"Error sending alert emails: {e}")
            raise
 