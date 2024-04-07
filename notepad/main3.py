# import GUI
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import scrolledtext
from tkinter import Spinbox
from tkinter import filedialog
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# create instance
win = tk.Tk()

# title name
win.title("Notepad")

# resizable option
win.resizable(True, True)

# geometry
win.geometry("800x600")

# changing icon
win.iconbitmap('notepad_2_2.ico')

FilePath = None

# quit
def quit():
    AskQuit = msg.askquestion('Notepad', 'Would You want to Quit?')
    if AskQuit == 'yes':
        win.quit()
        win.destroy()
        exit()
    elif AskQuit == 'no':
        pass

def about():
    msg.showinfo('Notepad', 'Notepad made by \'Ian Cho\' \nAt the year 2024.')
    msg.showinfo('Notepad', 'Special Thanks to "JRiggles" and "acw1668" from stackoverflow for fixing the bug!')

def save_check():
    if AutoSaveCheckVar.get() == '1':
        pass
    elif AutoSaveCheckVar.get() == '0':
        if (FilePath == None) or (FilePath == ''):
            win.title('* - Notepad')
        else:
            file_name = str(FilePath).split('\'')
            file_name = str(file_name[1]).split('/')
            win.title('*' + file_name[-1] + ' - Notepad')
    else:
        pass

# save function
def save_as():
    global FilePath
    try:
        FilePath = filedialog.asksaveasfile(title= 'Save As', defaultextension='.txt',
                                        filetypes=[
                                            ('Text File', '.txt'),
                                            ('All Files', '.*')
                                        ])
        SaveAsFileText1 = str(scr.get(1.0, tk.END))
        FilePath.write(SaveAsFileText1)
        FilePath.close()
        file_name = str(FilePath).split('\'')
        file_name = str(file_name[1]).split('/')
        win.title(file_name[-1] + ' - Notepad')

    except:
        pass


def open_file_def():
    global FilePath
    AskDel = msg.askquestion('Notepad', 'If you open your file everything you write will be gone will you still do this?')
    if AskDel == 'yes':
        try:
            FilePath = filedialog.askopenfilename(title='Open',
                                            filetypes=[
                                                ('Text File', '.txt'),
                                                ('All Files', '.*')
                                            ])
            file1 = open(FilePath, 'r')
            scr.delete(1.0, tk.END)
            scr.insert(tk.INSERT, file1.read())
            file1.close()
            ScrLength = len(str(scr.get(1.0, tk.END))) - 1
            length.config(text=ScrLength)
            file_name = str(FilePath).split('\'')
            file_name = str(file_name[1]).split('/')
            win.title(file_name[-1] + ' - Notepad')
        except:
            pass
    elif AskDel == 'no':
        pass

def save():
    global FilePath
    if (FilePath == None) or (FilePath == ''):
        try:
            FilePath = filedialog.asksaveasfile(title= 'Save As', defaultextension='.txt',
                                            filetypes=[
                                                ('Text File', '.txt'),
                                                ('All Files', '.*')
                                            ])
            SaveFileText2 = str(scr.get(1.0, tk.END))
            FilePath.write(SaveFileText2)
            FilePath.close()
            file_name = str(FilePath).split('\'')
            file_name = str(file_name[1]).split('/')
            win.title(file_name[-1] + ' - Notepad')
        except:
            pass
    else:
            try:
                SplitPath = str(FilePath).split("'")
                File = open(SplitPath[1], 'w')
                SaveFileText2 = str(scr.get(1.0, tk.END))
                File.write(SaveFileText2)
                File.close()
                file_name = str(FilePath).split('\'')
                file_name = str(file_name[1]).split('/')
                win.title(file_name[-1] + ' - Notepad')
            except:
                File = open(FilePath, 'w')
                SaveFileText2 = str(scr.get(1.0, tk.END))
                File.write(SaveFileText2)
                File.close()
                file_name = str(FilePath).split('\'')
                file_name = str(file_name[1]).split('/')
                win.title(file_name[-1] + ' - Notepad')

def search_def():
    SearchBoxText = SearchBox.get()    
    scr.tag_delete(1.0, 'END')
    if SearchBox == '':
        scr.tag_delete(1.0, 'END')
    else:
        scr.tag_remove("highlight", "1.0", "end")
        pattern = re.compile(SearchBoxText, re.IGNORECASE)
        matches = pattern.finditer(scr.get("1.0", "end"))
        for match in matches:
            start = f"1.0+{match.start()}c"
            end = f"1.0+{match.end()}c"
            scr.tag_add("highlight", start, end)
            scr.tag_configure("highlight", background="yellow")


