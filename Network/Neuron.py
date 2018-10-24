from random import uniform, random

import numpy as np

from Sigmoid import Sigmoid


class Neuron():
    def __init__(self, *, pesos=None, b=None, num=None):
        self.pesos = []
        if num == None:
            self.pesos = pesos
            self.b = b
        else:
            for i in range(0, num):
                self.pesos.append(uniform(-2, 2))
            self.b = random()
        self.delta=1
        self.output=1

    def feed(self, inputs):
        assert len(self.pesos) == len(inputs)

        equation = 0
        for i in range(0, len(inputs)):
            equation += inputs[i] * self.pesos[i]
        equation = equation + self.b
        sigma = 1 / (1 + np.exp(-equation))
        self.updateOutput(sigma)
        return sigma

    def updateOutput(self, newoutput):
        self.output=newoutput

    def getDelta(self):
        return self.delta
    def getWeighti(self,i):
        return self.pesos[i]

    def getOutput(self):
        return self.output
    def updateDelta(self, error):
        self.delta= error*self.transferDerivate(self.output)

    '''def updateWeight(self, learningRate):
        weightN = weightN + (learningRate * delta * inputN)'''

    def transferDerivate(self, output):
        return output*(1-self.output)


# bias = bias + (learningRate * delta)





