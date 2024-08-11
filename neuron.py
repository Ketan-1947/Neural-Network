import numpy as np

class neuron:
    def __init__(self , n):
        self.weights = np.random.rand(n)*4
        self.bias = np.random.randint(10)

    def weightedSum(self , inputs):
        z_i = np.dot(inputs , self.weights)
        
        return z_i+self.bias
    
    def modifyParams(self, weights , bias):
        self.weights = weights
        self.bias = bias
    
class layer:
    def __init__(self, n_neurons , input_size = 0):
        self.neurons =[]
        self.neuron_count = n_neurons
        self.inputSize = input_size

    def generateNeurons(self , input = 0):
        if input == 0:
            input = self.inputSize
        
        for i in range(self.neuron_count):
            n = neuron(input)
            self.neurons.append(n)

    def activationValue(self , input):
        activeValues = []
        
        for neuron in self.neurons:
            activation_value = max(0,neuron.weightedSum(input))
            activeValues.append(activation_value)

        return activeValues

    

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


    def fit(self,inputs):

        if len(self.layers) == 0:
            return "no layers"
        
        activation_for_each_input = []

        for input in inputs:
            activation_value = input
            for layer in self.layers:
                activation_value = layer.activationValue(activation_value)

            activation_for_each_input.append(activation_value)

        return activation_for_each_input
    
m = model()
layer1 = layer(20,10)
layer2 = layer(10)
layer3 = layer(5)

m.add(layer1)
m.add(layer2)
m.add(layer3)

ans = m.fit([[1,2,3,4,5,6,7,8,9,0],[0,9,1,2,3,4,5,6,7,8]])

print(ans)