def keyup(e):
    global FilePath
    search_def()
    save_check()
    ScrLength = len(str(scr.get(1.0, tk.END))) - 1
    length.config(text=ScrLength)
    if AutoSaveCheckVar.get() == '1':
        if (FilePath == None) or (FilePath == ''):
            try:
                FilePath = filedialog.asksaveasfile(title= 'Save As', defaultextension='.txt',
                                                filetypes=[
                                                    ('Text File', '.txt'),
                                                    ('All Files', '.*')
                                                ])
                SaveFileText3 = str(scr.get(1.0, tk.END))
                FilePath.write(SaveFileText3)
                FilePath.close()
            except:
                    msg.showwarning('Notepad', 'Save Path has not been decided!')
        else:
            try:
                SplitPath3 = str(FilePath).split("'")
                File = open(SplitPath3[1], 'w')
                SaveFileText2 = str(scr.get(1.0, tk.END))
                File.write(SaveFileText2)
                File.close()
            except:
                File = open(FilePath, 'w')
                SaveFileText2 = str(scr.get(1.0, tk.END))
                File.write(SaveFileText2)
                File.close()
    elif AutoSaveCheckVar.get() == '0':
        pass
    else:
        pass

def click(e):
    global FilePath
    GetFont = 'Arial, ' + str(FontSize.get())
    scr.configure(font=GetFont)
    if AutoSaveCheckVar.get() == '1':
        if (FilePath == None) or (FilePath == ''):
            try:
                FilePath = filedialog.asksaveasfile(title= 'Save As', defaultextension='.txt',
                                                filetypes=[
                                                    ('Text File', '.txt'),
                                                    ('All Files', '.*')
                                                ])
                SaveFileText3 = str(scr.get(1.0, tk.END))
                FilePath.write(SaveFileText3)
                FilePath.close()
                file_name = str(FilePath).split('\'')
                file_name = str(file_name[1]).split('/')
                win.title(file_name[-1] + ' - Notepad')
            except:
                    msg.showwarning('Notepad', 'Save Path has not been decided!')
        else:
            try:
                SplitPath3 = str(FilePath).split("'")
                File3 = open(SplitPath3[1], 'w')
                SaveFileText2 = str(scr.get(1.0, tk.END))
                File3.write(SaveFileText2)
                File3.close()
                file_name = str(FilePath).split('\'')
                file_name = str(file_name[1]).split('/')
                win.title(file_name[-1] + ' - Notepad')
            except:
                File3 = open(FilePath, 'w')
                SaveFileText2 = str(scr.get(1.0, tk.END))
                File3.write(SaveFileText2)
                File3.close()
                file_name = str(FilePath).split('\'')
                file_name = str(file_name[1]).split('/')
                win.title(file_name[-1] + ' - Notepad')
    elif AutoSaveCheckVar.get() == '0':
        pass
    else:
        pass

# frame 1
frame1 = ttk.LabelFrame(win, text='')
frame1.grid(column=0, row=0)

# frame 2
frame2 = ttk.LabelFrame(win, text='Search Box')
frame2.grid(column=0, row=1)

# search box
Search = tk.StringVar()
SearchBox = ttk.Entry(frame2, width=50, textvariable=Search)
SearchBox.grid(column=0, row=0)
SearchBox.pack(side='left', fill="both", expand=True, ipadx=0, ipady=0)
SearchBox.config(font='Arial, 10')

# blank
ttk.Label(frame1, text='').grid(column=1, row=0)

# auto save
AutoSaveCheckVar = tk.StringVar()
AutoSaveCheck = tk.Checkbutton(frame1, text='Auto Save', variable=AutoSaveCheckVar, onvalue='1', offrelief= 'flat', state='normal')
AutoSaveCheck.deselect()
AutoSaveCheck.grid(column=1, row=0, sticky=tk.W)

# blank
ttk.Label(frame1, text='   ').grid(column=4, row=2)


# blank
ttk.Label(frame1, text='').grid(column=0, row=1)

# font size
ttk.Label(frame1, text='Font Size:').grid(column=1, row=2)

# font spin box
FontSize = Spinbox(frame1, from_=10, to=60, width=4)
FontSize.grid(column=2, row=2)

# blank
ttk.Label(frame1, text='').grid(column=0, row=5)

# text length
ttk.Label(frame1, text='Text Length:').grid(column=1, row=6)
length = ttk.Label(frame1, text='0')
length.grid(column=2, row=6)

# row 4 blank
ttk.Label(frame1, text='').grid(column=0, row=5)

win.rowconfigure(7, weight=1)
win.columnconfigure(0, weight=1)

# frame3
frame3 = ttk.LabelFrame(win, text='')
frame3.grid(column=0, row=7, sticky='nsew', ipadx=880, ipady=370)

# scrolled text
ScrWidth = 0
ScrHight = 0
scr = scrolledtext.ScrolledText(frame3, wrap=tk.WORD, width=ScrWidth, height=ScrHight)
scr.pack(side='left', fill="both", expand=True, ipadx=0, ipady=0)
scr.config(font='Arial, 10')

win.bind("<KeyRelease>", keyup)
win.bind("<ButtonRelease-1>", click)

# menu bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# create menu and add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu2 = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Save', command=save)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Open', command=open_file_def)
file_menu.add_command(label='Exit', command=quit)

# about
menu_bar.add_cascade(label='About', menu=file_menu2)
file_menu2.add_command(label='About', command=about)

# start GUI
win.mainloop()
