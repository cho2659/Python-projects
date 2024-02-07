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
win.title("encrypt_n_decrypt ver.1.5")

# resizable option
win.resizable(False, False)

# window size
win.geometry("375x315")

# changing icon
win.iconbitmap('wow64_microsoft-windows-shlwapi_31bf3856ad364e35_10_300.ico')

# 26

capital_list = ["Ha8", "q8G", "Nh9", "b6R", "d6T", "8Xp", "P5u", "W4o", "s3Z", "3zU", "7Zk", "W9o", "9nE", "r1F", "H5n", "J3s", "2vA", "9Pt", "6mK", "T1a", "f9P", "L2p", "u1U", 
"uI2", "3zK", "bF9"]

small_list = ["5Pr", "L2z", "iV3", "m5G", "Ak2", "3Kw", "xF5", "2nB", "Qt3", "A2v", "2Cn", "oO3", "z9S", "Q5d", "3vI", "p5K", "Aj4", "y7D", "5gW", "E1d", "r5X", "6Xm", "4Lg", 
"Ww5", "6Lx", "Fz6"]

num_list = ["4Re", "O6n", "F7o", "yC5", "8eZ", "5xR", "tW3", "xH4", "U5m", "W7w"]

# ! @ # $ % ^ & * ( ) - _ = + ? / . , > < ' " ; : ` ~ [ ] { } 30

character_list = ["m8D", "7zC", "J1j", "m2A", "aT6", "uQ6", "5eR", "9Ql", "nJ7", "u9L", "En4", "P1x", "V3e", "6Bs", "U9c", "q2R", "J4l", "tI9", "Y8h", "gI7", "3Ds", "F6s", 
"Hk2", "9Pm", "3gQ", "8kS", "9tR", "D3k", "9jM", "4Ur"]

space = "9pJ"

next_line = "oL2"

# tab
tab_control = ttk.Notebook(win)

# tab1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Encrypt')
tab_control.pack(expand=1, fill='both')

