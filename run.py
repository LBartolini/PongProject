import net
from pong import game
import time
import random as r
import numpy as np
import matplotlib.pyplot as plt

popolation = []
GENOME_SIZE = 50
for i in range(GENOME_SIZE):
    popolation.append(net.Network([5, 5, 3, 1]))#, weights_path=f"Saves_little/save_{i}.txt"))

def log_change(best_five):
    vectors = []

    for i, j in zip(np.logspace(-5, -1, 4), range(len(best_five))):
        vectors.append(best_five[j] + (np.random.uniform(-1, 1, len(best_five[j]))*i)*best_five[j])

    for _ in range(25):
        vectors.append(np.random.uniform(-1, 1, len(best_five[0])))

    for i in range(len(best_five)):
        vectors.append(best_five[i])

    return np.array(vectors)    

best = 0
#a = net.Network([2, 3, 2], weights_path="best.txt")
epochs = 100

std_all = []
mean_all = []


ups = []
RUNS_PER_GENOME = 5
hits_mean_evolution, hits_std_evolution = [], []

for epoch in range(epochs):
    hits_genome_mean = []
    for genome in range(GENOME_SIZE):
        
        hits_genome = []
        for _ in range(RUNS_PER_GENOME):
            up, down = False, False
            hit = 0
            flag = False
            while ((not flag) and hit<25):
                flag, dx, dy, ball_y, ball_dx, ball_dy, hit = game(up, down, hit, False)
                fp = popolation[genome].forward_propagation([dx, dy, ball_y, ball_dx, ball_dy])

                up = fp > 0.5
                ups.append(fp)
                down = not up
            hits_genome.append(hit)
        hits_genome_mean.append(np.mean(hits_genome))

    best_genome_indexes = np.argsort(hits_genome_mean)[::-1]
    winner_genome = popolation[best_genome_indexes[0]]

    
    # evolution here
    best_five_genomes = [popolation[index] for index in best_genome_indexes[:5]]
    best_five_genomes = [x.export() for x in best_five_genomes]
    new_genomes = log_change(best_five_genomes)
    for i, c in enumerate(new_genomes):
        popolation[i]._import(c)
    
    # logging
    best_10_hits = [hits_genome_mean[index] for index in best_genome_indexes[:10]]
    hits_mean_evolution.append(np.mean(best_10_hits))
    hits_std_evolution.append(np.std(best_10_hits))

    np.array(hits_std_evolution).tofile("std_53_01.txt", sep=" ")
    np.array(hits_mean_evolution).tofile("mean_53_01.txt", sep=" ")
    
    print(f'Epoch {epoch}: {hits_mean_evolution[-1]:.2f} +/- {hits_std_evolution[-1]:.2f}')

    for i, c in enumerate(popolation):  
        c.export().tofile(f"Saves_little/save_{i}.txt", sep=" ")
    winner_genome.export().tofile("Saves_little/best.txt", sep=" ")

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

    


