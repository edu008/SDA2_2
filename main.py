# main.py
from core.core import Core

def main():
    core = Core()
    
    # Plugins laden
    plugins_loaded = core.load_plugins()
    if not plugins_loaded:
        return  # Programm stoppen, wenn keine Plugins verfügbar sind

    print("Available Plugins:")
    plugins = core.list_plugins()
    for i, plugin in enumerate(plugins, start=1):
        print(f"{i}. {plugin}")

    input_file = input("Enter the input file path: ")
    output_file = input("Enter the output file path: ")

    choice = int(input("Select a plugin by number: "))
    if 1 <= choice <= len(plugins):
        core.process_text(input_file, output_file, plugins[choice - 1])
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
