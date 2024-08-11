# Neural-Network
This is me learning about deep learnign, what artificial neurons are how they form layers and process data.

current progress:
<ol>
    <li>created a basic neuron that when initialized for n number of inputs generate n random weights and a single bias.</li>
    <li>added layer class wich initiaolzes a layer consisting of n neurons that can process x amount of inputs.
        <ul>
            <li>added dynamic nature to the neuron initiaolzation thus only first layer need to be specified with the input size</li>
        </ul>
   <li>a model class is added with followinf methods:
        <ul>
            <li>add(): it connects each layer to another in the model</li>
            <li>fit(): it fits the input data into the model to get exactly one forward propogation</li>
        </ul>
</ol>

<h3>currently working on:</h3> Learn and adding back propogation to it.

<h3>current goal:</h3> This should be able to train and classify images using mnist data("hello world of machine learning")
