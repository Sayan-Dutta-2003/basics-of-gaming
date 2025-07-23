import turtle

screen = turtle.Screen()
screen.title("Trapezium with Python Turtle")

t = turtle.Turtle() 
t.pensize(3)
t.pencolor("black")
t.speed('normal')

t.penup()
t.left(180)
t.forward(100)
t.right(180)
t.pendown()

t.forward(200)  
t.left(120)   
t.forward(100)   
t.left(60)     
t.forward(100)   
t.left(60)  
t.forward(100)  

t.hideturtle()
screen.mainloop()