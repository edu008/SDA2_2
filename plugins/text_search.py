# plugins/text_search.py
class Plugin:
    def __init__(self):
        self.key_required = False
        self.options_required = False
        self.text_input_required = True  # Zeigt an, dass ein Textinput nötig ist

    def process(self, text: str, search_word: str = None) -> str:
        if not search_word:
            return "Error: No search word provided."
        
        occurrences = text.count(search_word)
        return f"The word '{search_word}' was found {occurrences} times in the text.\nOriginal Text:\n{text}"
