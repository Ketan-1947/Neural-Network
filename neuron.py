import numpy as np
import random

class neuron:
    def __init__(self , n):
        self.weights = [random.uniform(-1,1) for i in range(n)]
        self.bias = 0
    
    def modifyParams(self, weights , bias):
        self.weights = weights
        self.bias = bias
    
class layer:
    def __init__(self, n_neurons , input_size = 0):
        self.neurons =[]
        self.weightsVector = []
        self.biases = []

        self.neuron_count = n_neurons
        self.inputSize = input_size

    def generateNeurons(self , input = 0):
        if input == 0:
            input = self.inputSize
        
        for i in range(self.neuron_count):
            n = neuron(input)

            self.weightsVector.append(n.weights)
            self.biases.append(n.bias)

        self.neurons = np.array(self.neurons)
        self.weightsVector = np.array(self.weightsVector)
        self.biases = np.array(self.biases)

    def activationValue(self , input):
        input = np.array(input).reshape((-1))
        
        weightedSum = np.dot(self.weightsVector, input)+self.biases
        activation_value = np.maximum(0,weightedSum)

        return activation_value

    

class model:
    def __init__(self):
        self.layers = []
        self.activation_for_each_input = []
        self.losses_for_each_input = []

    def add(self , layer):
        
        if layer in self.layers:
            print("already added")
            return
        if len(self.layers) == 0:
            print("adding first layer")
            if layer.inputSize == 0:
                print("give input size")
                return
            layer.generateNeurons()
            self.layers.append(layer)
        
        else:
            print("adding")
            last_layer = self.layers[-1]
            size = last_layer.neuron_count
            layer.generateNeurons(size)
            self.layers.append(layer)


    def fit(self,X,y, epochs = 5):

        if len(self.layers) == 0:
            return "no layers"

        for input in X:
            activation_value = input
            for layer in self.layers:
                activation_value = layer.activationValue(activation_value)
                # print(activation_value)

            self.activation_for_each_input.append(activation_value)
            self.losses_for_each_input.append(self.Cost(activation_value , y))
        
        return self.activation_for_each_input
    
    def Cost(self , values , targets):
        loss = np.mean((values-targets)**2)
        
        return loss
    
m = model()
layer1 = layer(20,10)
layer2 = layer(10)
layer3 = layer(5)

m.add(layer1)
m.add(layer2)
m.add(layer3)

ans = m.fit(np.random.random(size = (30,10)),[0,0,0,1,0])
loss = m.losses_for_each_input
print(len(loss))

