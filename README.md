# Neural-Network

This is me learning about deep learnign, what artificial neurons are how they form layers and process data.
In this i will explain all my thoughts by relating them to a model trained to classify images.

<h4>current understanding:</h4>a neural network is a combination or layers made of neurons, these layers can be arranged in a sequential manner i.e one after another.

<p></p>git commitHow does it work? well look at it as many different layers of switches and a combination of some switches turned on in a layer guides the next layers switches to turn on and so on, as a result in the output layer the correct switch shall to give desired output turn on if it makes sense. 
<p></p>we use a bias value which tells us if turning on that switch will make a difference or not in the context of image classification bias will tell if the pixels marked important by this neuron are worth considering or not.
<p></p>Now instead of having only on and off values that are 0 and 1 out activation value can be anything thus an activation function is required to convert it into sizable value, for making it easy to learn i am going to use ReLU function which is max(0,val) meaning if value is negative it is converted into 0 and if it is positive it remains unchanged.
<h4>What exactly is a artificial neuron, weights and biases:</h4>
An artificial neuron is just a processing using that contains the information of weights and bises. 
<b>Weight</b>  is a unit that tells us how important or significant a pixel is in that image. Each neuron is initialized with n number of random weights for n number of inputs, these weights are further optimized.
<p></p>
<b>Bias</b> Each neuron also has a bias value attached to it which tells us how significant that neuron's activation value is, this is also optimized in the training process. we initialize all biases as 0 or a very small value making everthing significant.

<h4>What are layers</h4>
layers are group of neurons arranges in a specific manner, for this study i am only focusing on sequential models in which layers are connected in a chain, so if a model has 3 layers it will all be connected in a single chain like Layer1->Layer2->Layer3. Next is what each layer passes to the next layer, it is simple: it passes an array of all activation values from previous layers as an input to each neuron in next layer. 
<p></p>Each layer can have its own different activation function which it applies to the weighted sum given by neurons, i dont't know what other functions are there and what are they used for but i know we use softMax function for classification which essentially calculates probablities, and i am going to use it in future to classify images.

<h4>currently working on:</h4> Learn and adding back propogation to it. Back propogation is the backbone of neural network and what enables this collection of mathematical functions "learn" by calculating cost/loss and adjusting weights and biases.

<h4>current goal:</h4> This should be able to train and classify images using mnist data("hello world of machine learning")
