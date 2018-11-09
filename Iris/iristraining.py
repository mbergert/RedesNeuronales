import time

from sklearn.model_selection import *
from sklearn.preprocessing import minmax_scale
import numpy
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

from NeuralNetwork import NeuralNetwork


class Iris:
    def irisTraining(self, dtname, ntrainings):
        # MANEJO DE DATOS
        print("comienza carga de datos")
        dt = numpy.loadtxt(dtname, delimiter=",")  # Cargamos el dataset csv
        print("Comienza edición de datos")
        dt = shuffle(dt)
        X = dt[:, 0:4]
        X_norm = minmax_scale(X)

        output = dt[:, 4:]

        X_train, X_test, output_train, output_test = train_test_split(X_norm, output, test_size=0.33,
                                                                      random_state=27)  # Separamos los datos en train/test

        "Cambiar los testing outputs"
        print("Fin ajuste de datos")

        print("Creacion de red neuronal")

        # Creacion de la red
        red = NeuralNetwork(4, (4,5,3), 0.5)
        finalaciertos = []
        finalerrores = []
        trainingInputs = []
        trainingOutputs = []

        this_time=0
        # Cargar un gran set de inputs para entrenar
        for i in range(0, ntrainings):
            trainingInputs.append(X_train)
            trainingOutputs.append(output_train)

        trainings = list(range(0, ntrainings, 100))
        trainingInputs, trainingOutputs = shuffle(trainingInputs, trainingOutputs)
        # inicio de los loops

        initial_time = time.time()
        print("initial time", format(initial_time))
        for i in range(0, len(trainings)):
            looping_time= time.time()
            print("Tiempo al inicio del loop")
            # entrenar a la red
            print("entrenando la red para", format(trainings[i]))
            # entrenar
            last_time= initial_time + this_time
            for j in range(0, trainings[i]):

                red.realTraining(trainingInputs[j], trainingOutputs[j])
            redanswers = []
            unnormalized_answers = []
            expected = []
            aciertos = 0
            errores = 0
            # Conseguir las respuestas del perceptron entrenado
            print("feed")
            for k in range(0, len(X_test)):
                an = red.feed(X_test[k])
                normalized_an = [0, 0, 0]
                for n in range(len(an)):

                    if an[n] < 0.5:
                        normalized_an[n] = 0
                    else:
                        normalized_an[n] = 1

                unnormalized_answers.append(an)
                redanswers.append(normalized_an)
                expected.append(output_test[k])
                a = 0
                e = 0
                for n in range(len(redanswers[k])):
                    if redanswers[k][n] == expected[k][n]:
                        a = a + 1
                    e = e + (expected[k][n] - unnormalized_answers[k][n]) ** 2

                aciertos = aciertos + a / 3
                errores = e + errores
            aciertos = float(aciertos) / len(X_test)

            print("Entrenar", format(trainings[i]),"veces, tomo", (time.time()- looping_time))
            finalaciertos.append(aciertos)
            finalerrores.append(errores)

        print("fin del loop")
        plt.plot(trainings, finalaciertos)
        plt.ylim((0, 1))
        plt.ylabel("Porcentaje de aciertos")
        plt.xlabel("# Entrenamientos")
        plt.title("Learning Curve")
        plt.show()

        plt.plot(trainings, finalerrores, 'r-')

        plt.ylabel("Errores")
        plt.xlabel("# Entrenamientos")
        plt.title("Curva de errores")
        plt.show()

        print(red.lr)

if __name__ == "__main__":
    iris = Iris()
    iris.irisTraining("iris.data.csv", 600)
