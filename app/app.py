import logging
import time
import random

logging.basicConfig(
    filename='/logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

while True:
    level = random.choice(["INFO","WARNING","ERROR"])

    if level == "INFO":
        logging.info("This is an info message.")
    elif level == "WARNING":
        logging.warning("This is a warning message.")
    else:
        logging.error("This is an error message.")
    time.sleep(5)