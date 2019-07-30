from tkinter import *
from tkinter import messagebox

window=Tk()

result = 0


#def okClick():
#    #name = txt.get()
#    messagebox.showinfo("이름", "test")


def test_func(): 
    #print("hello")
    messagebox.showinfo("이름", "hello")


button1 = Button(window, text="1", command=test_func)
button1.pack()

label = Label(window, text=result)
label.pack()

window.mainloop()