import net
from pong import game
import time
import random as r


network = net.Network([2, 5, 20, 3, 1, 2])
print(network.forward_propagation([0, 0]))



if False:	
	# Main game loop

	t0 = time.time()

	hits = []

	for epoch in range(100):
	    for genome in range(30):
	        hit = 0
	        while True:
	            up = r.choice([True, False])
	            down = not up
	            flag, dx, dy, hit = game(up, down, hit)
	            if(flag): break
	        hits.append(hit)

	print(time.time()-t0)
	print(hits, max(hits))