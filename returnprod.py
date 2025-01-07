from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Returning Sum if Product is less than 1000')
root.configure(bg='#DDA0DD')

frame = Frame(root, bg='#BA55D3')
frame.pack()
frame1 = Frame(root, bg='#BA55D3')
frame1.pack()

def lessthan1000():
    try:
        n1=int(entry1.get())
        n2=int(entry2.get())
        prod=n1*n2
        sumof=n1+n2
        output.delete(1.0,END)
        if prod<=1000:
            output.insert(END, prod)
        else:
            output.insert(END, sumof)
    except:
        messagebox.showerror('ERRORRR!', 'Try another value!')

label1=Label(frame, text='Enter n1: ', bg='#FF00FF')
label1.grid(row=0, column=0, pady=5, padx=5)
label2=Label(frame, text='Enter n2: ', bg='#FF00FF')
label2.grid(row=1, column=0, pady=5, padx=5)

entry1 = Entry(frame, width=20)
entry1.grid(row=0, column=1, pady=5, padx=5)
entry2 = Entry(frame, width=20)
entry2.grid(row=1, column=1, pady=5, padx=5)

button = Button(frame1, text='GENERATE',width=8, command=lessthan1000, bg='#006400',fg='white')
button.grid(row=1, column=0)

output = Text(root, bg='#663399', width=20, height=5, fg='white')
output.pack(padx=10, pady=10)

root.mainloop()