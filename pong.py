# Simple Pong in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import os
import time
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
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=3,stretch_len=1)
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
ball.dx = 5
ball.dy = 5

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
    y += 3
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 3
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
    global score_b, score_a

    if player:
        wn.listen()
        wn.onkeypress(paddle_b_up, "Up")
        wn.onkeypress(paddle_b_down, "Down")
        paddle_b.shapesize(stretch_wid=5,stretch_len=1)
        pen.write(f"Computer : {score_a} Player : {score_b}", align='center', font=('Courier', 24, 'normal'))
        collision = 50
    else:
        paddle_b.shapesize(stretch_wid=40,stretch_len=1)
        collision = 400


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

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        flag = True
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        flag = True
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 30 and ball.ycor() > paddle_a.ycor() - 30:
        ball.dx *= -1 
        hit += 1
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + collision and ball.ycor() > paddle_b.ycor() - collision:
        ball.dx *= -1

    if visualize: 
        wn.update()
        pen.clear()
    delta_x = paddle_a.xcor() - ball.xcor()
    delta_y = paddle_a.ycor() - ball.ycor()

    return flag, delta_x, delta_y, hit
    