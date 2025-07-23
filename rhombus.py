import turtle

# Setup
screen = turtle.Screen()
screen.title("Rhombus with Python Turtle")

t = turtle.Turtle()

t.penup()
t.left(180)
t.forward(80)
t.left(180)
t.pendown()

t.pensize(3)
t.pencolor("black")
t.speed('normal')

t.right(90)
t.circle(85, steps=4)
# Finish
t.hideturtle()
screen.mainloop()
