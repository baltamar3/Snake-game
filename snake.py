import turtle
import time
import random

posponer = 0.15

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

# Comida
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Cuerpo serpiente
body = []

# Funciones
def up():
    head.direction = "up"

def down():
    head.direction = "down"

def right():
    head.direction = "right"

def left():
    head.direction = "left"

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

# Eventos de teclado
window.listen()
window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(right, "Right")
window.onkeypress(left, "Left")

while True:
    window.update()

    # Colisiones bordes
    if head.xcor() == 280  or head.ycor() == 280 or head.xcor() == -280 or head.ycor() == -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for i in body: i.goto(1000,1000)
        body.clear()
    
    # Comer Fruta
    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)


        segment_body = turtle.Turtle()
        segment_body.speed(0)
        segment_body.shape("square")
        segment_body.color("grey")
        segment_body.penup()

        body.append(segment_body)
    
    total_seg = len(body)
    for i in range(total_seg - 1, 0, -1):
        x =  body[i-1].xcor()
        y =  body[i-1].ycor()
        body[i].goto(x,y)
    
    if total_seg > 0:
        body[0].goto(head.xcor(), head.ycor())

    mov()
    time.sleep(posponer)

window.exitonclick() 