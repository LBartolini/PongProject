import net
from pong import game
import time
import random as r
import numpy as np
import matplotlib.pyplot as plt

popolation = []
for i in range(30):
	popolation.append(net.Network([5, 5, 1], weights_path=f"Saves_little/save_{i}.txt"))

def log_change(best_five):
	vectors = []

	for i, j in zip(np.logspace(-5, -2, 4), range(len(best_five))):
		vectors.append(best_five[j]+(np.random.uniform(-0.1, 0.1, len(best_five[j]))*i*best_five[j]))

	for _ in range(5):
		vectors.append(np.random.uniform(-1, 1, len(best_five[0])))

	for i in range(len(best_fives)):
		vectors.append(best_fives[i])

	return np.array(vectors)	

best = 0
#a = net.Network([2, 3, 2], weights_path="best.txt")
epochs = 1

std_all = []
mean_all = []

for epoch in range(epochs):
	hits = []
	hits_gen = []
	print(epoch)
	for genome in range(30):
		mean = []	
		for _ in range(5):	
			hit = 0
			init = True
			while True:
				vis=False
				#if (epoch%5)==0 and epoch != 0:vis=True
				#if genome==11: vis = True
				if init: up, down = False, False
				flag, dx, dy, ball_y, ball_dx, ball_dy, hit = game(up, down, hit, vis)
				up = popolation[genome].forward_propagation([dx, dy, ball_y, ball_dx, ball_dy])>0.5
				down = not up
				init = False
				if(flag or hit>25): break
			#print(f"Gene : {genome}, Hits : {hit}")
			mean.append(hit)
		hits_gen.append(mean)
		hits.append(np.mean(mean))
	#training
	_sorted = np.argsort(hits)
	best = popolation[_sorted[len(_sorted)-1]]
	print(f"Hits : {[hits[x] for x in _sorted[len(_sorted)-5:]]}")
	best_fives = [popolation[x] for x in _sorted[len(hits)-5:]]
	best_fives = [x.export() for x in best_fives]
	hits_gen = np.array(hits_gen)
	mean_all.append(np.mean(hits_gen[_sorted[len(_sorted)-10:]][:]))
	std_all.append(np.std(hits_gen[_sorted[len(_sorted)-10:]][:]))
	changed = log_change(best_fives)
	for i, c in enumerate(changed):
		popolation[i]._import(c)

std_all = np.array(std_all)
mean_all = np.array(mean_all)

std_all.tofile("std_little.txt", sep=" ")
mean_all.tofile("mean_little.txt", sep=" ")

for i, c in enumerate(popolation):	
	c.export().tofile(f"Saves_little/save_{i}.txt", sep=" ")
best.export().tofile("Saves_little/best.txt", sep=" ")

if True:
	input('START GAME')
	init=True
	vis = True
	player = True
	while True:
		if init: up, down = False, False
		_, dx, dy, ball_y, ball_dx, ball_dy, _ = game(up, down, 0, vis, player)
		up = best.forward_propagation([dx, dy, ball_y, ball_dx, ball_dy])>0.5
		down = not up
		init = False
	


