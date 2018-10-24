from Network.NeuronLayer import NeuronLayer


class NeuralNetwork:
    def __init__(self, nInputs, neurperLayers):
        self.layers=[]

        self.lr=0.5
        self.output=0
        Inputs=nInputs
        for i in range(len(neurperLayers)):
            layer= NeuronLayer(nInputs, neurperLayers[i])
            self.layers.append(layer)
            Inputs= neurperLayers[i]


    def feed(self, inputs):
        output= self.layers[0].feed(inputs)
        for l in range(1, len(self.layers)):
            output= self.layers[l].feed(output)
        self.output=output
        return output


    def train(self, inputs, desiredOutputs):
        flayer=0
        nlayer= len(self.layers)-1
        # paso 1
        networkOutput= self.feed(inputs)
        #Inicio Backpropagation
        error= desiredOutputs-networkOutput
        #Inicio en layers
        self.layers[nlayer].backpropagation(error)
        #Training del resto

        for i in range(nlayer-1,flayer-1, -1):
            self.layers[i].setUpLayer(self.layers[i+1])
        #PASO 3
        #"weightN = weightN + (learningRate * delta * inputN)
        #bias = bias + (learningRate * delta)
        for i in range(0, len(self.layers)):
            self.layers[i].update(self.lr)

    #def backPropagation(self,expectedOutput):

