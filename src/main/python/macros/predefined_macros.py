import time

class MacroRunner:
    def __init__(self):
        self.macros = {}

    def add_macro(self, name, actions):
        self.macros[name] = actions

    def run_macro(self, name):
        if name not in self.macros:
            return f"Macro '{name}' not found."
        actions = self.macros[name]
        for action in actions:
            action_type = action.get("type")
            if action_type == "print":
                self._print_action(action.get("message"))
            elif action_type == "wait":
                self._wait_action(action.get("seconds"))
            # Add more actions as needed
        return f"Macro '{name}' executed successfully."

    def _print_action(self, message):
        print(message)

    def _wait_action(self, seconds):
        time.sleep(seconds)

# Example predefined macros
def predefined_macros():
    return {
        "example_macro": [
            {"type": "print", "message": "Starting macro..."},
            {"type": "wait", "seconds": 2},
            {"type": "print", "message": "Macro finished."}
        ]
    }
