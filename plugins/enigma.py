# plugins/encrypt_text.py
from cryptography.fernet import Fernet

class Plugin:
    def process(self, text: str) -> str:
        key = Fernet.generate_key()
        fernet = Fernet(key)
        
        encrypted_text = fernet.encrypt(text.encode()).decode()
        print(f"Encryption Key (save this to decrypt later): {key.decode()}")
        
        return encrypted_text
1