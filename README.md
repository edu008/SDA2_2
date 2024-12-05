
# Textprozessor mit Plugins

Dies ist eine Textverarbeitungsanwendung, die mit Python und Tkinter entwickelt wurde. Sie unterstützt Plugins für Verschlüsselung, Entschlüsselung und andere Textverarbeitungsfunktionen. Die Anwendung ermöglicht es Benutzern, eine Textdatei auszuwählen, ein Plugin anzuwenden und das verarbeitete Ergebnis anzuzeigen oder zu speichern.

## Funktionen

- Wählen Sie eine Textdatei aus, die verarbeitet werden soll.
- Wählen Sie ein Plugin aus (z. B. Verschlüsselung, Entschlüsselung).
- Geben Sie zusätzliche Eingaben wie Schlüssel ein, falls vom Plugin erforderlich.
- Zeigen Sie den verarbeiteten Text in der Benutzeroberfläche an.
- Speichern Sie das verarbeitete Ergebnis in einer Datei.
- Für Verschlüsselungs-Plugins wird der Schlüssel in einem separaten Fenster angezeigt und kann in die Zwischenablage kopiert werden.

## Voraussetzungen

- Python 3.x
- Benötigte Python-Bibliotheken:
  - `tkinter` (Standardbibliothek)
  - `cryptography` (für Plugins wie Verschlüsselung/Entschlüsselung)

## Installation der Anforderungen

Stellen Sie sicher, dass Sie die benötigten Python-Bibliotheken installieren. Dies kann über die Datei `requirements.txt` erfolgen. Installieren Sie die Anforderungen mit folgendem Befehl:

```bash
pip install -r requirements.txt
```

Inhalt der `requirements.txt`:

```plaintext
cryptography
```

## So starten Sie die Anwendung

1. Klonen oder laden Sie das Repository herunter.
2. Stellen Sie sicher, dass Python auf Ihrem System installiert ist.
3. Installieren Sie die Anforderungen wie oben beschrieben.
4. Starten Sie die Anwendung:

   ```bash
   python main.py
   ```

## Nutzung

1. **Datei auswählen**: Klicken Sie auf "Select File" und wählen Sie die Textdatei aus, die Sie verarbeiten möchten.
2. **Plugin auswählen**: Wählen Sie ein Plugin aus der Dropdown-Liste aus.
3. **Zusätzliche Eingaben**:
   - Wenn ein Plugin zusätzliche Eingaben benötigt (z. B. einen Schlüssel für die Verschlüsselung), geben Sie diese im angezeigten Eingabefeld ein.
4. **Text verarbeiten**: Klicken Sie auf "Process Text", um das Plugin anzuwenden und das Ergebnis anzuzeigen.
5. **Ergebnis speichern**: Klicken Sie auf "Save Output", um den verarbeiteten Text in einer Datei zu speichern.

### Verschlüsselungsschlüssel-Fenster

Für Verschlüsselungs-Plugins (wie `enigma`):
- Nach der Verarbeitung wird ein neues Fenster geöffnet, das den generierten Verschlüsselungsschlüssel anzeigt.
- Der Schlüssel kann mit der Schaltfläche "Copy Key" in die Zwischenablage kopiert werden.

## Plugins

Plugins werden im Ordner `plugins` gespeichert. Sie können neue Plugins hinzufügen, indem Sie eine Klasse mit einer `process`-Methode implementieren. Beispiel:

```python
class Plugin:
    def process(self, text: str, key: str = None) -> str:
        # Text hier verarbeiten
        return processed_text
```

## Beispiel-Plugins

- **Enigma Plugin**: Verschlüsselt den Text und zeigt den Verschlüsselungsschlüssel an.
- **Turing Plugin**: Entschlüsselt Text mit einem angegebenen Schlüssel.

