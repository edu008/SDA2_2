# plugins/word_counter.py
class Plugin:
    def process(self, text: str) -> str:
        word_count = len(text.split())
        return f"Word Count: {word_count}\nOriginal Text:\n{text}"
