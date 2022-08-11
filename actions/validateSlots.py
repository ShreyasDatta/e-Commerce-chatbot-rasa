from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateProductInfotForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_products_tags_form"


    def validate_products(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate products role value."""

        if slot_value is not None:
            # validation succeeded, set the value of the "cuisine" slot to value
            print(f"slot_value:{slot_value}")
            return {"products": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            return f"There was no value entered for the products slot. Please input again."