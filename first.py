'''from tkinter import *
root = Tk()

label = Label(root, text='Hello World') 
label.pack()

root.mainloop()

from tkinter import *
root=Tk()

label1= Label(root, text='hiii!')
label2= Label(root, text='whabro!')

label1.grid(row=0,column=0)
label2.grid(row=1,column=2)

root.mainloop()'''

'''from tkinter import *
root=Tk()

e = Entry(root, width=50, bg='blue', fg='white', borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.pack()
e.insert(0, 'enter ur name: ')

def myclick():
    hello = 'hello' + e.get()
    mylabel=Label(root, text=hello)
    mylabel.pack()

button = Button(root, text='click',padx=50,pady=50, command=myclick, fg='black', bg='blue')
button.pack()

root.mainloop()'''

from tkinter import *
root=Tk()

root.title('simple calculator')
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3 ,padx=10, pady=10)

def buttonclick(number):
    #e.delete(0, END)
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    return


button1= Button(root,text='1', padx=40, pady=20, command=lambda: buttonclick(1))
button2= Button(root,text='2', padx=40, pady=20, command=lambda: buttonclick(2))
button3= Button(root,text='3', padx=40, pady=20, command=lambda: buttonclick(3))
button4= Button(root,text='4', padx=40, pady=20, command=lambda: buttonclick(4))
button5= Button(root,text='5', padx=40, pady=20, command=lambda: buttonclick(5))
button6= Button(root,text='6', padx=40, pady=20, command=lambda: buttonclick(6))
button7= Button(root,text='7', padx=40, pady=20, command=lambda: buttonclick(7))
button8= Button(root,text='8', padx=40, pady=20, command=lambda: buttonclick(8))
button9= Button(root,text='9', padx=40, pady=20, command=lambda: buttonclick(9))
button0= Button(root,text='0', padx=40, pady=20, command=lambda: buttonclick(0))
buttonplus= Button(root, text='+', padx=39, pady=20, command= lambda: buttonclick())
buttonequal=Button(root, text='=', padx=40, pady=20, command= lambda: buttonclick())
buttonclear=Button(root, text='clear', padx=79, pady=20, command= lambda: buttonclick())
#buttonminus=Button(root, text='-', padx=39,pady=20, command=lambda: buttonclick())

button1.grid(row= 3, column=0)
button2.grid(row= 3, column=1)
button3.grid(row= 3, column=2)

button4.grid(row=2 , column=0)
button5.grid(row= 2, column=1)
button6.grid(row=2 , column=2)

button7.grid(row=1 , column=0)
button8.grid(row=1 , column=1)
button9.grid(row=1, column=2)

button0.grid(row=4 , column=0)
buttonplus.grid(row=4,column=1)
#buttonminus.grid(rows=1, column=2)
buttonclear.grid(row=5, column=0, columnspan=2)
buttonequal.grid(row=5,column=2, columnspan=2)

root.mainloop()

