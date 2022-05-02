from tkinter import *


def click(event):
    c.x = event.x + c.radius
    c.y = event.y + c.radius





root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()
c.radius = 10
c.ball = c.create_oval(0, 100, c.radius * 2, 100 + c.radius * 2, fill='yellow')
c.bind("<Button-1>", click)
root.mainloop()
