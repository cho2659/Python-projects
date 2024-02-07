# import GUI
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


# create instance
win = tk.Tk()

# title name
win.title("Notepad ver.1.0")

# resizable option
win.resizable(True, True)

# geometry
win.geometry("1900x1000")

# frame 1
frame1 = ttk.LabelFrame(win, text='')
frame1.grid(column=0, row=0)
# some lables are inside frame1
ttk.Label(frame1, text='Hello World').grid(column=0, row=0)

win.rowconfigure(7, weight=1)
win.columnconfigure(0, weight=1)

# frame2
frame2 = ttk.LabelFrame(win, text='')
# set the width and height of your frame as desired using ipadx and ipady
### changed sticky option to "nsew"
frame2.grid(column=0, row=7, sticky="nsew", ipadx=880, ipady=370)
# disable grid propagation to prevent resizing on font size changes
#frame2.grid_propagate(False)  # it is not necessary

# scrolled text
ScrWidth = 0
ScrHight = 0
scr = scrolledtext.ScrolledText(frame2, wrap=tk.WORD, width=ScrWidth, height=ScrHight)
scr.pack(side='left', fill="both", expand=True, ipadx=0, ipady=0)
scr.config(font='Arial, 10')
#scr.grid_propagate(False)  # it is not necessary

# start GUI
win.mainloop()