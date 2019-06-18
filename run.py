import net
from pong import game
import time
import random as r
import numpy as np

popolation = []
for _ in range(30):
	popolation.append(net.Network([2, 5, 2]))

def log_change(best_five):
	vectors = []

	for i, j in zip(np.logspace(-5, -2, 4), range(len(best_five))):
		vectors.append(best_five[j]+(np.random.random(len(best_five[j]))*i*best_five[j]))

	for _ in range(len(best_fives)):
		vectors.append(np.random.uniform(-0.5, 0.5, len(best_five[0])))

	for i in range(len(best_fives)):
		vectors.append(best_fives[i])

	return np.array(vectors)	

best = 0

for epoch in range(50):
	hits = []
	print(epoch)
	for genome in range(30):
		hit = 0
		init = True
		while True:
			vis=False
			#if (epoch%25)==0 and epoch != 0:vis=True
			if init: up, down = False, False
			flag, dx, dy, hit = game(up, down, hit, vis)
			up, down = popolation[genome].forward_propagation([dx, dy])>0.5
			init = False
			if(flag or hit>10): break
		#print(f"Gene : {genome}, Hits : {hit}")
		hits.append(hit)
	####training
	_sorted = np.argsort(hits)
	best = popolation[_sorted[len(_sorted)-1]]
	#print([hits[x] for x in _sorted])
	#print([hits[x] for x in _sorted[len(hits)-3:]])
	best_fives = [popolation[x] for x in _sorted[len(hits)-5:]]
	best_fives = [x.export() for x in best_fives]
	changed = log_change(best_fives)
	for i, c in enumerate(changed):
		popolation[i]._import(c)

input('START GAME')

init=True
while True:
	if init: up, down = False, False
	_, dx, dy, _ = game(up, down, hit, visualize=True, player=True)
	up, down = best.forward_propagation([dx, dy])>0.5
	init = False
	


