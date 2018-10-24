from Network.Neuron import Neuron


class NeuronLayer:
    def __init__(self, nInputs, nNeurons):
        self.neurons = []
        self.layeroutput = []

        for i in range(nNeurons):
            neur=Neuron(nInputs)
            self.neurons.append(neur)

    def feed(self, inputs):
        self.layeroutput=[]
        for neuron in self.neurons:
            output = neuron.feed(inputs)
            self.layeroutput.append(output)
        return self.layeroutput


    def getWeightsi(self, i):
        weightsi = []
        for neuron in self.neurons:
            w = neuron.getWeighti(i)
            weightsi.append(w)
        return weightsi

    def backpropagation(self, error):
        for neuron in self.neurons:
            neuron.updateDelta(error)

    '''def updateWeights(self, learningRate):
        for neuron in self.neurons:
            neuron.updateWeight(learningRate.)
        '''
    def setUpLayer(self, nextlayer):
        error=0
        for i in range(len(self.neurons)):
            for j in range(len(nextlayer.getNeurons())):
                error+= nextlayer.getNeurons()[j].getweighti(i)*nextlayer.getNeurons()[j].getDelta()
            self.neurons[i].updateDelta(error)
            error=0

    def getNeurons(self):
        return self.neurons

    def update(self,lr):
        for neuron in self.neurons:
            neuron.update(lr)