
from random import  randint

import numpy as np
from Perceptron import Perceptron


class Sigmoid(Perceptron):
    def __init__(self, *, pesos=None, b=None, num=None):
        super().__init__(pesos=pesos, b=b, num=num)

    def feed(self, inputs):
        assert len(self.pesos) == len(inputs)

        equation = 0
        for i in range(0, len(inputs)):
            equation += inputs[i] * self.pesos[i]
        equation = equation + self.b
        sigma = 1 / (1 + np.exp(-equation))

        return sigma


def trainingCurve(red, inputs, outputs, trainingrate):
    for i in range(0, trainingrate):
        # Training the perceptron
        for h in range(0, len(inputs)):
            x = randint(0, len(inputs)-1 )
            red.training(inputs[x], outputs[x])

    return red


class logicGates():
    def __init__(self, red):
        self.red = red

    def feed(self, inputs):
        r = self.red.feed(inputs)
        if r > 0.5:
            return 1
        return 0


class And(logicGates):
    def __init__(self, red):
        super().__init__(red)
        inputs = [[0, 1], [1, 0], [0, 0], [1, 1]]
        outputs = [0, 0, 0, 1]
        trainingCurve(self.red, inputs, outputs, 1000)


class Or(logicGates):
    def __init__(self, red):
        super().__init__(red)
        inputs = [[0, 1], [1, 0], [0, 0], [1, 1]]
        outputs = [1, 1, 0, 1]
        trainingCurve(self.red, inputs, outputs, 1000)


class NanD(logicGates):
    def __init__(self, red):
        super().__init__(red)
        inputs = [[0, 1], [1, 0], [0, 0], [1, 1]]
        outputs = [1, 1, 1, 0]
        trainingCurve(self.red, inputs, outputs, 1000)


if __name__ == "__main__":
    sigmoid = Sigmoid(num=2)
    And = And(sigmoid)
    print(And.feed([1, 1]))
    Or = Or(sigmoid)
    print(Or.feed([0, 1]))
    Nand = NanD(sigmoid)
    print(Nand.feed([1, 1]))