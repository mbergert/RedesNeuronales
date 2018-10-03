from random import random, uniform

from Perceptron.Perceptron import Perceptron


class Grafics:
    def __init__(self):

        self.randomweights = (uniform(-2, 2), uniform(-2, 2))
        self.bias = random()
        self.perceptron = Perceptron(self.randomweights, self.bias)
        self.randominputs = []
        for i in range(0, 1000):
            x = random(0, 100)
            y = random(0, 100)
            desiredy = self.fun(x)
            up = 0
            if y > desiredy:
                up = 1
            self.randominputs[i] = (x, y, up)
        for n in range(0, 1000):
            self.perceptron.training(list(self.randominputs[n])[:2], self.randominputs[n][2])

    def fun(self, x):
        y = 5 * x + 3
        return y
