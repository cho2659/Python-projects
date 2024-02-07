# import gui
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import scrolledtext
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# create instance
win = tk.Tk()

# title name
win.title("txt_2_morse_code ver.1.0")

# resizable option
win.resizable(False, False)

# window size
win.geometry("375x300")

# changing icon
win.iconbitmap('wmploc_460.ico')

# morse code list
alpha_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", 
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", "--.-", ".-.", "...", 
            "-", "..-", "...-", ".--", "-..-", "-.--", "--.." ]

beta_list = [".-.-.-", "--..--", "..--..", ".----.", "-.-.--", "-..-.", "---...", "-.-.-.", 
            "-...-", ".-.-.", "-....-", "..--.-", ".-..-."]

num_list = ["-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", 
            "---..", "----."]

# add input scrolled text
scrol_w = 50
scrol_h = 8
scr1 = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr1.grid(column=0, row=0, columnspan=5)
scr1.config(state='normal')

# add output scrolled text
scrol_w = 50
scrol_h = 8
scr2 = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr2.grid(column=0, row=2, columnspan=5)
scr2.config(state='disabled')

code = []
txt = ''
morse_code = ''

# convert butten function
def convert():
    global morse_code
    code.clear()
    txt = scr1.get(1.0, 'end')
    txt = str(txt)
    txt = txt.strip()
    
    for i in range(len(txt)):
        # alpha list
        if (txt[i] == 'A') or (txt[i] == 'a'):
            code.append(alpha_list[0])
        elif (txt[i] == 'B') or (txt[i] == 'b'):
            code.append(alpha_list[1])
        elif (txt[i] == 'C') or (txt[i] == 'c'):
            code.append(alpha_list[2])
        elif (txt[i] == 'D') or (txt[i] == 'd'):
            code.append(alpha_list[3])
        elif (txt[i] == 'E') or (txt[i] == 'e'):
            code.append(alpha_list[4])
        elif (txt[i] == 'F') or (txt[i] == 'f'):
            code.append(alpha_list[5])
        elif (txt[i] == 'G') or (txt[i] == 'g'):
            code.append(alpha_list[6])
        elif (txt[i] == 'H') or (txt[i] == 'h'):
            code.append(alpha_list[7])
        elif (txt[i] == 'I') or (txt[i] == 'i'):
            code.append(alpha_list[8])
        elif (txt[i] == 'J') or (txt[i] == 'j'):
            code.append(alpha_list[9])
        elif (txt[i] == 'K') or (txt[i] == 'k'):
            code.append(alpha_list[10])
        elif (txt[i] == 'L') or (txt[i] == 'l'):
            code.append(alpha_list[11])
        elif (txt[i] == 'M') or (txt[i] == 'm'):
            code.append(alpha_list[12])
        elif (txt[i] == 'N') or (txt[i] == 'n'):
            code.append(alpha_list[13])
        elif (txt[i] == 'O') or (txt[i] == 'o'):
            code.append(alpha_list[14])
        elif (txt[i] == 'P') or (txt[i] == 'p'):
            code.append(alpha_list[15])
        elif (txt[i] == 'Q') or (txt[i] == 'q'):
            code.append(alpha_list[16])
        elif (txt[i] == 'R') or (txt[i] == 'r'):
            code.append(alpha_list[17])
        elif (txt[i] == 'S') or (txt[i] == 's'):
            code.append(alpha_list[18])
        elif (txt[i] == 'T') or (txt[i] == 't'):
            code.append(alpha_list[19])
        elif (txt[i] == 'U') or (txt[i] == 'u'):
            code.append(alpha_list[20])
        elif (txt[i] == 'V') or (txt[i] == 'v'):
            code.append(alpha_list[21])
        elif (txt[i] == 'W') or (txt[i] == 'w'):
            code.append(alpha_list[22])
        elif (txt[i] == 'X') or (txt[i] == 'x'):
            code.append(alpha_list[23])
        elif (txt[i] == 'Y') or (txt[i] == 'y'):
            code.append(alpha_list[24])
        elif (txt[i] == 'Z') or (txt[i] == 'z'):
            code.append(alpha_list[25])
        
        # num_list
        elif (txt[i] == '0'):
            code.append(num_list[0])
        elif (txt[i] == '1'):
            code.append(num_list[1])
        elif (txt[i] == '2'):
            code.append(num_list[2])
        elif (txt[i] == '3'):
            code.append(num_list[3])
        elif (txt[i] == '4'):
            code.append(num_list[4])
        elif (txt[i] == '5'):
            code.append(num_list[5])
        elif (txt[i] == '6'):
            code.append(num_list[6])
        elif (txt[i] == '7'):
            code.append(num_list[7])
        elif (txt[i] == '8'):
            code.append(num_list[8])
        elif (txt[i] == '9'):
            code.append(num_list[9])
        
        # beta list
        elif (txt[i] == '.'):
            code.append(beta_list[0])
        elif (txt[i] == ','):
            code.append(beta_list[1])
        elif (txt[i] == '?'):
            code.append(beta_list[2])
        elif (txt[i] == "'"):
            code.append(beta_list[3])
        elif (txt[i] == '!'):
            code.append(beta_list[4])
        elif (txt[i] == '/'):
            code.append(beta_list[5])
        elif (txt[i] == ':'):
            code.append(beta_list[6])
        elif (txt[i] == ';'):
            code.append(beta_list[7])
        elif (txt[i] == '='):
            code.append(beta_list[8])
        elif (txt[i] == '+'):
            code.append(beta_list[9])
        elif (txt[i] == '-'):
            code.append(beta_list[10])
        elif (txt[i] == '_'):
            code.append(beta_list[11])
        elif (txt[i] == '"'):
            code.append(beta_list[12])
        elif (txt[i] == '@'):
            code.append(beta_list[13])
        
        # blank
        elif (txt[i] == ' '):
            code.append(' ')
        
        # next line
        elif (txt[i] == '\n'):
            code.append('\n')
        
        # else
        else:
            msg.showerror('txt_2_morse_code ver.1.0', 'Error')
            break

    morse_code = ''.join(code)

    # put into scr2
    scr2.config(state='normal')
    scr2.delete("1.0", "end")
    scr2.insert(tk.INSERT, morse_code)
    scr2.config(state='disabled')

# add convert butten
action_1 = ttk.Button(win, text='Convert', command=convert)
action_1.grid(column=2, row=1)

# copy butten function
def copy():
    win.clipboard_clear()
    win.clipboard_append(morse_code)
    win.update()

# add copy butten
action_2 = ttk.Button(win, text='Copy', command=copy)
action_2.grid(column=2, row=3)

# menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# exit
def quit():
    win.quit()
    win.destroy()
    exit()

# about
def about():
    msg.showinfo('txt_2_morse_code ver.1.0', 'Morse code converter made by \'Ian Cho\' \nAt the year 2023.')

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