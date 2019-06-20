
# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import os
import time
import random as r
import numpy as np
import random as r

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
collision_a = 30
collision_b = 30


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=int(collision_a/10),stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=int(collision_b/10),stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 8 * r.choice([1, -1])
ball.dy = 8 * r.choice([np.random.uniform(-1, -0.5), np.random.uniform(1, 0.5)])

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()

pen.hideturtle()
pen.goto(0, 260)
#pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 10
    paddle_b.sety(y)

# Keyboard bindings
#wn.listen()
#wn.onkeypress(paddle_a_up, "w")
#wn.onkeypress(paddle_a_down, "s")
#wn.onkeypress(paddle_b_up, "Up")
#wn.onkeypress(paddle_b_down, "Down")


def game(a_up, a_down, b_up, b_down):
    global score_b, score_a, collision_a, collision_b

    if a_up: paddle_a_up()
    if a_down: paddle_a_down()
    if b_up: paddle_b_up()
    if b_down: paddle_b_down()
    pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Border checking
    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if paddle_a.ycor() > 290:
        paddle_a.sety(290)
    
    elif paddle_a.ycor() < -290:
        paddle_a.sety(-290)

    if paddle_b.ycor() > 290:
        paddle_b.sety(290)
    
    elif paddle_b.ycor() < -290:
        paddle_b.sety(-290)

    # Left and right
    if ball.xcor() > 355:
        score_a += 1
        ball.dx *= -1 
        ball.dy = 8 * r.choice([np.random.uniform(-1, -0.5), np.random.uniform(1, 0.5)])
        ball.goto(0, 0)
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)

    elif ball.xcor() < -355:
        score_b += 1
        ball.dx *= -1 
        ball.dy = 8 * r.choice([np.random.uniform(-1, -0.5), np.random.uniform(1, 0.5)])
        ball.goto(0, 0)
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)

    

    # Paddle and ball collisions
    if ball.dx<0 and ball.xcor() < -345 and ball.ycor() < paddle_a.ycor() + collision_a and ball.ycor() > paddle_a.ycor() - collision_a:
        ball.dx *= -1 
        ball.dy = ball.dy * np.random.uniform(1, 1.05)
    
    elif ball.dx>0 and ball.xcor() > 345 and ball.ycor() < paddle_b.ycor() + collision_b and ball.ycor() > paddle_b.ycor() - collision_b:
        ball.dx *= -1 
        ball.dy = ball.dy * np.random.uniform(1, 1.05)

    wn.update()
    pen.clear()
    delta_x_a = paddle_a.xcor() - ball.xcor()
    delta_y_a = paddle_a.ycor() - ball.ycor()
    delta_x_b = paddle_b.xcor() - ball.xcor()
    delta_y_b = paddle_b.ycor() - ball.ycor()
    ball_bottom = 290 - ball.ycor()
    ball_top = -290 -ball.ycor()

    return delta_x_a/100, delta_y_a/100, delta_x_b/100, delta_y_b/100, ball.ycor()/100, ball.dx/4, ball.dy/4