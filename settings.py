"""
Settings for the main hub Bot.
"""

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# Rasa SDK Action server
SANIC_HOST='127.0.0.1:5505'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_BOTSs = [
    {
        'name': 'DiagnosisBot',
        'host': '127.0.0.1', 
        'port': '5005', 
    },
    {
        'name': 'AppointmentBot',
        'host': '127.0.0.1', 
        'port': '5006', 
    }
]