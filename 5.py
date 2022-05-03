from tkinter import *


def print_text():
    lab_text['text'] = var.get()


root = Tk()
root.title('5')
root.resizable(False, False)
root.columnconfigure(0, minsize=40)
root.columnconfigure(1, minsize=100)

lab_text = Label()

var = StringVar()

batton1 = Radiobutton(text='Вася',variable=var, value='+4 9087654321', indicatoron=0, command=print_text)
batton2 = Radiobutton(text='Петя',variable=var, value='+5 2087653321', indicatoron=0, command=print_text)
batton3 = Radiobutton(text='Маша',variable=var, value='+6 4087632321', indicatoron=0, command=print_text)

lab_text.grid(column=1, row=0, rowspan=2, sticky='ew')
batton1.grid(column=0, row=0, sticky='ew')
batton2.grid(column=0, row=1, sticky='ew')
batton3.grid(column=0, row=2, sticky='ew')

root.mainloop()




