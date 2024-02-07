# import GUI
import tkinter as tk
from tkinter import ttk
from tkinter import Spinbox as sp
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import scrolledtext
import random as r
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# create instance
win = tk.Tk()

# title name
win.title("num-picker ver.1.0")

# resizable option
win.resizable(False, False)

# changing icon
win.iconbitmap('compstui_1_64028.ico')

# window size
win.geometry("375x200")

alpha = 0
beta = 0

# spin call
def spin_call_1():
    global alpha
    alpha = spin1.get()

def spin_call_2():
    global beta
    beta = spin2.get()

# gen button function
def click():
    try:
        global x
        global alpha
        global beta
        alpha = int(alpha)
        beta = int(beta)
        scr.config(state='normal')
        x = r.randint(alpha, beta)
        scr.delete("1.0", "end")
        scr.insert(tk.INSERT, x)
        scr.config(state='disabled')
    except:
        msg.showerror('num-picker ver.1.0', 'Error, please try again!')


# copy button function
def copy():
    try:
        win.clipboard_clear()
        win.clipboard_append(x)
        win.update()
    except:
        msg.showerror('num-picker ver.1.0', 'Please generate the number first!')


# add spin box
spin1 = sp(from_=0, to= 10000000000000, width=15, command=spin_call_1, relief='sunken', font=('Helventica', 10))
spin1.grid(column=1, row=0)

spin2 = sp(from_=0, to= 10000000000000, width=15, command=spin_call_2, relief='sunken', font=('Helventica', 10))
spin2.grid(column=3, row=0)

# menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# add a lable
lable_1 = ttk.Label(win, text= ' ~ ')
lable_1.grid(column=2, row=0)

# add gen button
action_1 = ttk.Button(win, text='Generate', command=click)
action_1.grid(column=2, row=1)

# add copy button
action_1 = ttk.Button(win, text='Copy', command=copy)
action_1.grid(column=2, row=3)

# add scrolled text
scrol_w = 50
scrol_h = 6
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=2, columnspan=5)
scr.config(state='disabled')

# about
def about():
    msg.showinfo('num-picker ver.1.0', 'num-picker made by \'Ian Cho\' \nAt the year 2023.')

# exit
def quit():
    win.quit()
    win.destroy()
    exit()

# create menu and add menu items
file_menu = Menu(menu_bar, tearoff=0)

file_menu.add_command(label='Exit', command=quit)
menu_bar.add_cascade(label='File', menu=file_menu)

# add another menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=about)

# start GUI
win.mainloop()