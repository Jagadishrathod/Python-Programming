import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()

s.title("3D CUBOID")
s.screensize(800,800,bg="White")
t.pencolor("black")
t.pensize(3)

def cube():
    for i in range(4):
        t.forward(100)
        t.left(90)


cube()
t.right(30)
t.forward(100)
t.left(30)
cube()
t.left(90)
t.forward(100)
t.left(30+30)
t.forward(100)
t.right(90+30+30)
t.forward(100)
t.right(30)
t.forward(100)
t.left(90+210)
t.forward(100)
t.right(90+30)
t.forward(100)

turtle.done()