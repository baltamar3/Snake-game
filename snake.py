import turtle

# Escenario del juego
window = turtle.Screen()
window.title("Snake Game @BrayanAltamar")
window.bgcolor("black")
window.setup(width=600,height=600)

# Cabeza Serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

while True:
    window.update()

window.exitonclick() 