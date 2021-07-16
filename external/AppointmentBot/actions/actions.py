# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionTimeslot(Action):

    def name(self) -> Text:
        return "action_timeslot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
	
        timeslot = tracker.latest_message["text"]
        message = "Perfect. We have booked an appointment with Dr Tijmen at {}. We will be video-calling you through WhatsApp at this number then.".format(timeslot)
        
        dispatcher.utter_message(text=message)

        return [SlotSet("timeslot", timeslot)]

class ActionRepeat(Action):
    
    def name(self) -> Text:
        return "action_repeat"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("timeslot")
        if not name:
            dispatcher.utter_message(text="You haven't made an appointment yet.")
        else:
            dispatcher.utter_message(text=f"Your appointment is at {timeslot}!")
        return []
