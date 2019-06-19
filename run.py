import net
from pong import game
import time
import random as r
import numpy as np

popolation = []
for i in range(30):
	popolation.append(net.Network([5, 5, 2, 1], weights_path=f"Saves/save_{i}.txt"))

def log_change(best_five):
	vectors = []

	for i, j in zip(np.logspace(-5, -2, 4), range(len(best_five))):
		vectors.append(best_five[j]+(np.random.random(len(best_five[j]))*i*best_five[j]))

	for _ in range(5):
		vectors.append(np.random.uniform(-1, 1, len(best_five[0])))

	for i in range(len(best_fives)):
		vectors.append(best_fives[i])

	return np.array(vectors)	

best = 0

#a = net.Network([2, 3, 2], weights_path="best.txt")
epochs = 50
for epoch in range(epochs):
	hits = []
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
				if(flag or hit>35): break
			#print(f"Gene : {genome}, Hits : {hit}")
			mean.append(hit)
		hits.append(np.mean(mean))
	_sorted = np.argsort(hits)
	best = popolation[_sorted[len(_sorted)-1]]
	#print([hits[x] for x in _sorted])
	#print(_sorted)
	#print(_sorted[len(_sorted)-1])
	print(f"Hits : {[hits[x] for x in _sorted[len(hits)-5:]]}, Mean : {np.mean([hits[x] for x in _sorted])}, Std : {np.std([hits[x] for x in _sorted])}")
	best_fives = [popolation[x] for x in _sorted[len(hits)-5:]]
	best_fives = [x.export() for x in best_fives]
	changed = log_change(best_fives)
	for i, c in enumerate(changed):
		popolation[i]._import(c)

for i, c in enumerate(popolation):	
	c.export().tofile(f"Saves_temp/save_{i}.txt", sep=" ")
best.export().tofile("Saves_temp/best.txt", sep=" ")


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
	


