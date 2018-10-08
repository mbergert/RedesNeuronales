from cmath import exp
import numpy as np
from Perceptron import Perceptron


class Sigmoid(Perceptron):
    def __init__(self, pesos, b):
        super().__init__(pesos, b)

    def feed(self, inputs):
        assert len(self.pesos) == len(inputs)

        equation = 0
        for i in range(0, len(inputs)):
            equation += inputs[i] * self.pesos[i]
        equation = equation + self.b
        sigma = 1/ (1 + exp(-equation))

        if np.real(sigma) > 0.5:
            return 1
        return 0

class And(Sigmoid):
    def __init__(self):
        super().__init__([1, 1], -1.5)

class Or(Sigmoid):
    def __init__(self):
        super().__init__([1, 1], -0.5)

class NanD(Sigmoid):
    def __init__(self):
        super().__init__([-2, -2], 3)

if __name__ == "__main__":

    suma = Or()
    print(suma.feed([0, 1]))