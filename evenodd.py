from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('EVEN OR ODD.')
root.configure(bg='#A9A9A9')

frame = Frame(root, bg='#2E8B57')
frame.pack()
def evenodd():
    listofnums=[1,2,3,4,5,6,7,8,9]
    
label=Label(frame, text='Enter the number: ', bg='#00FF00')
label.grid(row=0, column=0, pady=5, padx=5)

entry = Entry(frame, width=20)
entry.grid(row=0, column=1, pady=5, padx=5)

button = Button(frame1, text='GENERATE',width=8, command=evenodd, bg='#006400',fg='white')
button.grid(row=1, column=0)

output = Text(root, bg='#228B22', width=50, height=5, fg='white')
output.pack(padx=10, pady=10)

root.mainloop()