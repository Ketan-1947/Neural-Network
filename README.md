# Neural-Network
This is me learning about deep learnign, what artificial neurons are how they form layers and process data.

current progress:
1. created a basic neuron that when initialized for n number of inputs generate n random weights and a single bias.
2. added layer class wich initializes a layer consisting of n neurons that can process x amount of inputs.
   2.1 added dynamic nature to the neuron initialization thus only first layer need to be specified with the input size
3. a model class is added with followinf methods:
   3.1 add(): it connects each layer to another in the model
   3.2 fit(): it fits the input data into the model to get exactly one forward propogation

currently working on: Learn and adding back propogation to it.

current goal: This should be able to train and classify images using mnist data("hello world of machine learning")
