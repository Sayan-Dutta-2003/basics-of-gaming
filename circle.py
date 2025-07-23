import turtle

# Setup
screen = turtle.Screen()
screen.title("Circle with Python Turtle")

t = turtle.Turtle()
t.pensize(3)
t.pencolor("black")
t.speed('normal')

# Draw a circle of radius 100
radius = 100
t.circle(radius)

# Finish
t.hideturtle()
screen.mainloop()
