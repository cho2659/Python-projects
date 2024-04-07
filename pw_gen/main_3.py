# import GUI
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Spinbox as sp
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import filedialog
import random as r
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# create instance
win = tk.Tk()

# title name
win.title("pw-gen ver.3.5")

# resizable option
win.resizable(False, False)

# changing icon
win.iconbitmap('amd64_microsoft-windows-shell32_31bf3856ad364e35_10_194.ico')

# window size
win.geometry("375x240")

# add a lable
lable_1 = ttk.Label(win, text='Number')
lable_1.grid(column=0, row=0)

lable_2 = ttk.Label(win, text='Special character')
lable_2.grid(column=0, row=1)

lable_3 = ttk.Label(win, text='Capital letter')
lable_3.grid(column=0, row=2)

lable_4 = ttk.Label(win, text='Small letter')
lable_4.grid(column=0, row=3)

# int
alpha = 0
beta = 0
gamma = 0
delta = 0

# make a, b, c, d
a = 0
b = 0
c = 0
d = 0

# make list
list_a = []
list_b = []
list_c = []
list_d = []
z = []

# gen button click funtion
def click():
    scr.config(state='normal')
    list_a.clear()
    list_b.clear()
    list_c.clear()
    list_d.clear()
    z.clear()
    global final

    for i in range(0, int(gamma)):
        a = r.choice(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'))
        list_a.append(a)

    for i in range(0, int(delta)):
        b = r.choice(('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'))
        list_b.append(b)

    for i in range(0, int(alpha)):
        c = r.randint(1, 9)
        c = str(c)
        list_c.append(c)

    for i in range(0, int(beta)):
        d = r.choice(('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?'))
        list_d.append(d)

    x = list_a + list_b + list_c + list_d
    for i in range(0, len(x)):
        y = r.choice(x)
        z.append(y)
        x.remove(y)

    final = ''.join(z)
    final = str(final)

    scr.delete("1.0", "end")
    scr.insert(tk.INSERT, final)
    scr.config(state='disabled')

# copy button click function
def copy():
    win.clipboard_clear()
    win.clipboard_append(final)
    win.update()

# spin call back
def spin_call_1():
    global alpha
    alpha = spin1.get()

def spin_call_2():
    global beta
    beta = spin2.get()

def spin_call_3():
    global gamma
    gamma = spin3.get()

def spin_call_4():
    global delta
    delta = spin4.get()

# spin box
spin1 = sp(from_=0, to=1000, width=5, command=spin_call_1, relief='sunken', font=('Helventica', 10))
spin1.grid(column=1, row=0)

spin2 = sp(from_=0, to=1000, width=5, command=spin_call_2, relief='sunken', font=('Helventica', 10))
spin2.grid(column=1, row=1)

spin3 = sp(from_=0, to=1000, width=5, command=spin_call_3, relief='sunken', font=('Helventica', 10))
spin3.grid(column=1, row=2)

spin4 = sp(from_=0, to=1000, width=5, command=spin_call_4, relief='sunken', font=('Helventica', 10))
spin4.grid(column=1, row=3)

# add gen button
action_1 = ttk.Button(win, text='Generate', command=click)
action_1.grid(column=2, row=4)

# add copy button
action_2 = ttk.Button(win, text='Copy', command=copy)
action_2.grid(column=2, row=5)

# add scrolled text
scrol_w = 50
scrol_h = 6
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)
scr.config(state='disabled')

# exit
def quit():
    win.quit()
    win.destroy()
    exit()

# save
def save():
        try:
            FilePath = filedialog.asksaveasfile(title= 'Save As', defaultextension='.txt',
                                filetypes=[
                                    ('txt file', '.txt')
                                ])
            FileName = str(FilePath).split("'")
            file = open(FileName[1], 'w')
            file.write(final)
            file.close()
        except:
            msg.showerror('pw-gen ver.3.5', 'Error, please try again!')

# about
def about():
    msg.showinfo('pw-gen ver.3.5', 'Password generater made by \'Ian Cho\' \nAt the year 2023. \nThanks to \'shinyangdevelop\' for fixing some bugs for me.')

# menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# create menu and add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save", command=save)
file_menu.add_separator()

file_menu.add_command(label='Exit', command=quit)
menu_bar.add_cascade(label='File', menu=file_menu)

# add another menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=about)

# start GUI
win.mainloop()