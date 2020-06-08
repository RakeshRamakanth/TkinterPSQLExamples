from tkinter import *

def function(value):
    labl = Label(frame2,text = "this is submenu "+value)
    labl.pack()

root = Tk()
root.geometry("500x500")
frame1 = Frame(root,highlightthickness=2,highlightbackground="green", width=500, height=20, bd= 0)
frame1.pack(side= TOP)

frame2 = Frame(root,highlightthickness=2,highlightbackground="green", width=500, height=20, bd= 0)
frame2.pack(side= BOTTOM)

mainmenu = Menu(root)
root.config(menu = mainmenu)

submenu1 = Menu(mainmenu)
mainmenu.add_cascade(label = "File", menu =submenu1)
submenu1.add_command(label= "New", command = lambda : function("New"))
submenu1.add_command(label= "Open", command = lambda : function("Open"))
submenu1.add_separator()
submenu1.add_command(label = "quit", command= root.quit)

submenu2= Menu(mainmenu)
mainmenu.add_cascade(label = "Edit", menu = submenu2)
submenu2.add_command(label = "Font", command = lambda : function("font"))
submenu2.add_separator()
submenu2.add_command(label = "quit", command= root.quit)

root.mainloop()