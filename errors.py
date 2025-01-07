from tkinter import *
from tkinter import messagebox

# Root configuration
root = Tk()
root.configure(bg='lightblue')
root.title('Area of a Circle')

# Frames for layout
frame = Frame(root, bg='lightblue')
frame.pack(pady=10, padx=40)
frame1 = Frame(root, bg='lightblue')
frame1.pack(pady=10, padx=40)

# Function to calculate area
def areaofcircle():
    try:
        radius = float(entry.get())
        if radius < 0:
            raise ValueError("Negative radius")
        area = 3.14 * (radius ** 2)
        output.delete(1.0, END)
        output.insert(END, f'The area of the circle with\nradius {radius} is {area:.2f}')
    except ValueError:
        messagebox.showerror('Error', 'Invalid input. Please enter a positive number.')

# Widgets
Label(frame, text='Enter the radius for the circle:', bg='lightblue').grid(row=0, column=0, pady=5)
entry = Entry(frame, width=20)
entry.grid(row=0, column=1, pady=5)

button = Button(frame1, text='Generate', width=10, command=areaofcircle)
button.grid(row=0, column=0, pady=10)

output = Text(root, width=30, height=5, borderwidth=5, relief=RIDGE)
output.pack(pady=10)

# Mainloop
root.mainloop()
