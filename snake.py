import turtle
import time

posponer = 0.2

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
head.direction = "down"

# Funciones
def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

while True:
    window.update()
    mov()
    time.sleep(posponer)

window.exitonclick() 