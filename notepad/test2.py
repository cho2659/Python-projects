import tkinter as tk
from tkinter.scrolledtext import ScrolledText

window = tk.Tk()
window.geometry("400x400")

def set_font(size):
    textField1.configure(font=('Times new Roman', size))

f = tk.Frame(window)
f.pack(side="bottom", fill="x")
for size in (8, 12, 18, 24):
    b = tk.Button(f, text=size, width=2, command=lambda size=size: set_font(size))
    b.pack(side="left")


PW1 = tk.PanedWindow(master=window,orient='vertical',bg="#E0E0E0",bd=9)
PW1.pack(side='left',expand='True',fill='both')
PW1.grid_propagate(False)
PW1.grid_rowconfigure(0, weight=1)
PW1.grid_columnconfigure(0, weight=1)
textField1 = ScrolledText(master=PW1,font=('Times New Roman',12), width=1, height=1)
textField1.grid(row=0, column=0, padx=5, pady=5,sticky='nsew')

window.mainloop()