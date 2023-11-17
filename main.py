from tkinter import *

root = Tk()
i = 0


def get_number(num):
    global i
    entry.insert(i, num)
    i += 1


def get_operations(operator):
    global i
    length = len(operator)
    entry.insert(i, operator)
    i += length


def all_clear():
    entry.delete(0, END)


entry = Entry(root)
entry.grid(row=1, padx=4, pady=5, columnspan=8)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        each_number = Button(root, text=numbers[counter], height=4, width=6, command=lambda text=numbers[counter]: get_number(text))
        each_number.grid(row=x+2, column=y, padx=5, pady=5)
        counter += 1

zero_button = Button(root, text='0', height=4, width=6, command=lambda: get_number(0))
zero_button.grid(row=5, column=1, padx=5, pady=5)

operators = ['+', '-', '*', '/', '%', '**', '(', '3.14', ')', '**2']
count = 0
for x in range(4):
    for y in range(3):
        if count < len(operators):
            op_button = Button(root, text=operators[count], height=4, width=6, command=lambda text=operators[count]: get_operations(text))
            op_button.grid(row=x+2, column=y+3, padx=5, pady=5)
            count += 1

allclr_button = Button(root, text='AC', height=4, width=6, command=all_clear)
allclr_button.grid(row=5, column=0, padx=5, pady=5)

root.mainloop()
