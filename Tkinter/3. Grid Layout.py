from tkinter import *

root = Tk()
root.geometry("500x500")

label1 = Label(root, text = "In Grid row =10, column= 10")
label1.grid(row =10, column= 10)

label2 = Label(root, text = "In Grid row =100, column= 100")
label2.grid(row =100, column= 100)

root.mainloop()
