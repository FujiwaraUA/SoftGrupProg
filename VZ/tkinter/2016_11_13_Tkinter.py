# -*- coding: utf-8 -*-
# # Скрипт
# import tkinter
#
#
# def printer(event):
#     print("Как всегда очередной 'Hello World!'")
#
#
# root = tkinter.Tk()
# but = tkinter.Button(root)
# but["text"] = "Печать"
# but.bind("<Button-1>", printer)
#
# but.pack()
# root.mainloop()

import tkinter


class But_print:
    def __init__(self, tk):
        self.tk = tk
        self.but = tkinter.Button(tk)
        self.but["text"] = "Печать"
        self.but.bind("<Button-1>", self.printer)
        self.but.pack()

    def printer(self, event):
        print("Как всегда очередной 'Hello World!'")


root = tkinter.Tk()
obj = But_print(root)
root.mainloop()