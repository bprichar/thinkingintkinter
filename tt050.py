#!/usr/bin/env python2.7

import Tkinter

class MyApp:
    def __init__(self, parent):
        self.myContainer1 = Tkinter.Frame(parent)
        self.myContainer1.pack()

        self.button1 = Tkinter.Button(self.myContainer1)
        self.button1["text"] = "Hello, World!"
        self.button1["background"] = "green"
        self.button1.pack(side=Tkinter.LEFT)    ### (1)

        self.button2 = Tkinter.Button(self.myContainer1)
        self.button2.configure(text="Off to join the circus!")
        self.button2.configure(background="tan")
        self.button2.pack(side=Tkinter.LEFT)   ### (2)

        self.button3 = Tkinter.Button(self.myContainer1)
        self.button3.configure(text="Join me?", background="cyan")
        self.button3.pack(side=Tkinter.LEFT)   ### (3)

        self.button4 = Tkinter.Button(self.myContainer1, text="Goodbye!", background="red")
        self.button4.pack(side=Tkinter.LEFT)   ### (4)

root = Tkinter.Tk()
myapp = MyApp(root)
root.mainloop()
