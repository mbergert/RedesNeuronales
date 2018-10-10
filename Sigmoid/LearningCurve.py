from random import random, uniform, randint
import matplotlib.pyplot as plt
from Sigmoid import Sigmoid


class LearningCurve(Sigmoid):
    def __init__(self, inputs, outputs, epoch):
        self.inputs = inputs
        self.outputs = outputs
        self.epoch = epoch
        # Create the Sigmoid
        self.randomweights = [uniform(-2, 2), uniform(-2, 2)]

        self.bias = random()
        self.sigmoid = Sigmoid(pesos=self.randomweights, b=self.bias)


    def learningCurve(self):

        final = []
        for i in range(0, self.epoch):
            # Training the perceptron

            for h in range(0, len(inputs)):
                x = randint(0, len(self.inputs) - 1)
                self.sigmoid.training(self.inputs[x], self.outputs[x])
            perceptronanswers = []

            aciertos = 0

            testingset = []
            testingoutputs = []
            for i in range(0, 100):
                random = randint(0, len(self.inputs) - 1)
                testingset.append(self.inputs[random])
                testingoutputs.append(self.outputs[random])
            for i in range(0, len(testingset)):
                perceptronanswers.append(self.sigmoid.feed(testingset[i]))
                if perceptronanswers[i]>0.5:
                    perceptronanswers[i]=1
                else:
                    perceptronanswers[i]=0
                if perceptronanswers[i] == testingoutputs[i]:
                    aciertos += 1
            aciertos = aciertos / len(testingset)

            final.append(aciertos)
        plt.plot(range(0, self.epoch), final)
        plt.ylim((0, 1))
        plt.ylabel("Porcentaje de aciertos")
        plt.xlabel("# Entrenamientos")
        plt.title("Sigmoid Learning Curve")
        plt.show()


if __name__ == "__main__":
    inputs = [[0, 1], [1, 0], [0, 0], [1, 1]]
    outputs = [1, 1, 0, 0]
    grafics = LearningCurve(inputs, outputs, 100)

    grafics.learningCurve()
