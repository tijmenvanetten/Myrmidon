[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

# Myrmidon

The Myrmidon Bot product designed for the InStepHacks 2021 Hackathon!

## Installation
Create a virtual environment and install the depencies listed in the requirements.txt file as follows:

```bash
virtualenv venv/
source venv/bin/activate
pip install -r requirements.txt
```

## Running
Instantiate locally installed bots by running 

```python 
python external/run.py
```

Then, instantiate the Hub bot by running the following commands

```bash
cd MyrmidonBot/
rasa run
```

## How does it work?
The MyrmidonBot works by fully leveraging the capabilities of the Rasa Open Source framework.

By specifying custom actions that instantiate different models through their API when triggered, we channel the conversation through purpose-specifically trained chatbots.

In this example, two external bots are connected to the main Hub called AppointmentBot and DiagnosisBot. As their names suggest, they are trained for the purpose of scheduling an appointment and helping to diagnose the patient respectively. 

