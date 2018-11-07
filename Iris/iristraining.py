from sklearn.model_selection import *
from sklearn.preprocessing import minmax_scale
import numpy
import matplotlib.pyplot as plt
from NeuralNetwork import NeuralNetwork


class Iris:
    def irisTraining(self, dtname, ntrainings):
        # MANEJO DE DATOS
        print("comienza carga de datos")
        dt = numpy.loadtxt(dtname, delimiter=",")  # Cargamos el dataset csv
        print("Comienza edición de datos")
        sh = dt.shape
        largo = sh[0]
        ancho = sh[1]
        X = dt[:, 0:ancho - 1]
        X_norm = minmax_scale(X)
        output = dt[:, ancho - 1]
        X_train, X_test, output_train, output_test = train_test_split(X_norm, output, test_size=0.33,
                                                                      random_state=27)  # Separamos los datos en train/test
        print("Fin ajuste de datos")
        print("Creacion de red neuronal")

        red = NeuralNetwork(4, (4, 5, 3))
        final = []
        trainingInputs = []
        trainingOutputs = []
        print(ntrainings)

        for i in range(0, ntrainings):
            trainingInputs.append(X_train)
            trainingOutputs.append(output_train)
        # red.realTraining(X_train, output_train)

        trainings = list(range(0, ntrainings, 100))
        print(trainings)
        for i in range(0, len(trainings)):
            # entrenar al perceptron
            for j in range(0, trainings[i]):
                red.realTraining(trainingInputs[j], trainingOutputs[j])
            redanswers = []
            expected = []
            aciertos = 0
            # Conseguir las respuestas del perceptron entrenado
            for k in range(0, len(X_test)):
                an=red.feed(X_test[k])
                normalized_an=[0,0,0]
                for n in range (len(an)):
                    if an[n] < 0.5:
                        normalized_an= 0
                    else:
                        normalized_an= 1

                redanswers.append(normalized_an)
                print("redanwers")
                print(redanswers)
                print(red.feed(X_test[k]))
                # Conseguir las respuestas esperadas
                expected.append(output_test[k])
                a=0
                for n in range (len(redanswers[n])):
                    if redanswers[k][n] == expected[k][n]:
                        a=1
                    else: a=0
                if a:
                    aciertos += 1
            aciertos = aciertos / len(X_test)
            final.append(aciertos)

        print("fin del loop")
        plt.plot(trainings, final)
        plt.ylim((0, 2))
        plt.ylabel("Porcentaje de aciertos")
        plt.xlabel("# Entrenamientos")
        plt.title("Learning Curve")
        plt.show()


if __name__ == "__main__":
    iris = Iris()
    iris.irisTraining("iris.data.csv", 1100)
    # grafics = Grafics()
    # grafics.plotear()
