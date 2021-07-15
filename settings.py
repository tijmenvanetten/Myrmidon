"""
Settings for the main hub Bot.
"""

from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

LOCAL_BOTS = [
    # Local bots
    'appointment_bot',
    'diagnose_bot',
]

EXTERNAL_BOTS = [
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