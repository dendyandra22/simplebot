# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict

class ValidateServiceForm(FormValidationAction):
    def name(self)-> Text:
        return "validate_service_form"

    def validate_service(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict)-> Dict[Text, Any]:
        '''Validate service values'''
        # if tracker.get_intent_of_latest_message != "give_information":
        #     dispatcher.utter_message

        if slot_value.lower() not in ['livebot', 'nabot']:
            dispatcher.utter_message(text="Service name is invalid! We only offer LiveBot and NaBot")
            return {'service':None}

        return {'service':slot_value}
    

    def validate_payment(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict)-> Dict[Text, Any]:
        '''Validate payment values'''
        # if tracker.get_intent_of_latest_message != "give_information":
        #     dispatcher.utter_message

        if slot_value.lower() not in ['debit card', 'credit card', 'bitcoin', 'debit', 'credit']:
            dispatcher.utter_message(text="Payment method is invalid! We only accept Debit card, Credit card, and Bitcoin")
            return {'payment':None}

        return {'payment':slot_value}


        