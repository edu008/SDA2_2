# plugins/text_search.py
class Plugin:
    def process(self, text: str) -> str:
        keyword = input("Enter a word to search: ")
        occurrences = text.count(keyword)
        return f"'{keyword}' found {occurrences} times in the text.\nOriginal Text:\n{text}"
