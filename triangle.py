
from tkinter import *
import time  #for sleep

win = Tk()
winX=300
winY=200
canvas = Canvas(win, bg="black", cursor="cross", width=winX, height=winY)
canvas.pack()

print("Sleeping...")
time.sleep(1)
print("Woke up...")
win.update()

i=0
x1=5
x2=12
x3=25
y1=12
y2=25
y3=5
stepX1=1
stepX2=2
stepX3=1
stepY1=2
stepY2=1
stepY3=3

while True:
    i += 1
    canvas.create_line(x1, y1, x2, y2, fill="black")
    canvas.create_line(x2, y2, x3, y3, fill="black")
    canvas.create_line(x3, y3, x1, y1, fill="black")
    x1 += stepX1
    x2 += stepX2
    x3 += stepX3
    y1 += stepY1
    y2 += stepY2
    y3 += stepY3
    if x1 < 1 or x1 >= winX-1: stepX1 *= -1
    if x2 < 1 or x2 >= winX-1: stepX2 *= -1
    if x3 < 1 or x3 >= winX-1: stepX3 *= -1
    if y1 < 1 or y1 >= winY-1: stepY1 *= -1
    if y2 < 1 or y2 >= winY-1: stepY2 *= -1
    if y3 < 1 or y3 >= winY-1: stepY3 *= -1
    canvas.create_line(x1, y1, x2, y2, fill="lime")  # #00FF00
    canvas.create_line(x2, y2, x3, y3, fill="lime")  # #00FF00
    canvas.create_line(x3, y3, x1, y1, fill="lime")  # #00FF00
    win.update()
    win.title(f"Bouncer: line ({i})")
mainloop()  #unreachable
