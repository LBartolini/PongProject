import net
from pong import game
import time
import random as r
import numpy as np
import matplotlib.pyplot as plt


winner_genome_a = net.Network([5, 3, 1], weights_path=f"Saves_little_04/best.txt")
winner_genome_b = net.Network([5, 3, 1], weights_path=f"Saves_little_04/best.txt")

input('START GAME')
init=True
while True:
    if init: up_a, down_a, up_b, down_b = False, False, False, False
    dx_a, dy_a, dx_b, dy_b, ball_y, ball_dx, ball_dy = game(up_a, down_a, up_b, down_b)
    up_a = winner_genome_a.forward_propagation([dx_a, dy_a, ball_y, ball_dx, ball_dy])>0.5
    down_a = not up_a
    up_b = winner_genome_b.forward_propagation([-dx_b, dy_b, ball_y, -ball_dx, ball_dy])>0.5
    down_b = not up_b
    init = False

    


