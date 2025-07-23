import turtle

# Setup
screen = turtle.Screen()
screen.title("Line with Python Turtle")

t = turtle.Turtle()
t.pensize(3)
t.pencolor("black")
t.speed('normal')

# Get user input for line endpoints
x1 = float(input("Enter starting X coordinate: "))
y1 = float(input("Enter starting Y coordinate: "))
x2 = float(input("Enter ending X coordinate: "))
y2 = float(input("Enter ending Y coordinate: "))

# Move to the start point without drawing
t.penup()
t.goto(x1, y1)
t.pendown()

# Draw the line to the end point
t.goto(x2, y2)

# Finish
t.hideturtle()
screen.mainloop()
