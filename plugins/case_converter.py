# plugins/case_converter.py
class Plugin:
    def process(self, text: str) -> str:
        print("1. Uppercase\n2. Lowercase\n3. Capitalize Each Word")
        choice = input("Choose an option: ")
        if choice == "1":
            return text.upper()
        elif choice == "2":
            return text.lower()
        elif choice == "3":
            return text.title()
        else:
            return text
