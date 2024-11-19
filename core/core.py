# core/core.py
import os
import importlib

class Core:
    def __init__(self):
        self.plugins = {}

    def load_plugins(self, plugin_folder="plugins"):
        plugin_files = [
            filename for filename in os.listdir(plugin_folder)
            if filename.endswith(".py") and filename != "__init__.py"
        ]
        
        if not plugin_files:
            print("No plugins found. Please add plugins to the 'plugins' folder.")
            return False  # Keine Plugins gefunden
        
        for filename in plugin_files:
            plugin_name = filename[:-3]
            module = importlib.import_module(f"{plugin_folder}.{plugin_name}")
            plugin_class = getattr(module, "Plugin")
            self.plugins[plugin_name] = plugin_class()
        
        return True  # Plugins erfolgreich geladen

    def process_text(self, input_file, output_file, plugin_name):
        if plugin_name not in self.plugins:
            print(f"Plugin '{plugin_name}' not found.")
            return

        with open(input_file, "r") as infile:
            text = infile.read()

        processed_text = self.plugins[plugin_name].process(text)

        with open(output_file, "w") as outfile:
            outfile.write(processed_text)
        print(f"Text processed with '{plugin_name}' and saved to '{output_file}'.")

    def list_plugins(self):
        return list(self.plugins.keys())
