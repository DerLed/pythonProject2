from tkinter import *
from functools import partial
# import math
import time


def tick():
    tm.after(200, tick)
    tm['text'] = time.strftime('%H:%M:%S')


def update(val):
    counter = int(str(lbl['text']))
    if val == "++":
        counter += 1
    if val == "--":
        counter -= 1
    lbl.configure(text=str(counter))
#
#
#
# # def create_counter():
# #    i = 0
# #    val = 0
# #
# #    def inner():
# #        nonlocal i
# #        if val == 0:
# #            i += 1
# #            return i - 1
# #        else:
# #            i -= 1
# #            return i + 1
# #
# #    return inner
#
#
# # my_counter = create_counter()
#


nums = ['1', '2', '3',
        '4', '5', '6',
        '7', '8', '9']

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('300x400')

tm = Label(font='sans 20')
tm.grid(column=2, row=0)
tm.after_idle(tick)

lbl = Label(window, text="0")
lbl.grid(column=0, row=0)
#
#
Button(text="+", command=partial(update, "++")).grid(column=0, row=1, sticky='nsew')
Button(text="-", command=partial(update, "--")).grid(column=1, row=1, sticky='nsew')

m_coll = 0
m_row = 2
for a in nums:
    # com = lambda x = a: calc(x)
    Button(text=a, width=7, height=2,).grid(column=m_coll, row=m_row, sticky="nsew")
    m_coll += 1
    if m_coll > 2:
        m_coll = 0
        m_row += 1


window.mainloop()
