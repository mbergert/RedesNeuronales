from random import random, uniform
import matplotlib.pyplot as plt
import numpy as np

from Perceptron import Perceptron


def fun( x):
    y = 5 * x + 3
    return y


def upp(input):
    desiredy = fun(input[0])
    up = 0
    if input[1] > desiredy:
        up = 1
    return up

class Grafics:
    def __init__(self):

        self.randomweights = [uniform(-2, 2), uniform(-2, 2)]
        self.bias = random()
        self.perceptron = Perceptron(self.randomweights, self.bias)
        self.randominputsx = []
        self.randominputsy = []
        self.perceptronanswers = []
        self.up = []

        # Training the Perceptron
        for i in range(0, 1000):
            x = uniform(0, 100)
            y = uniform(0, 100)
            self.perceptron.training([x, y], upp([x, y]))

    def plotear(self):
        # Generating random set
        for i in range(0, 200):
            self.randominputsx.append(uniform(0, 100))
            self.randominputsy.append(uniform(0, 500))
            self.perceptronanswers.append(self.perceptron.feed([self.randominputsx[i], self.randominputsy[i]]))

        plt.scatter(self.randominputsx, self.randominputsy, c=self.perceptronanswers)
        x = range(0, 101)
        y = []
        for i in range(0, 101):
            y.append(fun(x[i]))
        plt.plot(x, y)
        plt.show()


class LearningCurve:
    def __init__(self):
        self.randominputsx = []
        self.randominputsy = []
        self.traininginputsx = []
        self.traininginputsy = []
        self.points = 10001

        self.randomweights = [uniform(-2, 2), uniform(-2, 2)]
        self.bias = random()
        self.perceptron = Perceptron(self.randomweights, self.bias)
        # Training points
        for i in range(0, self.points):
            x = uniform(0, 100)
            y = uniform(0, 100)
            self.traininginputsx.append(x)
            self.traininginputsy.append(y)
        # Testing points
        for i in range(0, self.points):
            self.randominputsx.append(uniform(0, 100))
            self.randominputsy.append(uniform(0, 500))

    def learningcurve(self):
        final=[]
        # Trainings
        trainings = list(range(0, 10100, 100))

        for i in range(0, len(trainings)):
            # entrenar al perceptron
            for j in range(0, trainings[i] + 1):
                self.perceptron.training([self.traininginputsx[j], self.traininginputsy[j]], upp([self.traininginputsx[j], self.traininginputsy[j]]))
            perceptronanswers = []
            expected=[]
            aciertos=0
            #Conseguir las respuestas del perceptron entrenado
            for i in range(0, self.points):
                perceptronanswers.append(self.perceptron.feed([self.randominputsx[i], self.randominputsy[i]]))
            #Conseguir las respuestas esperadas
                expected.append(upp([self.randominputsx[i],self.randominputsy[i]]))
                if perceptronanswers[i]== expected[i]:
                    aciertos+=1
            aciertos=aciertos/self.points
            final.append(aciertos)

        plt.plot(trainings, final)
        plt.ylim((0,1))
        plt.ylabel("Porcentaje de aciertos")
        plt.xlabel("# Entrenamientos")
        plt.title("Learning Curve")
        plt.show()


if __name__ == "__main__":
    grafics = LearningCurve()
    grafics.learningcurve()
