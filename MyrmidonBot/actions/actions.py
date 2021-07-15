# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import requests
import json


class RequestDiagnosis(Action):

    def name(self) -> Text:
        return "process_diagnosis"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        context = {  
            "sender": "test_user",  
            "message": tracker.current_state()['latest_message'],
        }

        url = 'http://127.0.0.1:5006/webhooks/rest/webhook'

        response = requests.post(url, data=json.dumps(context)).text
        response = "DiagnosisBot: " + response

        dispatcher.utter_message(response = "give_diagnosis", text = response)

        return []

class ScheduleAppointment(Action):

    def name(self) -> Text:
        return "process_appointment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = 'http://127.0.0.1:5007/webhooks/rest/webhook'

        context = {  
            "sender": "test_user",  
            "message": tracker.current_state()['latest_message']
        }

        response = requests.post(url, data=json.dumps(context)).text
        response = "AppointmentBot: " + response

        dispatcher.utter_message(response = "give_appointment", text = response)

        return []

