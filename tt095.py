#!/usr/bin/env python2.7

import Tkinter

class App:
    def __init__(self, root, use_geometry, show_buttons):
        fm = Tkinter.Frame(root, width=300, height=200, bg="blue")
        fm.pack(side=Tkinter.TOP, expand=Tkinter.NO, fill=Tkinter.NONE)

        if use_geometry:
            root.geometry("600x400")  ### (1) Note geometry Window Manager method

        if show_buttons:
            Tkinter.Button(fm, text="Button 1", width=10).pack(side=Tkinter.LEFT)
            Tkinter.Button(fm, text="Button 2", width=10).pack(side=Tkinter.LEFT)
            Tkinter.Button(fm, text="Button 3", width=10).pack(side=Tkinter.LEFT)


case = 0
for use_geometry in (0, 1):
    for show_buttons in (0, 1):
        case = case + 1
        root = Tkinter.Tk()
        root.wm_title("Case " + str(case))  ### (2) Note wm_title Window Manager method
        display = App(root, use_geometry, show_buttons)
        root.mainloop()
