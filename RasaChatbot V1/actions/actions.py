from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet, UserUtteranceReverted, EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ValidateScholarshipForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_scholarship_form"
    
    def validate_country(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `country` value."""
        t=tracker.get_slot("country")
        if not t:
            msg="Please enter a correct country name"
            dispatcher.utter_message(text = msg)
            return {"country":None}
        msg="OK!"
        dispatcher.utter_message(text = msg)
        return {"country":t}

    def validate_finance(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `finance` value."""
        t=tracker.get_slot("finance")
        if not t:
            msg="Please enter a valid finance method"
            dispatcher.utter_message(text = msg)
            return {"finance":None}
        msg="OK!"
        dispatcher.utter_message(text = msg)
        return {"finance":t}

class ActionGetLinkSS(Action):

    def name(self) -> Text:
        return "action_get_link"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text,Any]) -> List[Dict[Text, Any]]:
        Link="localhost/home"
        dispatcher.utter_message(response="utter_link_ss",link=Link)
        return[]
