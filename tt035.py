#!/usr/bin/env python2.7

import Tkinter

class MyApp:                            ### (1)
    def __init__(self, myParent):       ### (1a)
        self.myContainer1 = Tkinter.Frame(myParent)
        self.myContainer1.pack()

        self.button1 = Tkinter.Button(self.myContainer1)
        self.button1["text"] = "Hello, World!"
        self.button1["background"] = "green"
        self.button1.pack()

root = Tkinter.Tk()
myapp = MyApp(root)  ### (2)
root.mainloop()      ### (3)
