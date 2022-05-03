from tkinter import *


def button_click(colour_kod, colour_colour):
    emp_colour.delete(0, END)
    emp_colour.insert(0, colour_kod)
    lab_text_colour['text'] = colour_colour


root = Tk()
root.title('3')
root.resizable(False, False)


lab_text_colour = Label()
lab_text_colour.grid(column=0, row=0, sticky='ew', columnspan=7)
emp_colour = Entry(justify=CENTER)
emp_colour.grid(column=0, row=1, sticky='ew', columnspan=7)

colour = {'#ff0000': 'Красный',
          '#ff7d00': 'Оранжевый',
          '#ffff00': 'Желтый',
          '#00ff00': 'Зеленый',
          '#007dff': 'Голубой',
          '#0000ff': 'Синий',
          '#7d00ff': 'Фиолетовый'}

i = 0
for key in colour:
    colour_key = lambda colour_kod=key, colour_colour=colour[key]: button_click(colour_kod, colour_colour)
    button_colour = Button(background=key, activebackground=key, command=colour_key)
    button_colour.grid(column=i, row=2, sticky='ew')
    i += 1

root.mainloop()


