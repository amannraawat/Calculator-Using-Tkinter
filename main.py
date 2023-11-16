from tkinter import *

root = Tk()

entry = Entry(root)
entry.grid(row=1, padx=4, pady=5, columnspan=8)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        each_number = Button(root, text=numbers[counter], height=4, width=6)
        each_number.grid(row=x+2, column=y, padx=5, pady=5)
        counter += 1

root.mainloop()