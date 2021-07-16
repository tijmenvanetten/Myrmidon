[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

# Myrmidon

Introducing Myrmidon! 
A modular approach to combining healthcare chatbot services to provide a seemless experience to the patient. Our submission to the Infosys InStepHacks2021 Hackathon.

## Installation and Running
Create a virtual environment and install the depencies listed in the requirements.txt file as follows:

```bash
virtualenv venv/
source venv/bin/activate
pip install -r requirements.txt
```

Instantiate locally installed bots by running 

```python 
python external/run.py
```

Instantiate the Hub bot by running the following commands

```bash
cd MyrmidonBot/
rasa run actions
rasa shell
```

This will open an interactive shell that allows you to communicate with the MyrmidonBot. When the MyrmidonBot feels like you need to be connected to a different bot, it will take your messages from there and handle the connections with other servers to keep the conversation going. As a result, the user will have a seamless experience but still leveraging various different sources of chatbots.

## How does it work?
The MyrmidonBot works by fully leveraging the capabilities of the Rasa Open Source framework.

By specifying custom actions that instantiate different models through their API when triggered, we channel the conversation to purpose-specifically trained chatbots when necessary.

In this example, two external bots are connected to the main Hub called AppointmentBot and DiagnosisBot. As their names suggest, they are trained for the purpose of scheduling an appointment and helping to diagnose the patient respectively. 

### Examples
```code
--> Hi, how can I help you today?  
I have some symptoms and would like to analyse them.

--> Could you share some details about the symptoms you are currently experiencing?  
My skin is dry and I have a rash on my elbows. 

--> Upon initial diagnosis, it seems like you might have a case of mild eczema. Would you like to know more about this condition or consult a doctor?  
Tell me more.

--> Eczema is a condition wherein patches of skin become inflamed, itchy, cracked, and rough. Some types can also cause blisters.   
I want to consult a doctor.

--> Sure. Please book an appointment with your doctor from the following time slots: 10AM, 11AM, 12PM, 1PM.  
1PM

--> Perfect. We have booked an appointment with dr. Chandrasekharan, at 1PM.  
```
## Myrmidon Team Members:
  * Philippos Giavridis
  * Vitor Aronis
  * Gabriela Do Prado
  * Salman Shahiwala
  * Tijmen van Etten
