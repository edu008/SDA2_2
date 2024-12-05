from cryptography.fernet import Fernet

class Plugin:
    def process(self, text: str, encryption_key: str = None) -> str:
        if not encryption_key:
            encryption_key = Fernet.generate_key().decode()  # Generiere Schlüssel, wenn keiner angegeben wurde
        else:
            encryption_key = encryption_key.encode()
        fernet = Fernet(encryption_key)
        encrypted_text = fernet.encrypt(text.encode()).decode()
        
        print(f"Encryption Key (save this to decrypt later): {encryption_key}")  # Für Debugging im Terminal
        return encrypted_text, encryption_key  # Rückgabe des verschlüsselten Texts und des Schlüssels
