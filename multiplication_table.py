from tkinter import *
from tkinter import messagebox
root=Tk()

root.configure(bg='#d4afb9')
root.title("Multiplication Table Generator")

def generate_table():
    try:
        number = int(entry.get())
        stop_num = int(entry1.get())
        output.delete(1.0, END)
        for i in range(1, stop_num + 1):
            output.insert(END, f"{number} x {i} = {number * i}\n")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

frame = Frame(root, bg='#FFB6C1', relief=RIDGE)
frame.pack(pady=8, padx=50)

label = Label(frame, text="Enter a number:", bg='#F5F5DC')
label2 = Label(frame, text='Enter the number to stop the table until: ', bg='#F5F5DC')
label.grid(row=0, column=0, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5)

entry = Entry(frame, width=10, relief=RIDGE, bg='#E6E6FA')
entry.grid(row=0, column=1, padx=5)
entry1 = Entry(frame, width=10, relief=RIDGE, bg='#E6E6FA')
entry1.grid(row=1, column=1, padx=5)

button = Button(frame, text="GENERATE",width=10,height=3, command=generate_table, bg='#C71585', fg='black', relief=RIDGE)
button.grid(row=3, column=2, padx=1)

output = Text(root, width=40, wrap=WORD, bg="#F5F5DC", borderwidth=5, relief=RIDGE)
output.pack(pady=10, padx=10)

root.mainloop()
