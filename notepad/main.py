# import GUI
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import scrolledtext
from tkinter import Spinbox
from tkinter import filedialog
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# create instance
win = tk.Tk()

# title name
win.title("Notepad ver.1.0")

# resizable option
win.resizable(True, True)

# geometry
win.geometry("1900x1000")

# fullscreen
win.attributes('-fullscreen', False)

# changing icon
win.iconbitmap('notepad_2_2.ico')

# quit
def quit():
    AskQuit = msg.askquestion('Notepad ver.1.0', 'Would You want to Quit?')
    if AskQuit == 'yes':
        win.quit()
        win.destroy()
        exit()
    elif AskQuit == 'no':
        pass

def about():
    msg.showinfo('Notepad ver.1.0', 'Notepad made by \'Ian Cho\' \nAt the year 2024.')
    msg.showinfo('Notepad ver.1.0', 'Special Thanks to "JRiggles" and "acw1668" from stackoverflow for fixing the bug!')


# save function

def save_as():
    try:
        global FilePath
        FilePath = filedialog.asksaveasfile(title= 'Save As', defaultextension='.txt',
                                        filetypes=[
                                            ('Text File', '.txt'),
                                            ('All Files', '.*')
                                        ])
        SaveAsFileText1 = str(scr.get(1.0, tk.END))
        FilePath.write(SaveAsFileText1)
        FilePath.close()
    except:
        pass

def open_file_def():
    AskDel = msg.askquestion('Notepad ver.1.0', 'If you open your file everything you write will be gone will you still do this?')
    if AskDel == 'yes':
        try:
            global FilePath
            FilePath = filedialog.askopenfilename(title='Open',
                                            filetypes=[
                                                ('Text File', '.txt'),
                                                ('All Files', '.*')
                                            ])
            file1 = open(FilePath, 'r')
            scr.delete(1.0, tk.END)
            scr.insert(tk.INSERT, file1.read())
            file1.close()
        except:
            pass
    elif AskDel == 'no':
        pass

def save():
    global FilePath    
    try:
        file2 = open(FilePath, 'w')
        SaveFileText2 = str(scr.get(1.0, tk.END))
        file2.write(SaveFileText2)
        file2.close()
    except:
        try:
            FilePath = filedialog.asksaveasfile(title= 'Save As', defaultextension='.txt',
                                            filetypes=[
                                                ('Text File', '.txt'),
                                                ('All Files', '.*')
                                            ])
            SaveFileText2 = str(scr.get(1.0, tk.END))
            FilePath.write(SaveFileText2)
            FilePath.close()
        except:
            pass

def keyup(e):
    ScrLength = len(str(scr.get(1.0, tk.END))) - 1
    length.config(text=ScrLength)
    if AutoSaveCheckVar.get() == '1':
        try:
            file3 = open(FilePath, 'w')
            SaveFileText3 = str(scr.get(1.0, tk.END))
            file3.write(SaveFileText3)
            file3.close()
        except:
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
                    msg.showwarning('Notepad ver.1.0', 'Save Path has not been decided!')
    elif AutoSaveCheckVar.get() == '0':
        pass
    else:
        pass

def click(e):
    GetFont = 'Arial, ' + str(FontSize.get())
    scr.configure(font=GetFont)
    if AutoSaveCheckVar.get() == '1':
        try:
            file3 = open(FilePath, 'w')
            SaveFileText3 = str(scr.get(1.0, tk.END))
            file3.write(SaveFileText3)
            file3.close()
        except:
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
                msg.showwarning('Notepad ver.1.0', 'Save Path has not been decided!')
    elif AutoSaveCheckVar.get() == '0':
        pass
    else:
        pass

#def update_text_widget_size():
    # Adjust the width and height of the ScrolledText widget based on the content
#    scr.update_idletasks()
#    scr.config(width=ScrWidth, height=ScrHight)

# frame 1
frame1 = ttk.LabelFrame(win, text='')
frame1.grid(column=0, row=0)

# save button
#SaveButton = ttk.Button(frame1, text='Save', command=save)
#SaveButton.grid(column=0, row=0)

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


# Save As button
#SaveAsButton = ttk.Button(frame1, text='Save As', command=save_as)
#SaveAsButton.grid(column=0, row=2)

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

# frame2
frame2 = ttk.LabelFrame(win, text='')
# set the width and height of your frame as desired using ipadx and ipady
frame2.grid(column=0, row=7, sticky='nsew', ipadx=880, ipady=370)
# disable grid propagation to prevent resizing on font size changes

# scrolled text
ScrWidth = 0
ScrHight = 0
scr = scrolledtext.ScrolledText(frame2, wrap=tk.WORD, width=ScrWidth, height=ScrHight)
scr.pack(side='left', fill="both", expand=True, ipadx=0, ipady=0)
scr.config(font='Arial, 10')

win.bind("<KeyRelease>", keyup)
win.bind("<ButtonRelease-1>", click)

# Initial adjustment of ScrolledText widget size
#update_text_widget_size()

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