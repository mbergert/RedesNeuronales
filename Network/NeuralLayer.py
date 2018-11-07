from Network.Neuron import Neuron


class NeuralLayer:
    def __init__(self, nInputs, nNeurons):
        self.neurons = []
        self.layeroutput = []

        for i in range(nNeurons):
            neur = Neuron(num=nInputs)
            self.neurons.append(neur)

    def feed(self, inputs):
        out = []
        for neuron in self.neurons:
            output = neuron.feed(inputs)
            out.append(output)
        self.layeroutput=out

        return self.layeroutput

    def getWeightsi(self, i):
        weightsi = []
        for neuron in self.neurons:
            w = neuron.getWeighti(i)
            weightsi.append(w)
        return weightsi

    def setUpLastLayer(self, output):
        for i in range(0,len(self.neurons)):
            self.neurons[i].updatelastlayererror(self.neurons[i].output)
            self.neurons[i].updatelastlayerDelta(self.layeroutput[i])


    def setUpLayer(self, nextlayer):
        error = 0
        for i in range(len(self.neurons)):
            for j in range(len(nextlayer.getNeurons())):
                error += nextlayer.getNeurons()[j].getWeighti(i) * nextlayer.getNeurons()[j].getDelta()
            self.neurons[i].updateDelta(error)
            error = 0

    def getNeurons(self):
        return self.neurons

    def update(self, lr):
        for neuron in self.neurons:
            neuron.update(lr)
