from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('N+NN+NNN')
root.configure(bg='#3CB371')

frame = Frame(root, bg='#2E8B57')
frame.pack()
frame1 = Frame(root, bg='#2E8B57')
frame1.pack()
def nnnnnn():
    try:
        number =str(entry.get())
        value = int(number) + int(number+number) + int(number + number + number)
        output.delete(1.0, END)
        output.insert(END, f'the final value of n + nn + nnn is {value}')
    except:
        messagebox.showerror('ERRORRR!', 'Try another value!')

label=Label(frame, text='Enter the number: ', bg='#00FF00')
label.grid(row=0, column=0, pady=5, padx=5)

entry = Entry(frame, width=20)
entry.grid(row=0, column=1, pady=5, padx=5)

button = Button(frame1, text='GENERATE',width=8, command=nnnnnn, bg='#006400',fg='white')
button.grid(row=1, column=0)

output = Text(root, bg='#228B22', width=50, height=5, fg='white')
output.pack(padx=10, pady=10)

root.mainloop()



