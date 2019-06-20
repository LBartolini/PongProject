import net
from pong import game
import time
import random as r
import numpy as np
import matplotlib.pyplot as plt


winner_genome = net.Network([5, 3, 1], weights_path=f"Saves_little/best.txt")




if True:
    input('START GAME')
    init=True
    vis = True
    player = True
    while True:
        if init: up, down = False, False
        _, dx, dy, ball_y, ball_dx, ball_dy, _ = game(up, down, 0, vis, player=False)
        up = winner_genome.forward_propagation([dx, dy, ball_y, ball_dx, ball_dy])>0.5
        down = not up
        init = False

    


