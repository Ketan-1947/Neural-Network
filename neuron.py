import numpy as np
import math
import random
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder,normalize

class neuron:
    def __init__(self , n):
        self.weights = np.random.randn(n) * 0.01  # Small random values
        self.bias = 0.0 
    
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
        
        weighted_sum = np.dot(self.weightsVector, input)+self.biases
        activationValue = np.maximum(0,weighted_sum)

        return (weighted_sum , activationValue)

    

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

        for i in range(epochs):
            for input,output in zip(X,y):
                activation_value = input
                weighted_sums = []
                activation_values = []
                inputs = []
                for layer in self.layers:
                    inputs.append(activation_value)
                    weighted_sum , activation_value = layer.activationValue(activation_value)
                    weighted_sums.append(weighted_sum)
                    activation_values.append(activation_value)

                self.backProp(weighted_sums , activation_values , inputs ,output)
            

    
    def backProp(self , z_i , a_i , inputs, target):
        learnRate = 0.01
        z_i = z_i[::-1]
        a_i =  a_i[::-1]
        layers =  self.layers[::-1]
        inputs =  inputs[::-1]
        delta = 0

        for z,a,layer,input in zip(z_i , a_i , layers , inputs):
            if type(delta) == int:
                delta =  2*np.array(a)-np.array(target)
                relu_derivative = np.where(z > 0, 1, 0)
                delta *= relu_derivative
            

            gradient_w = np.outer(delta, input)
            gradient_b = delta

            # updating weights and biases
            layer.weightsVector -= learnRate * gradient_w
            layer.biases -= learnRate * gradient_b

            delta = np.dot(layer.weightsVector.T, delta)


    def predict(self, X):
        if(len(X.shape) != 2):
            return "Improper shape"
        predictions = []
        for input in X:
            activation_value = input
            for layer in self.layers:
                w ,activation_value = layer.activationValue(activation_value)
            predictions.append(activation_value)

        return predictions
            


    
m = model()
layer1 = layer(20 , 784)
layer2 = layer(16)
layer3 = layer(10)

m.add(layer1)
m.add(layer2)
m.add(layer3)

data = np.load("mnist.npy")
X,y = data[: , 1:] , data[:,0].reshape(-1,1)
X = normalize(X)

encoder = OneHotEncoder(sparse_output = False)
y = encoder.fit_transform(y)

X_train , y_train , X_test , y_test = X[:17000] , y[:17000] , X[17000:] , y[17000:]

m.fit(X_train,y_train ,epochs=10)

preds = m.predict(X_test[0:20])
for pred in preds:
    print(np.argmax(pred))

print([np.argmax(np.array(i)) for i in y_test[0:20]])

