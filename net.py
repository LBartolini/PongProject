import numpy as np

np.random.seed(400)

#seed 60

def sigmoid(x):
	out = 1 / (1+np.exp(-x))
	return out

class Network(object):
	def __init__(self, shape):
		self.shape = shape

		self.weights = []
		for i in range(len(self.shape)-1):
			self.weights.append(np.random.uniform(-1, 1, (self.shape[i], self.shape[i+1])))

		self.bias = []
		for i in range(len(self.shape)-1):
			self.bias.append(np.random.uniform(-1, 1, self.shape[i+1]))

		self.layers = []
		for i in range(len(self.shape)):
			self.layers.append(np.zeros(self.shape[i]))

	def forward_propagation(self, inputs):
		self.layers[0] = inputs
		for i in range(len(self.shape)-1):
			self.layers[i+1] = np.dot(self.layers[i], self.weights[i])
			self.layers[i+1] = self.layers[i+1] + (self.bias[i]/10)
			self.layers[i+1] = sigmoid(self.layers[i+1])

		return self.layers[len(self.layers)-1]

	def export(self):
		vect = []
		for layer in self.weights:
			for k in layer:
				for j in k:	
					vect.append(j)
		for i in self.bias:
			for k in i:
				vect.append(k) 

		return vect

	def _import(self, vect):
		s = 0
		for layer in range(len(self.shape)-1):
			for k in range(len(self.weights[layer])):
				for j in range(len(self.weights[layer][k])):	
					self.weights[layer][k][j] = vect[s]
					s += 1
		for i in range(len(self.shape)-1):
			for k in range(len(self.bias[i])):
				self.bias[i][k] = vect[s] 
				s += 1
		


