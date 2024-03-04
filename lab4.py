import tkinter as tk  # Импортируем модуль tkinter под псевдонимом tk
from threading import Thread  # Импортируем класс Thread из модуля threading
import keyboard  # Импортируем модуль keyboard


class VirtualKeyboard:
    def __init__(self, root):
        self.root = root  # Инициализируем главное окно
        self.root.title("Virtual Keyboard")  # Устанавливаем заголовок окна
        self.text = tk.StringVar()  # Создаем переменную для отображения текста
        self.text.set("")  # Устанавливаем начальное значение текста
        self.key_mapping = {'Q': 'A', 'A': 'Q'}  # Определяем отображение клавиш
        self.text_entry = tk.Entry(root, textvariable=self.text)  # Создаем виджет для ввода текста
        self.text_entry.pack()  # Размещаем виджет на окне
        self.button_frame = tk.Frame(root)  # Создаем фрейм для кнопок
        self.button_frame.pack()  # Размещаем фрейм на окне
        self.create_keyboard_buttons()  # Создаем кнопки клавиатуры
        self.undo_button = tk.Button(root, text="Отменить", command=self.undo_action)  # Создаем кнопку для отмены действия
        self.undo_button.pack()  # Размещаем кнопку на окне
        self.history = []  # Инициализируем список для хранения истории нажатых клавиш
        self.pending_1 = False  # Переменная для отслеживания состояния ожидания ввода символа '1'
        self.keyboard_thread = Thread(target=self.listen_keyboard)  # Создаем поток для отслеживания клавиатуры
        self.keyboard_thread.daemon = True  # Устанавливаем поток как демонический  это поток, который выполняется в фоновом режиме и завершается, когда завершается основной поток программы.
        self.keyboard_thread.start()  # Запускаем поток

    def listen_keyboard(self):
        # Отслеживаем нажатия клавиш клавиатуры
        while True:
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_DOWN:
                self.add_character(event.name)
            elif event.event_type == keyboard.KEY_UP:
                self.undo_action()
    def create_keyboard_buttons(self):
        # Создаем кнопки клавиатуры согласно раскладке
        keyboard_layout = ['1234567890', 'QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
        for row in keyboard_layout:
            row_frame = tk.Frame(self.button_frame)  # Создаем фрейм для строки кнопок
            row_frame.pack()  # Размещаем фрейм на окне
            for char in row:
                  # Создаем экземпляр класса Key с командой LaunchBrowserCommand
                button = tk.Button(row_frame, text=char, command=lambda c=char: self.add_character(c))  # Создаем кнопку
                button.pack(side=tk.LEFT)  # Размещаем кнопку на фрейме

    def add_character(self, char): # char это клавиша
        if self.pending_1:
            if char == '2':
                self.text.set(self.text.get() + 'B')
                self.pending_1 = False
                self.history.append(char)
            elif char == '1':
                self.text.set(self.text.get() + '1' + char)
                self.pending_1 = False
                self.history.append('&')
            else:
                self.text.set(self.text.get() + char)
                self.pending_1 = False
                self.history.append(char)


        else:
            if char == '1':
                self.pending_1 = True
            mapped_char = self.key_mapping.get(char, char)
            self.text.set(self.text.get() + mapped_char)
            self.history.append(char)

    def undo_action(self):
        if self.history:
            current_text = self.text.get()
            counter = self.history.count('1')
            last_char = self.history.pop()
            if last_char == '&':
                self.text.set(current_text[:-2])
                self.pending_1 = False
            else:
                self.text.set(current_text[:-1])
                self.pending_1 = False

    def run(self):
        # Запускаем главное окно
        self.root.mainloop()


def simulate_typing(keyboard, text_to_type):
    # Симулируем нажатие клавиш клавиатуры для ввода текста
    for char in text_to_type:
        keyboard.add_character(char)

if __name__ == "__main__":
    root = tk.Tk()  # Создаем главное окно
    keyboard_app = VirtualKeyboard(root)  # Создаем экземпляр виртуальной клавиатуры
    simulation_thread = Thread(target=simulate_typing, args=(keyboard_app, "Hello!"))  # Создаем поток для симуляции ввода текста
    simulation_thread.start()  # Запускаем поток симуляции
    keyboard_app.run()  # Запускаем приложение виртуальной клавиатуры
