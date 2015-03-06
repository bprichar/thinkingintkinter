#!/usr/bin/env python2.7

import Tkinter

root = Tkinter.Tk()

myContainer1 = Tkinter.Frame(root)
myContainer1.pack()

button1 = Tkinter.Button(myContainer1)  ### (1)
button1["text"] = "Hello, World!"       ### (2)
button1["background"] = "green"         ### (3)
button1.pack()                          ### (4)

root.mainloop()
