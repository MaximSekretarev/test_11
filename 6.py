from tkinter import *

def b1():
    select = list(list1.curselection())
    select.reverse()
    for i in select:
        list2.insert(END, list1.get(i))
        list1.delete(i)


def b2():
    select = list(list2.curselection())
    select.reverse()
    for i in select:
        list1.insert(END, list2.get(i))
        list2.delete(i)


root = Tk()
root.title('6')
root.resizable(False, False)

l_frame = Frame(root)
r_frame = Frame(root)
rr_frame = Frame(root)
l_frame.pack(side= LEFT)
r_frame.pack(side= LEFT)
rr_frame.pack(side= LEFT)

list1 = Listbox(l_frame, selectmode=EXTENDED)
list1.pack()

list2 = Listbox(rr_frame, selectmode=EXTENDED)
list2.pack()

for i in ['apple', 'bananas', 'carrot', 'meat', 'potato']:
    list1.insert(END, i)

but1 = Button(r_frame, text='>>>', command=b1)
but1.pack()
but2 = Button(r_frame, text='<<<', command=b2)
but2.pack()

root.mainloop()





