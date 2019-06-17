import numpy as np

np.random.seed(5)

def sigmoid(x):
	out = 1 / (1+np.exp(-x))
	return out

class Network(object):
	def __init__(self, shape, variation=3, gen=50):
		self.shape = shape

		self.weights = []
		for i in range(len(self.shape)-1):
			self.weights.append(np.random.random_sample((self.shape[i], self.shape[i+1])))

		self.bias = []
		for i in range(len(self.shape)-1):
			self.bias.append(np.random.random_sample(self.shape[i+1]))

		self.layers = []
		for i in range(len(self.shape)):
			self.layers.append(np.zeros(self.shape[i]))

	def forward_propagation(self, inputs):
		self.layers[0] = inputs
		for i in range(len(self.shape)-1):
			self.layers[i+1] = np.dot(self.layers[i], self.weights[i])
			self.layers[i+1] = self.layers[i+1] + self.bias[i]
			self.layers[i+1] = sigmoid(self.layers[i+1])

		return self.layers[len(self.layers)-1]

