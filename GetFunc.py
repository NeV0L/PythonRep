"""
Модуль GetFunc предназначен для получения имен функций
и их ID как информационный материал помогающий аналитику
в поисках новых функций.
В открывшемся окне должно быть предложено выбрать место,
где храняться патчи, после нажатия кнопки "Поиск",
будет выдан список наименований функций и их ID
"""
from tkinter import Label, Tk, Button, StringVar, NONE, W, S, N, E, Text, Frame, Scrollbar, Entry

class Func(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def choice_dir(self):
        dir_name = "asd"

    def initUI(self):
        self.pack(fill=NONE, expand=True)

        dir_name = StringVar()
        # Создаем компоненты
        dir_label  = Label(self, text="Путь папки для поиска:")
        dir_entry  = Entry(self, textvariable=dir_name, width=50)
        dir_button = Button(self, text="Выбрать папку", command=self.choice_dir())
        search_button = Button(self, text="Поиск")
        answer_area = Text(self, height=15, width=20, state='disabled')
        scroll = Scrollbar(self, command=answer_area.yview)

        answer_area.config(yscrollcommand=scroll.set)
        # Распределяем компоненты по экрану
        dir_label.grid(row=1, column=0, sticky=W)
        dir_entry.grid(row=1, column=1, sticky=W)
        dir_button.grid(row=1, column=2, sticky=W, padx=5)
        search_button.grid(row=1, column=3, sticky=W, padx=5)
        answer_area.grid(row=2, column=0, rowspan=1, columnspan=4, padx=5, sticky=S+W+N+E)
        scroll.grid(row=2, column=3, sticky=E+N+S)


def main():
    # Создаем основную форму
    root = Tk()
    root.title("Получение новых функций")
    root.geometry("600x300")
    root.resizable(width=False, height=False)
    Func(root)
    root.mainloop()

if __name__ == '__main__':
    main()