


class NeuralNetwork:
    def __init__(self, layers):
        self.layers=layers
        self.learningrate=0.5
        self.output=0


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
            ''''
            #|for j in range(0,len(self.layers[i].neurons)):
                #Conseguir el peso #numero de la neurona# de cada neurona de la layer i+1
                weights= self.layers[i+1].getWeightsi(j)
                #Conseguir todos los deltas de las neuronas de la layer n+1
                deltas= self.layers[i+1].getDeltas()
                #error= la suma de la multiplicación de los puntos anteriores
                error=0
                for i in range(0,len(deltas)):
                    error+= weights[i]*deltas[i]
                self.layers[i].backpropagation(error)'''
        #PASO 3
        #"weightN = weightN + (learningRate * delta * inputN)
        #bias = bias + (learningRate * delta)
        for i in range(0, len(self.layers)):
            self.layers[i].updateWeights()
    #def backPropagation(self,expectedOutput):

