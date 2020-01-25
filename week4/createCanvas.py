from tkinter import *

def draw(canvas, width, height):
    canvas.create_rectangle(0, 0, 150, 150, fill="yellow")
    canvas.create_rectangle(100, 50, 250, 100, fill="orange", width=5)
    canvas.create_rectangle(50, 100, 150, 200, fill="green",
                            outline="red", width=3)
    canvas.create_rectangle(125, 25, 175, 190, fill="purple", width=0)

def runDrawing(width=300, height=300):
    root = Tk() # create our window
    canvas = Canvas(root, width=width, height=height)
    canvas.pack() # wrap our window around the canvas
    draw(canvas, width, height) # helper fn
    root.mainloop() # actually creates drawing, events, etc.
    print("bye!")

runDrawing(400, 200)