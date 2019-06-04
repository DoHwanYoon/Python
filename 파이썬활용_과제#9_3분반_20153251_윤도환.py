from tkinter import *

window = Tk()
window.geometry("360x240")
photo = PhotoImage(file="가위.JPG")
l1=Label(window, image=photo)
l1.place(x=100, y=30)

b1=Button(window, text="가위")
b2=Button(window, text="바위")
b1.place(x=50, y=130)
b2.place(x=160, y=130)

window.mainloop()