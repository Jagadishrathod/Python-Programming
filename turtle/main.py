import turtle
import time

t = turtle.Turtle()
s = turtle.Screen()

s.title("3D Shapes")
s.screensize(800,800,bg="White")
t.pencolor("black")
t.pensize(3)

def line():
    t.forward(200)
    t.left(90)
def square():
    for i in range(4):
        t.forward(100)
        t.left(90)
def rectangle():
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)
def triangle():
    for i in range(3):
        t.forward(100)
        t.left(120)
def circle():
    t.circle(80)
def ellipse():
    for i in range(2):
        t.circle(120, 90)
        t.circle(120//2, 90)
    t.seth(45)

if __name__== "__main__":
    check = int(input("Enter the Following 3D Drawings you want to Draw: "))
    if(check == 1):
        line()
    elif(check == 2):
        square()
        t.right(30)
        t.forward(100)
        t.left(30)
        square()
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
    elif(check == 3):
        rectangle()
        t.right(30)
        t.forward(100)
        t.left(30)
        rectangle()
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
    elif(check == 4):
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
    elif (check == 5):
        circle()
    elif (check == 6):
        ellipse()
    else:
        pass

turtle.done