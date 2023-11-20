from tkinter import *
import ast

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


def calculate():
    string = entry.get()
    try:
        node = ast.parse(string, mode='eval')
        result = eval(compile(node, '<string>', 'eval'))
        all_clear()
        entry.insert(0, result)
    except Exception:
        all_clear()
        entry.insert(0, 'Error')


def last_cut():
    string = entry.get()
    if len(string) != 0:
        new_string = string[:-1]
        all_clear()
        entry.insert(0, new_string)
    else:
        all_clear()
        entry.insert(0, '')


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

equalto_button = Button(root, text='=', height=4, width=6, command=calculate)
equalto_button.grid(row=5, column=4, padx=5, pady=5)

point_button = Button(root, text='.', height=4, width=6, command=lambda: get_number('.'))
point_button.grid(row=5, column=2, padx=5, pady=5)

lastcut_button = Button(root, text='<--', height=4, width=6, command=last_cut)
lastcut_button.grid(row=5, column=5, padx=5, pady=5)

root.mainloop()
