from random import random, uniform
import matplotlib.pyplot as plt

from Perceptron import Perceptron


class LearningCurve:
    def __init__(self, inputs, outputs, epoch):
        self.inputs = inputs
        self.outputs = outputs
        self.epoch=epoch


        # Create the perceptron
        self.randomweights = [uniform(-2, 2), uniform(-2, 2)]
        self.bias = random()
        self.perceptron = Perceptron(self.randomweights, self.bias)

    def learningCurve(self):

        final = []
        for i in range(0, self.epoch):
            # Training the perceptron

            for h in range(0,len(inputs)):
                self.perceptron.training(self.inputs[h], self.outputs[h])
            perceptronanswers = []

            aciertos = 0

            testingset= []
            testingoutputs=[]
            for i in range(0,100):
                random= int(uniform(0,3))
                testingset.append(self.inputs[random])
                testingoutputs.append(self.outputs[random])

            print(testingset)
            for i in range(0, len(testingset)):
                perceptronanswers.append(self.perceptron.feed(testingset[i]))
                if perceptronanswers[i] == testingoutputs[i]:
                    aciertos += 1
            aciertos = aciertos / len(testingset)
            final.append(aciertos)

        plt.plot(range(0,self.epoch), final)
        plt.ylim((0, 1))
        plt.show()


if __name__ == "__main__":
    inputs = [[0, 1], [1, 0], [0, 0], [1, 1]]
    outputs = [1, 1, 0, 0]
    grafics = LearningCurve(inputs, outputs, 100)

    grafics.learningCurve()
