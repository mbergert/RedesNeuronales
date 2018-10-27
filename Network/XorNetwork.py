from Network.NeuralNetwork import *
from operator import xor
from random import *


class XorNetwork:
    def __init__(self,  nTrain=1000, nInputs=2, nNeurCapas=(2, 3, 1)):
        self.Network = NeuralNetwork(nInputs, nNeurCapas)
        self.Inputs = []
        self.Outputs = []
        I1 = [0, 0]
        I2 = [0, 1]
        I3 = [1, 0]
        I4 = [1, 1]
        for i in range(nTrain):
            self.Inputs.append(I1)
            self.Inputs.append(I2)
            self.Inputs.append(I3)
            self.Inputs.append(I4)
            self.Outputs.append([xor(I1[0], I1[1])])
            self.Outputs.append([xor(I2[0], I2[1])])
            self.Outputs.append([xor(I3[0], I3[1])])
            self.Outputs.append([xor(I4[0], I4[1])])
        self.Network.realTraining(self.Inputs, self.Outputs)
        self.Network.feed([0, 1])
        print(self.Network.getOutput())


XorNetwork()
