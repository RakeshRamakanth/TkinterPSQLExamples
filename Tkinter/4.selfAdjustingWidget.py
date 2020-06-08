from tkinter import *

root = Tk()
root.geometry("500x500")

lab1 = Label(root, text = "First", bg = "red", fg = "blue")
lab1.pack(side=BOTTOM ,fill = X)

lab2 = Label(root, text = "Second", bg = "blue", fg = "red")
lab2.pack(side=LEFT, fill= Y)
root.mainloop()