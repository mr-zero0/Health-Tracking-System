**Health Monitoring System**

**Overview**
This project is a real-time health monitoring system that tracks patient data, identifies anomalies, and sends alerts to relevant parties during emergencies. It uses CSV-based data management and integrates email notifications with location details for timely assistance.

**Features**
Real-Time Monitoring: Continuously tracks health parameters like heart rate, blood pressure, SpO2, etc.
Anomaly Detection: Automatically flags critical health issues.
Alert System: Sends emails to family members, hospitals, and police stations with patient details and location information.
Emergency Details: Provides nearby hospital and police station locations for quick response.
Data Logging: Saves alert details in a local alert_received.txt file for demonstration purposes.

**Technical Details**
Input: Data fetched from a CSV file, updated at regular intervals.
Output: Alerts sent via email and logged locally.
Languages: Python.
Environment: No external libraries; designed for portability and efficiency.

**How It Works**
Monitor: Reads and monitors health parameters from the CSV file.
Analyze: Checks for anomalies against predefined thresholds.
Notify: Sends alerts to registered contacts if anomalies are detected.
Escalate: If no response from the user after three alerts, escalates notifications to family and emergency services.
