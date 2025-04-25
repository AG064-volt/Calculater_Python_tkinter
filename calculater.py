from tkinter import *

root = Tk()
root.geometry('300x350')
root.title('Калькулятор')
root.resizable(False, False)
root.attributes("-alpha", 0.97)
root.config(bg="light sky blue")
root.iconbitmap(default="keys.ico")

def clear():
    text3.config(text="Результат")
    vidpovid.config(text="0")
    pole1.delete(0,END)
    pole2.delete(0,END)
def plus():
    a = float(pole1.get())
    b = float(pole2.get())
    c = a+b
    vidpovid.config(text=c)
def minus():
    a = float(pole1.get())
    b = float(pole2.get())
    c = a-b
    vidpovid.config(text=c)
def mnoj():
    a = float(pole1.get())
    b = float(pole2.get())
    c = a*b
    vidpovid.config(text=c)
def dilen():
    a = float(pole1.get())
    b = float(pole2.get())
    c = a/b
    vidpovid.config(text=c)

text1 = Label(root, text="Число 1", font=("Arial", 15), bg="sky blue")
text1.place(x=20, y=45)
text2 = Label(root, text="Число 2", font=("Arial", 15), bg="sky blue")
text2.place(x=20, y=95)
text3 = Label(root, text="Результат:", font=("Arial", 20), bg="sky blue")
text3.place(x=20, y=140)
vidpovid = Label(root, text="0", font=("Arial", 20), bg="sky blue")
vidpovid.place(x=180, y=140)

btn1 = Button(root, text="+", font=("Arial",20), padx=10, bg="sky blue", command=plus)
btn1.place(x=20, y=200)
btn2 = Button(root, text="-", font=("Arial",20), padx=10, bg="sky blue", command=minus)
btn2.place(x=90, y=200)
btn3 = Button(root, text="*", font=("Arial",20), padx=10, bg="sky blue", command=mnoj)
btn3.place(x=160, y=200)
btn4 = Button(root, text="/", font=("Arial",20), padx=10, bg="sky blue", command=dilen)
btn4.place(x=230, y=200)
btn5 = Button(root, text="Очистити", font=("Arial",14), padx=80, bg="sky blue", command=clear)
btn5.place(x=20, y=270)

pole1 = Entry(root, width=30, bg="sky blue")
pole1.place(x=100, y=50)
pole2 = Entry(root, width=30, bg="sky blue")
pole2.place(x=100, y=100)

root.mainloop()