# logging_config.py
import logging
import os

# Creează un director pentru log-uri dacă nu există
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configurarea de bază pentru logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

# Funcție pentru a obține un logger
def get_logger(name):
    return logging.getLogger(name)
