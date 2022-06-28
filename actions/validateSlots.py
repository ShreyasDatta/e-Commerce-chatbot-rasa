from typing import Text, Any, Dict

from rasa_sdk import Tracker, ValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

# Need to work on it further. Improve logic
class ValidatePredefinedSlots(ValidationAction):
    def name(self)-> Text:
        return "validate_products"
    
    def validate_products(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate products value."""
        pt = tracker.get_latest_entity_values(entity_type="product")
        
        if isinstance(slot_value, str):
            # validation succeeded, capitalize the value of the "location" slot
            dispatcher.utter_message(text="I'm sorry, Is "(slot_value))
            return {"products": slot_value.capitalize()}
        else:
            # validation failed, set this slot to None
            dispatcher.utter_message(text="Or it, Is "(pt))
            return {"products": pt}