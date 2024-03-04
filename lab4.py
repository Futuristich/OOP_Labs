import time  # Импорт модуля time для работы с временем

class Keyboard:  # Определение класса Keyboard
    def __init__(self):  # Определение конструктора класса Keyboard
        self.keymap = {}  # Инициализация словаря keymap для хранения действий и их отмены по клавишам
        self.history = []  # Инициализация списка history для отслеживания нажатых клавиш

    def register_key(self, key, action, undo_action):  # Определение метода register_key для регистрации действий и их отмены по клавишам
        self.keymap[key] = (action, undo_action)  # Регистрация действия и его отмены для указанной клавиши

    def press_key(self, key):  # Определение метода press_key для нажатия клавиши
        if key not in self.keymap:  # Проверка наличия клавиши в keymap
            raise Exception("Неизвестная клавиша нажата")  # Возбуждение исключения, если клавиша не найдена
        self.history.append(key)  # Добавление нажатой клавиши в историю
        self.keymap[key][0]()  # Выполнение зарегистрированного действия по нажатой клавише

    def undo(self):  # Определение метода undo для отмены последнего действия
        if self.history:  # Проверка наличия элементов в истории
            last_key = self.history.pop()  # Извлечение последней нажатой клавиши из истории
            if last_key in self.keymap:  # Проверка наличия последней клавиши в keymap
                self.keymap[last_key][1]()  # Отмена последнего действия, связанного с последней нажатой клавишей

    def is_key_registered(self, key):  # Определение метода is_key_registered для проверки регистрации клавиши
        return key in self.keymap  # Возврат True, если клавиша зарегистрирована, и False в противном случае

class Workflow:  # Определение класса Workflow
    def __init__(self, keyboard):  # Определение конструктора класса Workflow
        self.keyboard = keyboard  # Инициализация атрибута keyboard для хранения экземпляра класса Keyboard
        self.actions = []  # Инициализация списка actions для хранения действий рабочего процесса

    def keypress(self, key):  # Определение метода keypress для нажатия клавиши
        self.keyboard.press_key(key)  # Вызов метода press_key экземпляра класса Keyboard
        time.sleep(1)  # Задержка выполнения на 1 секунду

    def undo(self):  # Определение метода undo для отмены последнего действия
        self.keyboard.undo()  # Вызов метода undo экземпляра класса Keyboard
        time.sleep(1)  # Задержка выполнения на 1 секунду

    def perform(self):  # Определение метода perform для выполнения рабочего процесса
        for action in self.actions:  # Итерация по списку actions
            action()  # Выполнение текущего действия
            time.sleep(1)  # Задержка выполнения на 1 секунду

    def add_action(self, action):  # Определение метода add_action для добавления действия в рабочий процесс
        self.actions.append(action)  # Добавление действия в список actions

def main():  # Определение функции main
    keyboard = Keyboard()  # Создание экземпляра класса Keyboard

    keyboard.register_key("A", lambda: print("Клавиша A нажата"), lambda: None)  # Регистрация действия и его отмены для клавиши A

    keyboard.register_key("Ctrl+C", lambda: print("Комбинация Ctrl+C нажата"), lambda: print("Ctrl+C действие отменено"))  # Регистрация действия и его отмены для комбинации клавиш Ctrl+C

    keyboard.register_key("Ctrl+V", lambda: print("Комбинация Ctrl+V нажата"), lambda: print("Ctrl+V действие отменено"))  # Регистрация действия и его отмены для комбинации клавиш Ctrl+V

    keyboard.register_key("F1", lambda: print("Клавиша F1 нажата"), lambda: None)  # Регистрация действия и его отмены для клавиши F1

    keyboard.register_key("F2", lambda: print("Клавиша F2 нажата"), lambda: None)  # Регистрация действия и его отмены для клавиши F2

    workflow = Workflow(keyboard)  # Создание экземпляра класса Workflow

    workflow.add_action(lambda: workflow.keypress("A"))  # Добавление действия нажатия клавиши A в рабочий процесс

    workflow.add_action(lambda: workflow.keypress("Ctrl+C"))  # Добавление действия нажатия комбинации клавиш Ctrl+C в рабочий процесс

    workflow.add_action(lambda: workflow.keypress("Ctrl+V"))  # Добавление действия нажатия комбинации клавиш Ctrl+V в рабочий процесс

    workflow.add_action(lambda: workflow.undo())  # Добавление действия отмены последнего действия в рабочий процесс

    workflow.add_action(lambda: workflow.undo())  # Добавление действия отмены последнего действия в рабочий процесс

    workflow.add_action(lambda: workflow.keypress("F1"))  # Добавление действия нажатия клавиши F1 в рабочий процесс

    workflow.add_action(lambda: workflow.keypress("F2"))  # Добавление действия нажатия клавиши F2 в рабочий процесс

    workflow.perform()  # Выполнение рабочего процесса

    print("\nПереназначение клавиш и перезапуск процесса...")  # Вывод сообщения о переназначении клавиш и перезапуске процесса

    keyboard.register_key("A", lambda: print("Клавиша A теперь ничего не делает"), lambda: None)  # Переназначение действия и его отмены для клавиши A

    keyboard.register_key("Ctrl+C", lambda: print("Комбинация Ctrl+C теперь выводит 87 "), lambda: print("Отмена действия для Ctrl+C"))  # Переназначение действия и его отмены для комбинации клавиш Ctrl+C

    keyboard.register_key("Ctrl+V", lambda: print("Комбинация Ctrl+V теперь выводит 1"), lambda: print("Отмена действия для Ctrl+V"))  # Переназначение действия и его отмены для комбинации клавиш Ctrl+V

    workflow.perform()  # Выполнение рабочего процесса

if __name__ == '__main__':  # Проверка, запускается ли скрипт напрямую

    main()  # Вызов функции main
