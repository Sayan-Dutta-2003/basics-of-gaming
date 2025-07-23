import turtle

screen = turtle.Screen()
screen.title("Oval with Python Turtle")

t = turtle.Turtle()
t.pensize(3)
t.pencolor("black")
t.speed('normal')

radius = 70

t.left(45)
for loop in range(2):     
    t.circle(radius,90)
    t.circle(radius/2,90)

t.hideturtle()
screen.mainloop()