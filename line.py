# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')


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
x2=25
y1=5
y2=5
stepX1=1
stepX2=2
stepY1=2
stepY2=1

while True:
    i += 1
    canvas.create_line(x1, y1, x2, y2, fill="black")  # #000000, delete last line
    x1 += stepX1
    x2 += stepX2
    y1 += stepY1
    y2 += stepY2
    if x1 < 1 or x1 >= winX-1: stepX1 *= -1
    if x2 < 1 or x2 >= winX-1: stepX2 *= -1
    if y1 < 1 or y1 >= winY-1: stepY1 *= -1
    if y2 < 1 or y2 >= winY-1: stepY2 *= -1
    canvas.create_line(x1, y1, x2, y2, fill="lime")  # #00FF00
    win.update()
    win.title(f"Bouncer: line ({i})")
mainloop()  #unreachable
