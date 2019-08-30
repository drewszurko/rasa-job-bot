from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import random


class ActionCheckStatus(Action):

    def name(self):
        return "action_check_status"

    def run(self, dispatcher, tracker, domain):
        # return a random status, just a mockup
        statuses = ["received", "rejected", "interview", "unknown"]
        status = random.choice(statuses)
        return [SlotSet("status", status)]


class ActionCheckPositions(Action):

    def name(self):
        return "action_check_positions"

    def run(self, dispatcher, tracker, domain):
        # return hard-coded open positions, this would normally come from an API
        positions = {
            "technical": [
                "ML Engineer",
                "Solutions Engineer"
            ],
            "business": []
        }

        position_type = tracker.get_slot("role_type")
        if position_type == "any":
            relevant_positions = positions["technical"] + positions["business"]
        else:
            relevant_positions = positions.get(position_type, [])

        if not relevant_positions:
            description = f"There are currently no open {position_type} positions at Rasa."
        else:
            position_str = " and ".join([p for p in relevant_positions])
            description = f"{position_str} are the open positions."

        dispatcher.utter_message(description)
        return [SlotSet("positions", relevant_positions)]
