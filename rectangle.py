import turtle

screen = turtle.Screen()
screen.title("Rectangle with Python Turtle")

t = turtle.Turtle()
t.pensize(3)
t.pencolor("black")
t.speed('normal')

width = 50
height = 100

t.penup()
t.goto(-width/2, -height/2)  # center the rectangle
t.pendown()

for _ in range(2):
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)

t.hideturtle()
screen.mainloop()
