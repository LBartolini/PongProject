
# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import os
import time
import random as r
import numpy as np

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
collision_a = 70


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
paddle_b.shapesize(stretch_wid=40,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 6
ball.dy = 6 * np.random.uniform(-1, 1)

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
    y += 5
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 5
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

# Keyboard bindings
#wn.listen()
#wn.onkeypress(paddle_a_up, "w")
#wn.onkeypress(paddle_a_down, "s")
#wn.onkeypress(paddle_b_up, "Up")
#wn.onkeypress(paddle_b_down, "Down")


def game(a_up, a_down, hit, visualize=False, player=False):
    global score_b, score_a, collision_a

    if player:
        wn.listen()
        wn.onkeypress(paddle_b_up, "Up")
        wn.onkeypress(paddle_b_down, "Down")
        paddle_b.shapesize(stretch_wid=5,stretch_len=1)
        pen.write(f"Computer : {score_a} Player : {score_b}", align='center', font=('Courier', 24, 'normal'))
        collision_b = 100
    else:
        paddle_b.shapesize(stretch_wid=40,stretch_len=1)
        collision_b = 400


    if a_up: paddle_a_up()
    if a_down: paddle_a_down()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    flag = False
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
        flag = True
        ball.dy = 6 * np.random.uniform(-1, 1)
        ball.goto(0, 0)
        paddle_a.goto(-350, 0)
        #paddle_b.goto(350, 0)
        ball.dx = abs(ball.dx)
        #ball.dy = abs(ball.dy)

    elif ball.xcor() < -355:
        score_b += 1
        flag = True
        ball.dy = 6 * np.random.uniform(-1, 1)
        ball.goto(0, 0)
        paddle_a.goto(-350, 0)
        #paddle_b.goto(350, 0)
        ball.dx = abs(ball.dx)
        #ball.dy = abs(ball.dy)

    # Paddle and ball collisions
    if ball.dx<0 and ball.xcor() < -350 and ball.ycor() < paddle_a.ycor() + collision_a and ball.ycor() > paddle_a.ycor() - collision_a:
        ball.dx *= -1 
        ball.dy = ball.dy * np.random.uniform(1, 1.05)
        hit += 1
    
    elif ball.dx>0 and ball.xcor() > 350 and ball.ycor() < paddle_b.ycor() + collision_b and ball.ycor() > paddle_b.ycor() - collision_b:
        ball.dx *= -1 
        ball.dy = ball.dy * np.random.uniform(1, 1.05)

    if visualize: 
        wn.update()
        pen.clear()
    delta_x = paddle_a.xcor() - ball.xcor()
    delta_y = paddle_a.ycor() - ball.ycor()
    ball_bottom = 290 - ball.ycor()
    ball_top = -290 -ball.ycor()

    return flag, delta_x/100, delta_y/100, ball.ycor()/100, ball.dx/4, ball.dy/4, hit