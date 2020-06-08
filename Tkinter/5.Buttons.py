from tkinter import *

root = Tk()
root.geometry("500x500")

def radio_btn(value):
    text = "radio button "+ value
    lbl = Label(frame2, text= text, bg="black", fg="white")
    lbl.grid(row=0, column=50)

frame1 = Frame(root,highlightthickness=2,highlightbackground="green", width=500, height=400, bd= 0)
frame1.pack(side= TOP)
frame2 = Frame(root,highlightthickness=2,highlightbackground="blue", width=500, height=100, bd= 0)
frame2.pack(side= LEFT)



btn1 = Button(frame1, text = "Button 1 ", bg= "blue", fg= "brown",command = lambda : radio_btn("one"))
btn1.pack()
btn2 = Button(frame1, text = "Button 1 ", bg= "blue", fg= "brown",command = lambda : radio_btn("two"))
btn2.pack()
btn3 = Button(frame1, text = "Button 1 ", bg= "blue", fg= "brown",command = lambda : radio_btn("three"))
btn3.pack()
btn4 = Button(frame1, text = "Button 1 ", bg= "blue", fg= "brown",command = lambda : radio_btn("four"))
btn4.pack()

root.mainloop()