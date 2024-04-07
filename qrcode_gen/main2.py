# import GUI
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import scrolledtext
from tkinter import filedialog
import qrcode as qr
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# create instance
win = tk.Tk()

# title name
win.title('qrcode-gen ver.1.5')

# resizable option
win.resizable(False, False)

# changing icon
win.iconbitmap('amd64_microsoft-windows-shell32_31bf3856ad364e35_10_38.ico')

# window size
win.geometry("375x180")

# exit
def quit():
    win.quit()
    win.destroy()
    exit()

def about():
    msg.showinfo('qrcode-gen ver.1.5', 'qrcode generater made by \'Ian Cho\' \nAt the year 2024.')

def generate():
    try:
        FilePath = filedialog.asksaveasfile(title= 'Save As', defaultextension='.png',
                                filetypes=[
                                    ('PNG file', '.png')
                                ])
        FileName_a = str(FilePath).split("'")
        FileName_b = FileName_a[1].split('/')
        FileName = FileName_b[-1]
        text = scr.get(1.0,'end')
        qr_img = qr.make(text)
        qr_img.save(FileName)
        msg.showinfo('qrcode-gen ver.1.5', 'Generated successfuly!')
    except:
        pass

# add label
lable_1 = ttk.Label(win, text='Enter url or text:', font=('Arial', 15))
lable_1.grid(column=1, row=0)

# add scrolled text
scrol_w = 50
scrol_h = 6
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)

# add button
action = ttk.Button(win, text='Generate', command=generate)
action.grid(column=1, row=2)

# menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

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