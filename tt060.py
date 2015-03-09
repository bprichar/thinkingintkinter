#!/usr/bin/env python2.7

import Tkinter

class MyApp:
    def __init__(self, parent):
        self.myParent = parent  ### (7) remember my parent, the root
        self.myContainer1 = Tkinter.Frame(parent)
        self.myContainer1.pack()

        self.button1 = Tkinter.Button(self.myContainer1)
        self.button1.configure(text="OK", background="green")
        self.button1.pack(side=Tkinter.LEFT)
        self.button1.bind("<Button-1>", self.button1Click) ### (1)

        self.button2 = Tkinter.Button(self.myContainer1)
        self.button2.configure(text="Cancel", background="red")
        self.button2.pack(side=Tkinter.RIGHT)
        self.button2.bind("<Button-1>", self.button2Click) ### (2)

    def button1Click(self, event):    ### (3)
        if self.button1["background"] == "green": ### (4)
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"

    def button2Click(self, event):   ### (5)
        self.myParent.destroy()      ### (6)

root = Tkinter.Tk()
myapp = MyApp(root)
root.mainloop()
