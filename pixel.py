# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')


from tkinter import *
import time  #for sleep

win = Tk()  #win2 = Tk()
win.title("Bouncer: pixel")
winX=300
winY=200
canvas = Canvas(win, bg="black", cursor="cross", width=winX, height=winY) #later win.configure()
#canvas2 = Canvas(win, bg="green", width=30, height=20)
#win2.geometry("200x200+50+50")

canvas.pack()  #canvas2.pack()

canvas.create_line(5, 5, 75, 35, fill="green")  # #00FF00
print("Sleeping...")
time.sleep(1)
print("Woke up...")
win.update()

i=0
x=5
y=5
stepX=1
stepY=2

while True:
    i += 1
    x += stepX;
    y += stepY;
    if x < 1 or x >= winX-1: stepX *= -1
    if y < 1 or y >= winY-1: stepY *= -1
    canvas.create_oval(x,y,x,y,fill="lime")
    win.update()
    win.title(f"Bouncer: pixel ({i})")
mainloop()  #unreachable

"""
# https://rosettacode.org/wiki/Draw_a_pixel#Python
from PIL import Image

img = Image.new('RGB', (320, 240))
pixels = img.load()
pixels[100, 100] = (255, 0, 0)
img.show()


https://www.coursera.org/lecture/interactive-python-1/canvas-and-drawing-sMd7e
import simplegui
def draw(canvas):
    canvas.draw_circle([100,100],2,2,"Red")
frame = simplegui.create_frame("Test",300,200)
frame.set_draw_handler(draw)
frame.start()
"""