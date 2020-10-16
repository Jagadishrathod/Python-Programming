import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()

s.title("3D CUBE")
s.screensize(800,800,bg="White")
t.pencolor("black")
t.pensize(3)

def circle():
    t.circle(80)

circle()

turtle.done()