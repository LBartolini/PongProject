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

hit=0

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



class Paddle(object):
    def __init__(self, max_speed=10, speed_step=0.1):
        self.pos = 0
        self.speed = 0
        self.max_speed = max_speed
        self.speed_step = speed_step

p_a = Paddle(max_speed=10, speed_step=5)
p_b = Paddle(max_speed=10, speed_step=5)


# Functions
def paddle_a_up():
    p_a.speed = min(p_a.max_speed, p_a.speed + p_a.speed_step)

def paddle_a_down():
    p_a.speed = max(-p_a.max_speed, p_a.speed - p_a.speed_step)

def paddle_b_up():
    p_b.speed = min(p_b.max_speed, p_b.speed + p_b.speed_step)

def paddle_b_down():
    p_b.speed = max(-p_b.max_speed, p_b.speed - p_b.speed_step)


def game(a_up, a_down, hit, visualize=False, player=False, player2=False, limit_frame=0.00):
    global score_b, score_a,paddle_a, paddle_b

    start_time = time.time()

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

    if player2:
        wn.listen()
        wn.onkeypress(paddle_a_up, "w")
        wn.onkeypress(paddle_a_down, "s")
        a_up=False
        a_down=False


    if a_up: paddle_a_up()
    if a_down: paddle_a_down()


    # Move the paddles
    p_a.pos = p_a.pos + p_a.speed
    paddle_a.sety(p_a.pos)
    p_b.pos = p_b.pos + p_b.speed
    paddle_b.sety(p_b.pos)

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    is_game_over = False


    # Border checking  # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 

    if paddle_a.ycor() > 290:
        p_a.speed=-p_a.speed
    
    elif paddle_a.ycor() < -290:
        p_a.speed=-p_a.speed


    if paddle_b.ycor() > 290:
        p_b.speed=-p_b.speed
    
    elif paddle_b.ycor() < -290:
        p_b.speed=-p_b.speed


    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        is_game_over = True
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        is_game_over = True
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 30 and ball.ycor() > paddle_a.ycor() - 30:
        ball.dx *= -1 
        hit += 1
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + collision and ball.ycor() > paddle_b.ycor() - collision:
        ball.dx *= -1



    if is_game_over:
        paddle_a.goto(-350, 0)
        p_a.speed=0
        p_a.pos=0
        paddle_b.goto(350, 0)
        p_b.speed=0
        p_b.pos=0


    if visualize: 
        wn.update()
        pen.clear()
    delta_x = paddle_a.xcor() - ball.xcor()
    delta_y = paddle_a.ycor() - ball.ycor()

    wait_time = limit_frame - (time.time() - start_time)
    if wait_time > 0:
        time.sleep(wait_time)

    return is_game_over, delta_x, delta_y, hit
    


if __name__ == "__main__":
    for i in range(1000):
        _ = game(False, False, hit=hit, visualize=True, player=True, player2=True, limit_frame=0.03)
