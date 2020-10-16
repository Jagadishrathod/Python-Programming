import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()

s.title("3D CUBE")
s.screensize(800,800,bg="White")
t.pencolor("black")
t.pensize(3)

def triangle():
    for i in range(3):
        t.forward(100)
        t.left(120)

triangle()
t.right(30)
t.forward(100)
t.left(30)
triangle()
t.forward(100)
t.right(90+90+30)
t.forward(100)
t.right(30)
t.forward(100)
t.left(90+90+30)
t.forward(100)

turtle.done()