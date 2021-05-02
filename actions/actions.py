# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class reservationform(FormAction):

    def name(self) -> Text:
        return "reservation_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
         required_slots = ["seatcount", "section", "time"]

         for slot_name in required_slots:
             if tracker.slots.get(slot_name) is None:
                 return [SlotSet("requested_slot", slot_name)]
                 
         return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
 def name(self)  -> Text:
     return "action_submit"

 def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict"
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("Thanks, great job!")
        return []
