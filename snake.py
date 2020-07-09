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
head.goto(100, 100)
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


# Set movement
def move_up():
    if head.direction != "down":
        head.direction = "up"


def move_down():
    if head.direction != "up":
        head.direction = "down"


def move_left():
    if head.direction != "right":
        head.direction = "left"


def move_right():
    if head.direction != "left":
        head.direction = "right"


# Adding food
food = turtle.Turtle()
food.speed()
food.shape("circle")
food.color("blue")
food.penup()
food.shapesize(.5, .5)
food.goto(0, 0)

# Keyboard binding, move around
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center",
          font=("Courier", 24, "normal"))

# Main loop
while True:
    screen.update()

    # Checks for collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        delay = 0.1

    # Move food randomly
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add tail
        new_seg = turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("white")
        new_seg.penup()
        segments.append(new_seg)

        delay -= 0.001

    # move the tail
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Checks for collision with body
    # for segment in segments:
    #     if segment.distance(head) < 20:
    #         time.sleep(1)
    #         head.goto(0, 0)
    #         head.direction = "stop"

    #         for segment in segments:
    #             segment.goto(1000, 1000)

    #         segments.clear()

    #         delay = 0.1

    time.sleep(delay)

screen.mainloop()
