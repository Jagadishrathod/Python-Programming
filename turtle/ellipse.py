import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()

s.title("3D Ellipse")
s.screensize(800,800,bg="White")
t.pencolor("black")
t.pensize(3)

def ellipse():
    for i in range(2):
        t.circle(120, 90)
        t.circle(120//2, 90)
        
    t.seth(45)
    
ellipse()

turtle.done()