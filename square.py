import turtle

screen = turtle.Screen()
screen.title("Square with Python Turtle")

t = turtle.Turtle()
t.pensize(3)
t.pencolor("black")
t.speed('normal')

t.penup()
t.left(180)
t.forward(100)
t.left(180)
t.pendown()

side_length = 200
for _ in range(4):
    t.forward(side_length)
    t.left(90)

t.hideturtle()
screen.mainloop()
