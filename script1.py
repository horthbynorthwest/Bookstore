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

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

year_input = StringVar()
e3 = Entry(window, textvariable=year_input)
e3.grid(row=1, column=1)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

isbn_input = StringVar()
e4 = Entry(window, textvariable=isbn_input)
e4.grid(row=1, column=3)

window.mainloop()