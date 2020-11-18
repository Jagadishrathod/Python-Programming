from vpython import *

def circle():
    circle = sphere(pos=vector(0,0,0), color=color.red, radius=0.5)
def cube():
    cube = box(pos=vector(1,-1,1), color=color.green, height=0.4, width=1.2, lenght=1.2)
def triangle():
    triangle = pyramid(pos=vector(2,5,2), size=vector(4,2,3), color=color.yellow)
def line():
    line =arrow(pos=vector(0,-1,0), axis=vector(1,1,1), color=color.cyan)
def ellipse():
    ellipse = ellipsoid(pos=vector(2,2,2),axis=vector(1,1,1), lenght=5, height=2.5, width=3)

# sphere(pos=vector(0,0,0), color=color.red, radius=0.5)
# box(pos=vector(1,-1,1), color=color.green, height=0.4, width=1.2, lenght=1.2)
# arrow(pos=vector(-1,2,2), axis=vector(3,1,1), color=color.cyan)
# pyramid(pos=vector(2,5,2), size=vector(4,2,3), color=color.yellow)
# obj.rotate(angle=pi/4., axis=axis, origin=pos)
# E = ellipsoid(pos=vector(2,2,2),axis=vector(1,1,1), lenght=5, height=2.5, width=3)
# T = triangle(
#     v0=vertex(pos=vec(0,0,0)),
#     v1=vertex(pos=vec(1,0,0)),
#     v2=vertex(pos=vec(1,1,0))
# )
# T.rotate(angle=pi/4., axis=axis, origin=pos)
if __name__== "__main__":
    while(1):
        check = int(input("Enter the Following 3D Drawings you want to Draw: "))
        if(check == 1):
            line()
        elif(check == 2):
            cube()
        elif(check == 3):
            triangle()
        elif(check == 4):
            circle()
        elif(check == 5):
            ellipse()
        else:
            pass
