def forward_prop(self, inputs):
    print(341243)
    self.layers[0] = inputs
    for i in range(len(self.shape)-1):
        self.layers[i+1] = np.dot(self.layers[i], self.weights[i])
        self.layers[i+1] = self.layers[i+1] + (self.bias[i])
        '''
        if i != len(self.shape)-2:
            self.layers[i+1] = sigmoid(self.layers[i+1])
        else:
            self.layers[i+1] = relu(self.layers[i+1])
        '''
        self.layers[i+1] = sigmoid(self.layers[i+1])
        return self.layers[len(self.layers)-1]

print(33)