from tkinter import *

window = Tk()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

title_text = StringVar() 
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

window.mainloop()