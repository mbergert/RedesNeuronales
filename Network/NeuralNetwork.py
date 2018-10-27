from Network.NeuralLayer import NeuralLayer


class NeuralNetwork:
    def __init__(self, nInputs, neurperLayers):
        self.layers = []
        self.lr = 0.5
        self.output = 0
        Inputs = nInputs
        for i in range(len(neurperLayers)):
            layer = NeuralLayer(Inputs, neurperLayers[i])
            self.layers.append(layer)
            Inputs = neurperLayers[i]

    def feed(self, inputs):
        output = self.layers[0].feed(inputs)
        for l in range(1, len(self.layers)):
            output = self.layers[l].feed(output)
        self.output = output
        return self.output

    def train(self, inputs, desiredOutputs):

        flayer = 0
        nlayer = len(self.layers) - 1
        # paso 1
        self.feed(inputs)
        # Inicio Backpropagation
        # Inicio en layers
        self.layers[nlayer].setUpLastLayer(desiredOutputs)
        # Training del resto

        for i in range(nlayer - 1, flayer-1, -1):
            self.layers[i].setUpLayer(self.layers[i + 1])
        # PASO 3
        for i in range(0, len(self.layers)):
            self.layers[i].update(self.lr)

    def realTraining(self, traininginputs, Desiredoutput):
        for i in range(len(traininginputs)):
            self.train(traininginputs[i], Desiredoutput[i])

    def getOutput(self):
        return self.output


