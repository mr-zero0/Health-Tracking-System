 
import logging
import os
from datetime import datetime
 
try:
    # Define base directory and create the required folder structure
    base_log_dir = 'Logs'
    date_str = datetime.now().strftime('%d_%m_%Y')
    run_number = 1
 
    # Check for existing run directories and increment the run number
    while os.path.exists(f"{base_log_dir}/{date_str}/Run{run_number}"):
        run_number += 1
 
    # Create the new run folder
    run_dir = f"{base_log_dir}/{date_str}/Run{run_number}"
    os.makedirs(run_dir, exist_ok=True)
 
    # Configure logging with the new path
    log_file_path = os.path.join(run_dir, 'Monitoring.log')
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
 
    # Create the logger instance
    logger = logging.getLogger("HealthSense")
    logger.info("Logging initialized successfully.")
except Exception as e:
    print(f"An error occurred while setting up the log directory or file: {e}")
    # Log the error in a fallback location if necessary (this is entirely optional, but is a good practice)
    logging.basicConfig(
        filename='Logs/error_log.log',
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger("HealthSense")
    logger.error(f"Error setting up logging: {e}")
finally:
    # Any cleanup code can be added here if needed
    print("Logging setup process completed.")
 