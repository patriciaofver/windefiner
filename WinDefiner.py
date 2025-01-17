import json
import os
import keyboard

class WinDefiner:
    def __init__(self, save_file='definitions.json'):
        self.save_file = save_file
        self.definitions = self.load_definitions()

    def load_definitions(self):
        if os.path.exists(self.save_file):
            with open(self.save_file, 'r') as f:
                return json.load(f)
        return {}

    def save_definitions(self):
        with open(self.save_file, 'w') as f:
            json.dump(self.definitions, f, indent=4)

    def add_definition(self, shortcut, replacement):
        self.definitions[shortcut] = replacement
        self.save_definitions()
        print(f"Added: '{shortcut}' as '{replacement}'")

    def remove_definition(self, shortcut):
        if shortcut in self.definitions:
            del self.definitions[shortcut]
            self.save_definitions()
            print(f"Removed: '{shortcut}'")
        else:
            print(f"Shortcut '{shortcut}' not found.")

    def replace_text(self, event):
        if event.name in self.definitions:
            keyboard.write(self.definitions[event.name])
            keyboard.press_and_release('backspace' * len(event.name))

    def start_listening(self):
        for shortcut in self.definitions:
            keyboard.add_word_listener(shortcut, self.replace_text, triggers=['space', 'enter'])
        print("Listening for shortcuts... Press ESC to stop.")
        keyboard.wait('esc')

if __name__ == "__main__":
    print("Welcome to WinDefiner!")
    wd = WinDefiner()

    while True:
        print("\nOptions:")
        print("1. Add a new definition")
        print("2. Remove a definition")
        print("3. Start listening for shortcuts")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            shortcut = input("Enter the shortcut: ")
            replacement = input("Enter the replacement text: ")
            wd.add_definition(shortcut, replacement)
        elif choice == '2':
            shortcut = input("Enter the shortcut to remove: ")
            wd.remove_definition(shortcut)
        elif choice == '3':
            wd.start_listening()
        elif choice == '4':
            print("Exiting WinDefiner. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")