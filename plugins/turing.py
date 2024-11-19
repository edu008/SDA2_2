# plugins/decrypt_text.py
from cryptography.fernet import Fernet

class Plugin:
    def __init__(self):
        self.key_required = True  # Zeigt der UI, dass ein Key gebraucht wird

    def process(self, text: str, key: str = None) -> str:
        if not key:
            return "Decryption failed: No key provided."
        
        try:
            fernet = Fernet(key.encode())
            decrypted_text = fernet.decrypt(text.encode()).decode()
            return decrypted_text
        except Exception as e:
            return f"Decryption failed: {str(e)}"
