import tkinter as tk
from tkinter import filedialog, messagebox
from core.core import Core

class TextProcessorApp:
    def __init__(self, root):
        self.core = Core()
        plugins_loaded = self.core.load_plugins()
        if not plugins_loaded:
            messagebox.showerror("Error", "No plugins found. Please add plugins to the 'plugins' folder.")
            root.destroy()
            return

        self.root = root
        self.root.title("Text Processor")

        self.label = tk.Label(root, text="Text Processor with Plugins", font=("Arial", 16))
        self.label.pack(pady=10)

        self.file_label = tk.Label(root, text="No file selected")
        self.file_label.pack(pady=5)

        self.select_file_btn = tk.Button(root, text="Select File", command=self.select_file)
        self.select_file_btn.pack(pady=5)

        self.plugin_label = tk.Label(root, text="Select a Plugin:")
        self.plugin_label.pack(pady=5)

        self.plugin_var = tk.StringVar()
        self.plugin_var.set("None")
        self.plugin_menu = tk.OptionMenu(root, self.plugin_var, *self.core.list_plugins())
        self.plugin_menu.pack(pady=5)

        self.extra_input_label = tk.Label(root, text="", font=("Arial", 10))
        self.extra_input_label.pack(pady=5)
        self.extra_input_entry = tk.Entry(root)
        self.extra_input_entry.pack(pady=5)
        self.extra_input_label.pack_forget()
        self.extra_input_entry.pack_forget()

        self.process_btn = tk.Button(root, text="Process Text", command=self.process_text)
        self.process_btn.pack(pady=10)

        self.text_output = tk.Text(root, height=10, width=50)
        self.text_output.pack(pady=10)

        self.save_btn = tk.Button(root, text="Save Output", command=self.save_output)
        self.save_btn.pack(pady=5)

        self.file_path = None
        self.processed_text = None

        # Track current plugin to update UI dynamically
        self.plugin_var.trace("w", self.update_extra_input)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.file_path = file_path
            self.file_label.config(text=f"Selected: {file_path}")
        else:
            self.file_label.config(text="No file selected")

    def update_extra_input(self, *args):
    # --- UI zurücksetzen ---
    # Entferne zusätzliche Eingaben
        self.extra_input_label.pack_forget()
        self.extra_input_label.config(text="")
        self.extra_input_entry.delete(0, tk.END)  # Löscht den Inhalt des Eingabefeldes
        self.extra_input_entry.pack_forget()

    # Lösche Optionen (Dropdown-Menü), falls vorhanden
        if hasattr(self, "extra_input_menu"):
            self.extra_input_menu.pack_forget()
            del self.extra_input_menu

    # Lösche Textausgabe und verarbeitete Daten
        self.text_output.delete(1.0, tk.END)  # Löscht den Inhalt der Textbox
        self.processed_text = None  # Verarbeitete Daten zurücksetzen

    # --- Plugin-spezifische UI anzeigen ---
        plugin_name = self.plugin_var.get()
        if plugin_name in self.core.plugins:
            plugin = self.core.plugins[plugin_name]

        # Zusätzliche Eingabe für Suchwörter
            if getattr(plugin, "text_input_required", False):
                self.extra_input_label.config(text="Enter search word:")
                self.extra_input_label.pack(after=self.process_btn, pady=5)
                self.extra_input_entry.pack(after=self.extra_input_label, pady=5)

        # Zusätzliche Eingabe für Schlüssel
            elif getattr(plugin, "key_required", False):
                self.extra_input_label.config(text="Enter Key:")
                self.extra_input_label.pack(after=self.process_btn, pady=5)
                self.extra_input_entry.pack(after=self.extra_input_label, pady=5)

        # Dropdown-Menü für Optionen
            elif getattr(plugin, "options_required", False):
                self.extra_input_label.config(text="Choose Option:")
                self.extra_input_label.pack(after=self.process_btn, pady=5)

                self.option_var = tk.StringVar(self.root)
                self.option_var.set("Select Option")
                options = ["Uppercase", "Lowercase", "Capitalize Each Word"]
                self.extra_input_menu = tk.OptionMenu(self.root, self.option_var, *options)
                self.extra_input_menu.pack(after=self.extra_input_label, pady=5)


            
        else:
        # Entferne alle UI-Elemente, falls kein Plugin ausgewählt ist
                self.extra_input_label.config(text="")
                self.extra_input_label.pack_forget()
                if hasattr(self, "extra_input_entry"):
                    self.extra_input_entry.pack_forget()
                if hasattr(self, "extra_input_menu"):
                    self.extra_input_menu.pack_forget()

    def process_text(self):
            if not self.file_path:
                messagebox.showerror("Error", "No file selected.")
                return

            plugin_name = self.plugin_var.get()
            if plugin_name == "None":
                messagebox.showerror("Error", "No plugin selected.")
                return

            try:
                with open(self.file_path, "r") as file:
                    text = file.read()

                plugin = self.core.plugins[plugin_name]
                extra_input = None

                # Zusätzliche Eingaben je nach Plugin-Typ validieren
                if getattr(plugin, "key_required", False):
                    if hasattr(self, "extra_input_entry"):
                        extra_input = self.extra_input_entry.get()
                    if not extra_input:
                        messagebox.showerror("Error", "No key provided.")
                        return
                elif getattr(plugin, "options_required", False):
                    if hasattr(self, "option_var"):
                        extra_input = self.option_var.get()
                    if extra_input == "Select Option":
                        messagebox.showerror("Error", "No option selected.")
                        return
                elif getattr(plugin, "text_input_required", False):
                    if hasattr(self, "extra_input_entry"):
                        extra_input = self.extra_input_entry.get()
                    if not extra_input:
                        messagebox.showerror("Error", "No search word provided.")
                        return

        # Verarbeite den Text je nach Plugin-Typ
                if plugin_name == "enigma":
                    result = plugin.process(text)
                    if isinstance(result, tuple) and len(result) == 2:
                        encrypted_text, encryption_key = result

                # Zeige Schlüssel in einem Pop-up-Fenster
                        self.show_key_window(encryption_key)

                # Speichere verschlüsselten Text
                        self.processed_text = encrypted_text
                    else:
                        messagebox.showerror("Error", "Unexpected plugin result format.")
                        return
                else:
                    if extra_input:
                        self.processed_text = plugin.process(text, extra_input)
                    else:
                        if getattr(plugin, "key_required", False):
                            messagebox.showerror("Error", "No key provided. Please enter a key.")
                            return
                        self.processed_text = plugin.process(text)

        # Zeige das Ergebnis in der Textbox an
                self.text_output.delete(1.0, tk.END)
                self.text_output.insert(tk.END, self.processed_text)

            except Exception as e:
                messagebox.showerror("Error", f"Processing failed: {str(e)}")
    

    def show_key_window(self, encryption_key):
        # Erstelle ein Pop-up-Fenster
        key_window = tk.Toplevel(self.root)
        key_window.title("Encryption Key")
        key_window.geometry("400x200")

        tk.Label(key_window, text="Encryption Key (save this to decrypt later):", font=("Arial", 12)).pack(pady=10)

        key_textbox = tk.Text(key_window, height=3, width=50, wrap=tk.WORD)
        key_textbox.insert(1.0, encryption_key)
        key_textbox.pack(pady=10)
        key_textbox.config(state=tk.DISABLED)  # Schreibgeschützt

        def copy_to_clipboard():
            self.root.clipboard_clear()
            self.root.clipboard_append(encryption_key)
            self.root.update()  # Clipboard aktualisieren
            messagebox.showinfo("Copied", "Encryption Key copied to clipboard!")

        copy_btn = tk.Button(key_window, text="Copy Key", command=copy_to_clipboard)
        copy_btn.pack(pady=5)

    def save_output(self):
        if not self.processed_text:
            messagebox.showerror("Error", "No processed text to save.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if save_path:
            with open(save_path, "w") as file:
                file.write(self.processed_text)
            messagebox.showinfo("Success", f"Processed text saved to {save_path}")



if __name__ == "__main__":
    root = tk.Tk()
    app = TextProcessorApp(root)
    root.mainloop()
