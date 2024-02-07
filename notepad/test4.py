import tkinter as tk
from tkinter import scrolledtext

def on_resize(event):
    # Adjust the size of the LabelFrame and ScrolledText widget when the window size changes
    label_frame.config(width=event.width // 2, height=event.height // 2)
    text_area.config(width=(event.width // 20), height=(event.height // 20))

root = tk.Tk()
root.title("Resizable ScrolledText in LabelFrame Example")

# Create a LabelFrame widget
label_frame = tk.LabelFrame(root, text="Resizable LabelFrame")

# Pack the LabelFrame widget and make it fill the entire window
label_frame.pack(fill=tk.BOTH, expand=True)

# Create a ScrolledText widget inside the LabelFrame
text_area = scrolledtext.ScrolledText(label_frame, wrap=tk.WORD)

# Pack the ScrolledText widget and make it fill the LabelFrame
text_area.pack(fill=tk.BOTH, expand=True)

# Bind the event handler to the window resizing event
root.bind("<Configure>", on_resize)

root.mainloop()
