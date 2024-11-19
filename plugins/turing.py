# plugins/decrypt_text.py
from cryptography.fernet import Fernet

class Plugin:
    def process(self, text: str) -> str:
        key = input("Enter the encryption key: ").encode()
        fernet = Fernet(key)
        
        try:
            decrypted_text = fernet.decrypt(text.encode()).decode()
            return decrypted_text
        except Exception as e:
            return f"Decryption failed: {str(e)}"
