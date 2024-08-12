import numpy as np
import random

class neuron:
    def __init__(self , n):
        self.weights = np.random.rand(n)*random.uniform(-1,1)
        self.bias = np.random.random()
    
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
        activation_value = [max(0,val) for val in weightedSum]

        return activation_value

    

class model:
    def __init__(self):
        self.layers = []

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
        
        activation_for_each_input = []

        for input in X:
            activation_value = input
            for layer in self.layers:
                activation_value = layer.activationValue(activation_value)
                print(activation_value)

            activation_for_each_input.append(activation_value)
        return activation_for_each_input
    
    def Loss(self , values , targets):
        loss = 0
        for value,target in zip(values,targets):
            loss += (value-target)**2
        
        return loss
    
m = model()
layer1 = layer(20,10)
layer2 = layer(10)
layer3 = layer(5)

m.add(layer1)
m.add(layer2)
m.add(layer3)

ans = m.fit([[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0]],[0,0,0,1,0,0,0,0,0,0])

print(ans)

