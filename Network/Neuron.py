from random import uniform, random

import numpy as np


class Neuron:
    def __init__(self, *, weights=None, b=None, num=None):
        self.weights = []
        if num == None:
            self.weights = weights
            self.bias = b
        else:
            for i in range(0, num):
                self.weights.append(uniform(-2, 2))
            self.bias = random()
        self.delta = 0
        self.output = 0
        self.lastinputs = []
        self.error = 0

    def feed(self, inputs):

        assert len(self.weights) == len(inputs)
        self.lastinputs = inputs
        equation = 0
        for i in range(0, len(inputs)):
            equation += inputs[i] * self.weights[i]
        equation += self.bias
        sigma = 1 / (1 + np.exp(-equation))
        self.updateOutput(sigma)
        return sigma

    def updateOutput(self, newoutput):
        self.output = newoutput

    def getDelta(self):
        return self.delta

    def getWeighti(self, i):
        return self.weights[i]

    def getOutput(self):
        return self.output

    def updatelastlayerDelta(self, output):
        self.delta = self.error * self.transferDerivate(output)

    def updateDelta(self, error):
        self.delta = error * self.transferDerivate(self.output)


    def transferDerivate(self, output):
        return output * (1 - output)

    def update(self, lr):
        for i in range(len(self.weights)):
            self.weights[i] += lr * self.getDelta() * self.lastinputs[i]
        self.bias += lr * self.getDelta()

    def updatelastlayererror(self, desiredOutput):
        self.error = desiredOutput - self.output


