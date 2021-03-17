from tkinter import *

window = Tk()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

title_text = StringVar() 
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

window.mainloop()