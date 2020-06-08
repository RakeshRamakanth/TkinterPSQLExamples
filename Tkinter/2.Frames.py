from tkinter import *

root = Tk()
root.geometry("500x500")  # Width x Height
frame1 = Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=2, width=100, height=100, bd= 0)
frame1.pack(side = TOP)
frame1.pack_propagate(False)

frame2 = Frame(root, highlightbackground="red", highlightcolor="red", highlightthickness=10, width=100, height=100, bd= 0)
frame2.pack(side = BOTTOM)
frame2.pack_propagate(False)

frame3 = Frame(root, highlightbackground="yellow", highlightcolor="red", highlightthickness=10, width=100, height=100, bd= 0)
frame3.pack(side = LEFT)
frame3.pack_propagate(False)

frame4 = Frame(root, highlightbackground="brown", highlightcolor="red", highlightthickness=10, width=100, height=100, bd= 0)
frame4.pack(side = RIGHT)
frame4.pack_propagate(False)
root.mainloop()