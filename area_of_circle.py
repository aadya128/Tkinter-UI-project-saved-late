from tkinter import *
from tkinter import messagebox
root=Tk()

root.configure(bg='#DEB887')
root.title('AREA OF A CIRCLE')

frame = Frame(root, bg='#FFE4C4')
frame.pack(pady=10, padx=60)
frame1 = Frame(root, bg='#FFE4C4')
frame1.pack(pady=10, padx=60)

def areaofcircle():
    try:
        radius=float(entry.get())
        area=3.14 * (radius **2)
        output.delete(1.0, END)
        output.insert(END,f'the area of the circle with radius {radius} is \n{area}')
    except:
        messagebox.showerror('ERRORRR', 'sorry invalid expression.\n try again.')

label=Label(frame, text='Enter the radius for the circle: ', bg='#FA8072')
label.grid(row=0, column=0, pady=5, padx=5)

entry = Entry(frame, width=20)
entry.grid(row=0, column=1, pady=5, padx=5)

button = Button(frame1, text='GENERATE',width=8, command=areaofcircle, bg='#8B4513',fg='white')
button.grid(row=0, column=0)

output = Text(root, width=50,height=8, borderwidth=5, relief=RIDGE,bg='#FFA07A' )
output.pack(pady=10,padx=5)

root.mainloop()



