from tkinter import *
root = Tk()
root.title("Shapes")
root.geometry("800x800")

area = Canvas(root, height=800, width=800)
area.pack()

circle = area.create_oval(20,20, 150,150,fill="black")
rectangle = area.create_rectangle(180, 20, 300, 150, fill="black")
line = area.create_line(320,20, 450,20, width=3)
trinagle = area.create_polygon(480,20, 620,20, 550, 150, 480, 20, fill="black")

ellipse = area.create_oval(20,200, 150,300, fill="black")
square = area.create_rectangle(180,200, 280,300, fill="black")
right_angle = area.create_arc(320,200, 420,300, fill="black")
root.mainloop()