# add input scrolled text
scrol_w = 50
scrol_h = 8
scr1 = scrolledtext.ScrolledText(tab1, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr1.grid(column=0, row=0, columnspan=5)
scr1.config(state='normal')

# add output scrolled text
scr2 = scrolledtext.ScrolledText(tab1, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr2.grid(column=0, row=2, columnspan=5)
scr2.config(state='disabled')

code1 = []

x1 = ''

txt1 = ''

# encrypt butten function
def encrypt():
    global x1
    code1.clear()
    txt1 = scr1.get(1.0, 'end')
    txt1 = str(txt1)
    txt1 = txt1.strip()

    for i in range(len(txt1)):
        # capital_list
        if (txt1[i] == 'A'):
            code1.append(capital_list[0])
        elif (txt1[i] == 'B'):
            code1.append(capital_list[1])
        elif (txt1[i] == 'C'):
            code1.append(capital_list[2])
        elif (txt1[i] == 'D'):
            code1.append(capital_list[3])
        elif (txt1[i] == 'E'):
            code1.append(capital_list[4])
        elif (txt1[i] == 'F'):
            code1.append(capital_list[5])
        elif (txt1[i] == 'G'):
            code1.append(capital_list[6])
        elif (txt1[i] == 'H'):
            code1.append(capital_list[7])
        elif (txt1[i] == 'I'):
            code1.append(capital_list[8])
        elif (txt1[i] == 'J'):
            code1.append(capital_list[9])
        elif (txt1[i] == 'K'):
            code1.append(capital_list[10])
        elif (txt1[i] == 'L'):
            code1.append(capital_list[11])
        elif (txt1[i] == 'M'):
            code1.append(capital_list[12])
        elif (txt1[i] == 'N'):
            code1.append(capital_list[13])
        elif (txt1[i] == 'O'):
            code1.append(capital_list[14])
        elif (txt1[i] == 'P'):
            code1.append(capital_list[15])
        elif (txt1[i] == 'Q'):
            code1.append(capital_list[16])
        elif (txt1[i] == 'R'):
            code1.append(capital_list[17])
        elif (txt1[i] == 'S'):
            code1.append(capital_list[18])
        elif (txt1[i] == 'T'):
            code1.append(capital_list[19])
        elif (txt1[i] == 'U'):
            code1.append(capital_list[20])
        elif (txt1[i] == 'V'):
            code1.append(capital_list[21])
        elif (txt1[i] == 'W'):
            code1.append(capital_list[22])
        elif (txt1[i] == 'X'):
            code1.append(capital_list[23])
        elif (txt1[i] == 'Y'):
            code1.append(capital_list[24])
        elif (txt1[i] == 'Z'):
            code1.append(capital_list[25])
        
        # small
        elif (txt1[i] == 'a'):
            code1.append(small_list[0])
        elif (txt1[i] == 'b'):
            code1.append(small_list[1])
        elif (txt1[i] == 'c'):
            code1.append(small_list[2])
        elif (txt1[i] == 'd'):
            code1.append(small_list[3])
        elif (txt1[i] == 'e'):
            code1.append(small_list[4])
        elif (txt1[i] == 'f'):
            code1.append(small_list[5])
        elif (txt1[i] == 'g'):
            code1.append(small_list[6])
        elif (txt1[i] == 'h'):
            code1.append(small_list[7])
        elif (txt1[i] == 'i'):
            code1.append(small_list[8])
        elif (txt1[i] == 'j'):
            code1.append(small_list[9])
        elif (txt1[i] == 'k'):
            code1.append(small_list[10])
        elif (txt1[i] == 'l'):
            code1.append(small_list[11])
        elif (txt1[i] == 'm'):
            code1.append(small_list[12])
        elif (txt1[i] == 'n'):
            code1.append(small_list[13])
        elif (txt1[i] == 'o'):
            code1.append(small_list[14])
        elif (txt1[i] == 'p'):
            code1.append(small_list[15])
        elif (txt1[i] == 'q'):
            code1.append(small_list[16])
        elif (txt1[i] == 'r'):
            code1.append(small_list[17])
        elif (txt1[i] == 's'):
            code1.append(small_list[18])
        elif (txt1[i] == 't'):
            code1.append(small_list[19])
        elif (txt1[i] == 'u'):
            code1.append(small_list[20])
        elif (txt1[i] == 'v'):
            code1.append(small_list[21])
        elif (txt1[i] == 'w'):
            code1.append(small_list[22])
        elif (txt1[i] == 'x'):
            code1.append(small_list[23])
        elif (txt1[i] == 'y'):
            code1.append(small_list[24])
        elif (txt1[i] == 'z'):
            code1.append(small_list[25])
        
        # num_list
        elif (txt1[i] == '0'):
            code1.append(num_list[0])
        elif (txt1[i] == '1'):
            code1.append(num_list[1])
        elif (txt1[i] == '2'):
            code1.append(num_list[2])
        elif (txt1[i] == '3'):
            code1.append(num_list[3])
        elif (txt1[i] == '4'):
            code1.append(num_list[4])
        elif (txt1[i] == '5'):
            code1.append(num_list[5])
        elif (txt1[i] == '6'):
            code1.append(num_list[6])
        elif (txt1[i] == '7'):
            code1.append(num_list[7])
        elif (txt1[i] == '8'):
            code1.append(num_list[8])
        elif (txt1[i] == '9'):
            code1.append(num_list[9])

        # character_list
        # ! @ # $ % ^ & * ( ) - _ = + ? / . , > < ' " ; : ` ~ [ ] { } 30
        
        elif (txt1[i] == '!'):
            code1.append(character_list[0])
        elif (txt1[i] == '@'):
            code1.append(character_list[1])
        elif (txt1[i] == '#'):
            code1.append(character_list[2])
        elif (txt1[i] == '$'):
            code1.append(character_list[3])
        elif (txt1[i] == '%'):
            code1.append(character_list[4])
        elif (txt1[i] == '^'):
            code1.append(character_list[5])
        elif (txt1[i] == '&'):
            code1.append(character_list[6])
        elif (txt1[i] == '*'):
            code1.append(character_list[7])
        elif (txt1[i] == '('):
            code1.append(character_list[8])
        elif (txt1[i] == ')'):
            code1.append(character_list[9])
        elif (txt1[i] == '-'):
            code1.append(character_list[10])
        elif (txt1[i] == '_'):
            code1.append(character_list[11])
        elif (txt1[i] == '='):
            code1.append(character_list[12])
        elif (txt1[i] == '+'):
            code1.append(character_list[13])
        elif (txt1[i] == '?'):
            code1.append(character_list[14])
        elif (txt1[i] == '/'):
            code1.append(character_list[15])
        elif (txt1[i] == '.'):
            code1.append(character_list[16])
        elif (txt1[i] == ','):
            code1.append(character_list[17])
        elif (txt1[i] == '>'):
            code1.append(character_list[18])
        elif (txt1[i] == '<'):
            code1.append(character_list[19])
        elif (txt1[i] == '\''):
            code1.append(character_list[20])
        elif (txt1[i] == '"'):
            code1.append(character_list[21])
        elif (txt1[i] == ';'):
            code1.append(character_list[22])
        elif (txt1[i] == ':'):
            code1.append(character_list[23])
        elif (txt1[i] == '`'):
            code1.append(character_list[24])
        elif (txt1[i] == '~'):
            code1.append(character_list[25])
        elif (txt1[i] == '['):
            code1.append(character_list[26])
        elif (txt1[i] == ']'):
            code1.append(character_list[27])
        elif (txt1[i] == '{'):
            code1.append(character_list[28])
        elif (txt1[i] == '}'):
            code1.append(character_list[29])

        # space
        elif (txt1[i] == ' '):
            code1.append(space)

        # next line
        elif (txt1[i] == '\n'):
            code1.append(next_line)

        # else
        else:
            msg.showerror('encrypt_n_decrypt ver.1.5', 'Error')
            break

    x1 = ''.join(code1)

    # put into scr2
    scr2.config(state='normal')
    scr2.delete("1.0", "end")
    scr2.insert(tk.INSERT, x1)
    scr2.config(state='disabled')


# copy1 butten function
def copy1():
    win.clipboard_clear()
    win.clipboard_append(x1)
    win.update()

# add encrypt butten
action_1 = ttk.Button(tab1, text='Encrypt', command=encrypt)
action_1.grid(column=2, row=1)

# add copy1 butten
action_2 = ttk.Button(tab1, text='Copy', command=copy1)
action_2.grid(column=2, row=3)

# tab2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Decrypt')

code2 = []

x2 = ''

txt2 = ''

# decrypt function
def decrypt():
    global x2
    a = 0 # 2nBAk2oO3oO33vI
    b = 3
    code2.clear()
    txt2 = scr3.get(1.0, 'end')
    txt2 = str(txt2)
    txt2 = txt2.strip()

    for i in range((len(txt2)) // 3):
        # capital
        if (txt2[a:b] == capital_list[0]):
            code2.append('A')
        elif (txt2[a:b] == capital_list[1]):
            code2.append('B')
        elif (txt2[a:b] == capital_list[2]):
            code2.append('C')
        elif (txt2[a:b] == capital_list[3]):
            code2.append('D')
        elif (txt2[a:b] == capital_list[4]):
            code2.append('E')
        elif (txt2[a:b] == capital_list[5]):
            code2.append('F')
        elif (txt2[a:b] == capital_list[6]):
            code2.append('G')
        elif (txt2[a:b] == capital_list[7]):
            code2.append('H')
        elif (txt2[a:b] == capital_list[8]):
            code2.append('I')
        elif (txt2[a:b] == capital_list[9]):
            code2.append('J')
        elif (txt2[a:b] == capital_list[10]):
            code2.append('K')
        elif (txt2[a:b] == capital_list[11]):
            code2.append('L')
        elif (txt2[a:b] == capital_list[12]):
            code2.append('M')
        elif (txt2[a:b] == capital_list[13]):
            code2.append('N')
        elif (txt2[a:b] == capital_list[14]):
            code2.append('O')
        elif (txt2[a:b] == capital_list[15]):
            code2.append('P')
        elif (txt2[a:b] == capital_list[16]):
            code2.append('Q')
        elif (txt2[a:b] == capital_list[17]):
            code2.append('R')
        elif (txt2[a:b] == capital_list[18]):
            code2.append('S')
        elif (txt2[a:b] == capital_list[19]):
            code2.append('T')
        elif (txt2[a:b] == capital_list[20]):
            code2.append('U')
        elif (txt2[a:b] == capital_list[21]):
            code2.append('V')
        elif (txt2[a:b] == capital_list[22]):
            code2.append('W')
        elif (txt2[a:b] == capital_list[23]):
            code2.append('X')
        elif (txt2[a:b] == capital_list[24]):
            code2.append('Y')
        elif (txt2[a:b] == capital_list[25]):
            code2.append('Z')

        # small
        elif (txt2[a:b] == small_list[0]):
            code2.append('a')
        elif (txt2[a:b] == small_list[1]):
            code2.append('b')
        elif (txt2[a:b] == small_list[2]):
            code2.append('c')
        elif (txt2[a:b] == small_list[3]):
            code2.append('d')
        elif (txt2[a:b] == small_list[4]):
            code2.append('e')
        elif (txt2[a:b] == small_list[5]):
            code2.append('f')
        elif (txt2[a:b] == small_list[6]):
            code2.append('g')
        elif (txt2[a:b] == small_list[7]):
            code2.append('h')
        elif (txt2[a:b] == small_list[8]):
            code2.append('i')
        elif (txt2[a:b] == small_list[9]):
            code2.append('j')
        elif (txt2[a:b] == small_list[10]):
            code2.append('k')
        elif (txt2[a:b] == small_list[11]):
            code2.append('l')
        elif (txt2[a:b] == small_list[12]):
            code2.append('m')
        elif (txt2[a:b] == small_list[13]):
            code2.append('n')
        elif (txt2[a:b] == small_list[14]):
            code2.append('o')
        elif (txt2[a:b] == small_list[15]):
            code2.append('p')
        elif (txt2[a:b] == small_list[16]):
            code2.append('q')
        elif (txt2[a:b] == small_list[17]):
            code2.append('r')
        elif (txt2[a:b] == small_list[18]):
            code2.append('s')
        elif (txt2[a:b] == small_list[19]):
            code2.append('t')
        elif (txt2[a:b] == small_list[20]):
            code2.append('u')
        elif (txt2[a:b] == small_list[21]):
            code2.append('v')
        elif (txt2[a:b] == small_list[22]):
            code2.append('w')
        elif (txt2[a:b] == small_list[23]):
            code2.append('x')
        elif (txt2[a:b] == small_list[24]):
            code2.append('y')
        elif (txt2[a:b] == small_list[25]):
            code2.append('z')

        # num
        elif (txt2[a:b] == num_list[0]):
            code2.append('0')
        elif (txt2[a:b] == num_list[1]):
            code2.append('1')
        elif (txt2[a:b] == num_list[2]):
            code2.append('2')
        elif (txt2[a:b] == num_list[3]):
            code2.append('3')
        elif (txt2[a:b] == num_list[4]):
            code2.append('4')
        elif (txt2[a:b] == num_list[5]):
            code2.append('5')
        elif (txt2[a:b] == num_list[6]):
            code2.append('6')
        elif (txt2[a:b] == num_list[7]):
            code2.append('7')
        elif (txt2[a:b] == num_list[8]):
            code2.append('8')
        elif (txt2[a:b] == num_list[9]):
            code2.append('9')

        # ! @ # $ % ^ & * ( ) - _ = + ? / . , > < ' " ; : ` ~ [ ] { } 30
        # caracter list
        elif (txt2[a:b] == character_list[0]):
            code2.append('!')
        elif (txt2[a:b] == character_list[1]):
            code2.append('@')
        elif (txt2[a:b] == character_list[2]):
            code2.append('#')
        elif (txt2[a:b] == character_list[3]):
            code2.append('$')
        elif (txt2[a:b] == character_list[4]):
            code2.append('%')
        elif (txt2[a:b] == character_list[5]):
            code2.append('^')
        elif (txt2[a:b] == character_list[6]):
            code2.append('&')
        elif (txt2[a:b] == character_list[7]):
            code2.append('*')
        elif (txt2[a:b] == character_list[8]):
            code2.append('(')
        elif (txt2[a:b] == character_list[9]):
            code2.append(')')
        elif (txt2[a:b]== character_list[10]):
            code2.append('-')
        elif (txt2[a:b] == character_list[11]):
            code2.append('_')
        elif (txt2[a:b] == character_list[12]):
            code2.append('=')
        elif (txt2[a:b] == character_list[13]):
            code2.append('+')
        elif (txt2[a:b] == character_list[14]):
            code2.append('?')
        elif (txt2[a:b] == character_list[15]):
            code2.append('/')
        elif (txt2[a:b] == character_list[16]):
            code2.append('.')
        elif (txt2[a:b] == character_list[17]):
            code2.append(',')
        elif (txt2[a:b] == character_list[18]):
            code2.append('>')
        elif (txt2[a:b] == character_list[19]):
            code2.append('<')
        elif (txt2[a:b] == character_list[20]):
            code2.append('\'')
        elif (txt2[a:b] == character_list[21]):
            code2.append('"')
        elif (txt2[a:b] == character_list[22]):
            code2.append(';')
        elif (txt2[a:b] == character_list[23]):
            code2.append(':')
        elif (txt2[a:b] == character_list[24]):
            code2.append('`')
        elif (txt2[a:b] == character_list[25]):
            code2.append('~')
        elif (txt2[a:b] == character_list[26]):
            code2.append('[')
        elif (txt2[a:b] == character_list[27]):
            code2.append(']')
        elif (txt2[a:b] == character_list[28]):
            code2.append('{')
        elif (txt2[a:b] == character_list[29]):
            code2.append('}')

        # space
        elif (txt2[a:b] == space):
            code2.append(' ')

        # next line
        elif (txt2[a:b] == next_line):
            code2.append('\n')

        # else
        else:
            msg.showerror('encrypt_n_decrypt ver.1.5', 'Error')
            break

        # add
        a = a + 3
        b = b + 3

    # final
    x2 = ''.join(code2)

    # put into scr4
    scr4.config(state='normal')
    scr4.delete("1.0", "end")
    scr4.insert(tk.INSERT, x2)
    scr4.config(state='disabled')

# copy2 butten function
def copy2():
    win.clipboard_clear()
    win.clipboard_append(x2)
    win.update()

# add input scrolled text
scr3 = scrolledtext.ScrolledText(tab2, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr3.grid(column=0, row=0, columnspan=5)
scr3.config(state='normal')

# add output scrolled text
scr4 = scrolledtext.ScrolledText(tab2, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr4.grid(column=0, row=2, columnspan=5)
scr4.config(state='disabled')

# add decrypt butten
action_3 = ttk.Button(tab2, text='Decrypt', command=decrypt)
action_3.grid(column=2, row=1)

# add copy2 butten
action_4 = ttk.Button(tab2, text='Copy', command=copy2)
action_4.grid(column=2, row=3)

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
    msg.showinfo('encrypt_n_decrypt ver.1.5', 'Encrypter & Decrypter made by \'Ian Cho\' \nAt the year 2023.')

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