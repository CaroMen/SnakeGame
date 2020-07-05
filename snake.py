# Created with inspiration from Tetris game using Turtle

import turtle
import time
import random

# Screen info
screen = turtle.Screen()
screen.title('Snake by @carodevcodes')
screen.bgcolor("grey")
screen.setup(width=600, height=600)
screen.tracer(0)

delay = .1

# Starting head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lightblue")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# Move snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)


def move_up():
    head.direction = "up"


def move_down():
    head.direction = "down"


def move_left():
    head.direction = "left"


def move_right():
    head.direction = "right"


# Keyboard binding, move around
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")


# Main loop
while True:
    screen.update()

    move()

    time.sleep(delay)

screen.mainloop()
