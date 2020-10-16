import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()

s.title("3D CUBE")
s.screensize(800,800,bg="White")
t.pencolor("black")
t.pensize(3)

def Rectangle():
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)

Rectangle()
t.right(30)
t.forward(100)
t.left(30)
Rectangle()
t.left(90)
t.forward(100)
t.left(30+30)
t.forward(100)
t.right(90+30+30)
t.forward(200)
t.right(30)
t.forward(100)
t.left(90+210)
t.forward(100)
t.right(90+30)
t.forward(100)

turtle.done()