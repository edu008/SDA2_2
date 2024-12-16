class Plugin:
    def __init__(self):
        self.options_required = True  # Zeigt an, dass Optionen benötigt werden

    def process(self, text: str, option: str) -> str:
        if option == "Uppercase":
            return text.upper()
        elif option == "Lowercase":
            return text.lower()
        elif option == "Capitalize Each Word":
            return text.title()
        else:
            return "Invalid option selected."
