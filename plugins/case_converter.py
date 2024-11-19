# plugins/case_converter.py
class Plugin:
    def __init__(self):
        self.options_required = True  # Zeigt der UI, dass eine Auswahl benötigt wird

    def process(self, text: str, option: str = None) -> str:
        if option == "Uppercase":
            return text.upper()
        elif option == "Lowercase":
            return text.lower()
        elif option == "Capitalize Each Word":
            return text.title()
        else:
            return "Invalid option selected."
