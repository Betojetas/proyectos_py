import turtle

# Configuración de la ventana
window = turtle.Screen()
window.bgcolor("black")

# Dibuja la calabaza
pumpkin = turtle.Turtle()
pumpkin.hideturtle()
pumpkin.color("orange")
pumpkin.dot(200)

# Dibuja los ojos
eye = turtle.Turtle()
eye.hideturtle()
eye.color("black")
eye.penup()
eye.goto(-50, 50)
eye.pendown()
eye.begin_fill()
eye.goto(-25, 75)
eye.goto(0, 50)
eye.goto(-25, 25)
eye.goto(-50, 50)
eye.end_fill()
eye.penup()
eye.goto(50, 50)
eye.pendown()
eye.begin_fill()
eye.goto(25, 75)
eye.goto(0, 50)
eye.goto(25, 25)
eye.goto(50, 50)
eye.end_fill()

# Dibuja la boca
mouth = turtle.Turtle()
mouth.hideturtle()
mouth.color("black")
mouth.penup()
mouth.goto(-100, -75)
mouth.pendown()
mouth.setheading(270)
mouth.circle(100, 180)

# Dibuja el tallo
stem = turtle.Turtle()
stem.hideturtle()
stem.color("green")
stem.penup()
stem.goto(0, 100)
stem.pendown()
stem.setheading(90)
stem.forward(50)

# Cierra la ventana al hacer clic
window.exitonclick()
