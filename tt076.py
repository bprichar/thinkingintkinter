#!/usr/bin/env python2.7

import Tkinter

class MyApp:
    def __init__(self, parent):

        ### 1 -- At the outset, we haven't yet invoked any button handler.
        self.myLastButtonInvoked = None

        self.myParent = parent
        self.myContainer1 = Tkinter.Frame(parent)
        self.myContainer1.pack()

        self.yellowButton = Tkinter.Button(self.myContainer1, command=self.yellowButtonClick)
        self.yellowButton.configure(text="YELLOW", background="yellow")
        self.yellowButton.pack(side=Tkinter.LEFT)

        self.redButton = Tkinter.Button(self.myContainer1, command=self.redButtonClick)
        self.redButton.configure(text="RED", background="red")
        self.redButton.pack(side=Tkinter.LEFT)

        self.whiteButton = Tkinter.Button(self.myContainer1, command=self.whiteButtonClick)
        self.whiteButton.configure(text="WHITE", background="white")
        self.whiteButton.pack(side=Tkinter.LEFT)

    def redButtonClick(self):
        print "RED     button clicked.  Previous button invoked was", self.myLastButtonInvoked ### 2
        self.myLastButtonInvoked = "RED"  ### 1

    def yellowButtonClick(self):
        print "YELLOW  button clicked.  Previous button invoked was", self.myLastButtonInvoked ### 2
        self.myLastButtonInvoked = "YELLOW"  ### 1

    def whiteButtonClick(self):
        print "WHITE   button clicked.  Previous button invoked was", self.myLastButtonInvoked ### 2
        self.myLastButtonInvoked = "WHITE"  ### 1


print "\n"*100 # a simple way to clear the screen
print "Starting..."
root = Tkinter.Tk()
myapp = MyApp(root)
root.mainloop()
print "... Done!"
