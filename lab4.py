import time


class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class Action1(Command):
    def execute(self):
        print("Выполнено действие 1")

    def undo(self):
        pass


class Action2(Command):
    def execute(self):
        print("Выполнено действие 2")

    def undo(self):
        pass


class Action3(Command):
    def execute(self):
        print("Выполнено действие 3")

    def undo(self):
        pass


class VirtualKeyboard:
    def __init__(self):
        self.actions = {}
        self.history = []

    def assign_action(self, key, action):
        self.actions[key] = action
        print(f"Клавиша {key} назначена на действие {action.__class__.__name__}")

    def press_key(self, key):
        if key in self.actions:
            action = self.actions[key]
            action.execute()
            self.history.append(action)
            print(f"Нажата клавиша {key}")

    def undo_last_action(self):
        if self.history:
            action = self.history.pop()
            action.undo()
            print(f"Отменено действие {action.__class__.__name__}")
        else:
            print(f"История пуста")


keyboard = VirtualKeyboard()

keyboard.assign_action("F1", Action1())
keyboard.assign_action("Ctrl+Alt+Del", Action2())
keyboard.assign_action("Сtrl+S", Action3())
print('////////////////////////////////')
time.sleep(3)

keyboard.press_key("F1")  #Выполнено действие 1
time.sleep(3)

keyboard.press_key("Ctrl+Alt+Del")  #Выполнено действие 2
time.sleep(3)

keyboard.press_key("Ctrl+S")  #Выполнено действие 3
time.sleep(3)

keyboard.undo_last_action()  #Отменено действие 3
time.sleep(3)

keyboard.undo_last_action() #Отменено действие 2
time.sleep(3)

keyboard.undo_last_action()  #Отменено действие 1
time.sleep(3)

keyboard.undo_last_action()  #Нечего отменять
print('////////////////////////////////')
time.sleep(3)

keyboard.assign_action("F1", Action3())
keyboard.assign_action("Ctrl+Alt+Del", Action1())
time.sleep(3)

keyboard.press_key("F1")  #Выполнено действие 3
time.sleep(3)

keyboard.press_key("Ctrl+Alt+Del")  #Выполнено действие 1
print('////////////////////////////////')
