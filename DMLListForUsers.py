"""
Скрипт для получения DML скриптов по выбранному списку пользователей.
"""
from tkinter import Label, Tk, Button, StringVar, NONE, W, S, N, E, Text, Frame, Scrollbar, Entry, Radiobutton, LabelFrame

class Func(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def getListUsers():
        try:
            with open("users.txt") as file_handler:
                for line in file_handler:
                    if line.find("USERS") != -1:

        except IOError:
            print("Ошибка работы с файлом users.txt")

    def initUI(self):
        self.pack(fill=NONE, expand=True)

        user_label = LabelFrame(self, height=300, width=500, text="Пользователи")
        user_label.pack


def main():
    # Создаем основную форму
    root = Tk()
    root.title("Список скриптов для БД")
    root.geometry("600x900")
    root.resizable(width=False, height=False)
    Func(root)
    root.mainloop()

if __name__ == '__main__':
    main()