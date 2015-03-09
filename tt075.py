#!/usr/bin/env python2.7

import Tkinter

class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = Tkinter.Frame(parent)
        self.myContainer1.pack()

        self.button1 = Tkinter.Button(self.myContainer1, command=self.button1Click)
        self.button1.bind("<Return>", self.button1Click_a)    ### (1)
        self.button1.configure(text="OK", background="green")
        self.button1.pack(side=Tkinter.LEFT)
        self.button1.focus_force()

        self.button2 = Tkinter.Button(self.myContainer1, command=self.button2Click)
        self.button2.bind("<Return>", self.button2Click_a)   ### (1)
        self.button2.configure(text="Cancel", background="red")
        self.button2.pack(side=Tkinter.RIGHT)

    def button1Click(self):  ### (2)
        print "button1Click event handler"
        if self.button1["background"] == "green": ### (4)
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"

    def button2Click(self):  ### (2)
        print "button2Click event handler"
        self.myParent.destroy()

    def button1Click_a(self, event):  ### (3)
        print "button1Click_a event handler (a wrapper)"
        self.button1Click()

    def button2Click_a(self, event):  ### (3)
        print "button2Click_a event handler (a wrapper)"
        self.button2Click()

root = Tkinter.Tk()
myapp = MyApp(root)
root.mainloop()
