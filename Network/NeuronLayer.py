from pip._internal.utils.misc import enum


class NeuronLayer:
    def __init__(self, neurons):
        self.neurons=neurons
        self.layeroutput=[]
        self.deltas=[]


    def feed(self, inputs):

        for neuron in self.neurons:
            output=neuron.feed(inputs)
            self.layeroutput.append(output)
        return self.layeroutput

    def getDeltas(self):
        for neuron in self.neurons:
            self.deltas.append(neuron.getDelta())

        return self.deltas
    def getWeightsi(self, i):
        weightsi=[]
        for neuron in self.neurons:
            w=neuron.getWeighti(i)
            weightsi.append(w)
        return weightsi

    def backpropagation(self, error):
        for neuron in self.neurons:
            neuron.updateDelta(error* neuron.getOutput(1.0 - neuron.getOutput()))




