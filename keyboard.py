import tkinter as tk
import sys

win = tk.Tk()
win.geometry("400x200")
win.title("Keyboard")
win.resizable(0, 0)
win.config(bg="white")
win.wm_attributes("-transparentcolor", "white")
win.attributes("-topmost",True)
win.overrideredirect(True)

def leave():
    sys.exit()

button1 = tk.Button(win, text="W",command=leave,activebackground="#777777",bg="#aaaaaa",font=("Fixedsys",15), relief=tk.RAISED, bd=10)
button2 = tk.Button(win, text="A",command=leave,activebackground="#777777",bg="#aaaaaa",font=("Fixedsys",15), relief=tk.RAISED, bd=10)
button3 = tk.Button(win, text="S",command=leave,activebackground="#777777",bg="#aaaaaa",font=("Fixedsys",15), relief=tk.RAISED, bd=10)
button4 = tk.Button(win, text="D",command=leave,activebackground="#777777",bg="#aaaaaa",font=("Fixedsys",15), relief=tk.RAISED, bd=10)

win.grid_rowconfigure(0, weight=1)
win.grid_rowconfigure(2, weight=1)
win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(4, weight=1)

button1.grid(row=0, column=2, ipadx=40, ipady=20)
button2.grid(row=1, column=1, ipadx=40, ipady=20)
button3.grid(row=1, column=2, ipadx=40, ipady=20)
button4.grid(row=1, column=3, ipadx=40, ipady=20) 

def key_pressed(event):
    if event.char == 'w':
        button1.config(bg="#777777")
    if event.char == 'a':
        button2.config(bg="#777777")
    if event.char == 's':
        button3.config(bg="#777777")
    if event.char == 'd':
        button4.config(bg="#777777")

def key_released(event):
    if event.char == 'w':
        button1.config(bg="#aaaaaa")  
    if event.char == 'a':
        button2.config(bg="#aaaaaa")
    if event.char == 's':
        button3.config(bg="#aaaaaa")
    if event.char == 'd':
        button4.config(bg="#aaaaaa")

win.bind("<KeyPress>", key_pressed)
win.bind("<KeyRelease>", key_released)

win.mainloop()