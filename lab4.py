import tkinter as tk
from threading import Thread
import keyboard

class Command:
    def execute(self):
        pass

    def undo(self):
        pass

class LaunchBrowserCommand(Command):
    def execute(self):
        print("Launching browser")

    def undo(self):
        print("Closing browser")

class Key:
    def __init__(self, command):
        self.command = command

    def press(self):
        self.command.execute()

    def release(self):
        self.command.undo()

class VirtualKeyboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Keyboard")
        self.text = tk.StringVar()
        self.text.set("")
        self.key_mapping = {
            'Q': 'A',
            'A': 'Q',
        }
        self.text_entry = tk.Entry(root, textvariable=self.text)
        self.text_entry.pack()
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()
        self.create_keyboard_buttons()
        self.undo_button = tk.Button(root, text="Отменить", command=self.undo_action)
        self.undo_button.pack()
        self.history = []
        self.pending_1 = False
        self.keyboard_thread = Thread(target=self.listen_keyboard)
        self.keyboard_thread.daemon = True
        self.keyboard_thread.start()

    def create_keyboard_buttons(self):
        keyboard_layout = [
            '1234567890',
            'QWERTYUIOP',
            'ASDFGHJKL',
            'ZXCVBNM',
        ]
        for row in keyboard_layout:
            row_frame = tk.Frame(self.button_frame)
            row_frame.pack()
            for char in row:
                command = Key(LaunchBrowserCommand())  # Создаем экземпляр класса Key с командой LaunchBrowserCommand
                button = tk.Button(row_frame, text=char, command=lambda c=char: self.add_character(c))
                button.pack(side=tk.LEFT)

    def add_character(self, char):
        if self.pending_1:
            if char == '2':
                self.text.set(self.text.get() + 'B')
                self.pending_1 = False
            else:
                self.text.set(self.text.get() + '1' + char)
        else:
            if char == '1':
                self.pending_1 = True
            mapped_char = self.key_mapping.get(char, char)
            self.text.set(self.text.get() + mapped_char)
            self.history.append(char)

    def undo_action(self):
        if self.history:
            last_char = self.history.pop()
            if self.pending_1:
                self.pending_1 = False
            current_text = self.text.get()
            if current_text:
                self.text.set(current_text[:-1])

    def run(self):
        self.root.mainloop()

    def listen_keyboard(self):
        while True:
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_DOWN:
                self.add_character(event.name)

def simulate_typing(keyboard, text_to_type):
    for char in text_to_type:
        keyboard.add_character(char)

if __name__ == "__main__":
    root = tk.Tk()
    keyboard_app = VirtualKeyboard(root)
    simulation_thread = Thread(target=simulate_typing, args=(keyboard_app, "Hello, World!"))
    simulation_thread.start()
    keyboard_app.run()
