# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from function import find_resource, find_city
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher




class ActionPincodeApi(Action):

    def name(self) -> Text:
        return "action_pincode_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pincode = tracker.latest_message['text']

        city = find_city(pincode)

        dispatcher.utter_template("utter_city", tracker,city = city)

        return []

class ActionResourceApi(Action):

    def name(self) -> Text:
        return "action_resource_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resource = tracker.latest_message['text']

        message_list = []

        for event in tracker.events:
            if(event.get("event") == "user"):
                message_list.append("{}".format(event.get("text")))

        pin = message_list[-3]

        city = find_city(pin)
        res = find_resource(city,resource)

        resource_category = res['category']
        resource_city = res['city']
        resource_contact = res['contact']
        resource_description = res['description']
        resource_organisation = res['organisation']
        resource_phone = res['phone']
        resource_state  = res['state']

        dispatcher.utter_template("utter_resource", tracker,resource_category = resource_category, resource_city = resource_city, resource_contact = resource_contact, resource_organisation = resource_organisation, resource_description = resource_description, resource_phone = resource_phone, resource_state = resource_state)

        return []

class ActionResourceandPinApi(Action):

    def name(self) -> Text:
        return "action_resource_pin_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pincode = ""
        Resource = ""

    
        for m in tracker.latest_message['entities']:
            if(m['entity'] == 'pincode'):
                pincode = m['value']

            if(m['entity'] == 'resources'):
                Resource = m['value']

        city = find_city(pincode)

        res = find_resource(city,Resource)

        resource_category = res['category']
        resource_city = res['city']
        resource_contact = res['contact']
        resource_description = res['description']
        resource_organisation = res['organisation']
        resource_phone = res['phone']
        resource_state  = res['state']

        dispatcher.utter_template("utter_resource", tracker,resource_category = resource_category, resource_city = resource_city, resource_contact = resource_contact, resource_organisation = resource_organisation, resource_description = resource_description, resource_phone = resource_phone, resource_state = resource_state)

        return []
