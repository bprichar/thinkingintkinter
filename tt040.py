#!/usr/bin/env python2.7

import Tkinter

class MyApp:
    def __init__(self, myParent):
        self.myContainer1 = Tkinter.Frame(myParent)
        self.myContainer1.pack()

        self.button1 = Tkinter.Button(self.myContainer1)
        self.button1["text"] = "Hello, World!"           ### (1)
        self.button1["background"] = "green"             ### (1)
        self.button1.pack()

        self.button2 = Tkinter.Button(self.myContainer1)
        self.button2.configure(text="Off to join the circus!") ### (2)
        self.button2.configure(background="tan")               ### (2)
        self.button2.pack()


        self.button3 = Tkinter.Button(self.myContainer1)
        self.button3.configure(text="Join me?", background="cyan")  ### (3)
        self.button3.pack()

        self.button4 = Tkinter.Button(self.myContainer1, text="Goodbye!", background="red") ### (4)
        self.button4.pack()


root = Tkinter.Tk()
myapp = MyApp(root)  ### (2)
root.mainloop()      ### (3)
