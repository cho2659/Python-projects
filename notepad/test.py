# import GUI
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Spinbox

# create instance
win = tk.Tk()

# title name
win.title("Notepad ver.1.0")

# resizable option
win.resizable(True, True)

# geometry
win.geometry("1900x1000")


def click(e):
    GetFont = 'Arial, ' + str(FontSize.get())
    scr.configure(font=GetFont)

# frame 1
frame1 = ttk.LabelFrame(win, text='')
frame1.grid(column=0, row=0)

# font size
ttk.Label(frame1, text='Font Size:').grid(column=1, row=2)

# font spin box
FontSize = Spinbox(frame1, from_=10, to=60, width=4)
FontSize.grid(column=2, row=2)


# frame2
frame2 = ttk.LabelFrame(win, text='')
# set the width and height of your frame as desired using ipadx and ipady
frame2.grid(column=0, row=7, sticky=tk.S, ipadx=920, ipady=400)
# disable grid propagation to prevent resizing on font size changes

# scrolled text
ScrWidth = 0
ScrHight = 0
scr = scrolledtext.ScrolledText(frame2, width=ScrWidth, height=ScrHight)
scr.pack(side='left', fill="both", expand=True, padx=1, pady=1)
scr.config(font='Arial, 10')
scr.grid_propagate(False)

scr.insert(tk.INSERT, 'Sample Text')

win.bind("<ButtonRelease-1>", click)

# start GUI
win.mainloop()