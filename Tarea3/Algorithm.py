
from math import floor
from random import randint, random, choice
import matplotlib.pyplot as plt


from Tree import *


def comp(elem1, elem2):
    if len(elem1.serialize()) != len(elem2.serialize()):
        return False
    for i in range(len(elem1.serialize())):
        if elem1.serialize()[i] != elem2.serialize()[i]:
            return False
    return True


def gen(specs):
    return Tree(specs[0], specs[1], specs[2])


# La la funcion fitness calulara la diferencia entre el resultado esperado y el obtenido

def fitness(tree):
    #expected_result = 147
    #expected_result = 10000
    expected_result=1
    ev = tree.evalTree()
    return abs(expected_result - ev)


class GeneticAlgorithm:
    def __init__(self, specs, npopulation, fitness, gen, mutationRate, tolerancy=10):
        self.specs = specs
        self.npopulation = npopulation
        self.population = []
        self.fit = []
        self.fitness = fitness
        self.gen = gen
        self.mutationRate = mutationRate
        self.tolerancy = tolerancy
        self.bestfit = []
        self.generation = []
        self.allfit = []

    def getGenerations(self):
        return self.generation

    def getFitness(self):
        return self.bestfit

    # Step 1
    # Crea un arbol al azar con las especs dadas
    def initPopulation(self):
        for i in range(self.npopulation):
            self.population.append(self.gen(self.specs))

    # Step 2

    def checkfitness(self):
        self.fit = []
        for elem in self.population:
            self.fit.append(self.fitness(elem))

    # Step 3: Tournament Selection
    def tournament_selection(self, k):
        best = None
        if k == 0:
            best = 0
        for i in range(0, k):
            ind = randint(0, k)
            if (best == None) or (self.fit[ind] < self.fit[best]):
                best = ind
        return best

    # Step4: Reproduction. Each baby must be created with cross over
    # and mutation
    def reproduction(self):
        nparents = 2 * len(self.population)
        parents = []
        babies = []
        k = floor(3 * len(self.population) / 4)
        # elejir a los padres
        for i in range(0,  nparents):
            # Shuffle artesanal
            for index in range(len(self.population)):
                a = randint(0, len(self.population) - 1)
                b = randint(0, len(self.population) - 1)
                self.population[a], self.population[b] = self.population[b], self.population[a]
                self.fit[a], self.fit[b] = self.fit[b], self.fit[a]

            best = self.tournament_selection(k)
            parents.append(self.population[best])

        # Crear a los hijos, se modifica para que trabaje con arboles
        for i in range(0, len(self.population) * 2, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            # Para mixear los arboles, se serializaran ambos padres , se seleccionará un nodo para ambos y el primero
            # se convertirá en el padre del segundo

            mixingParent2 = parent2.serialize()
            mixingPoint2 = randint(0, len(mixingParent2) - 1)
            baby1= parent1.copyTree()
            baby2 = mixingParent2[mixingPoint2].copyTree()
            baby2.parent = baby1
            if random() > 0.5:
                baby1.left = baby2
            else:
                baby1.right = baby2
            baby = baby1

            # Mutation, reemplaza una parte al azar del arbol con otro
            if random() < self.mutationRate:
                a = baby.serialize()
                m = a[randint(0, len(a) - 1)]
                parent = m.parent
                if parent is not None:
                    if parent.left == m:
                        parent.left = Tree(randint(1, 10), parent.ops, parent.terms)
                    else:
                        parent.right = Tree(randint(1, 10), parent.ops, parent.terms)
            babies.append(baby)
        self.population = babies

    def getBestIndex(self):
        best = 0
        assert len(self.population) == len(self.fit)
        for i in range(len(self.fit)):
            if self.fit[i] < self.fit[best]:
                best = i
        return best

    def run(self):
        # paso1
        self.initPopulation()
        self.checkfitness()
        index = self.getBestIndex()
        guess = self.population[index]
        guessFitness = self.fit[index]

        last = []
        last.append(guess)
        self.end = 0
        iter = 1
        self.generation.append(iter)
        self.allfit.append(self.fit)
        self.bestfit.append(guessFitness)

        while guessFitness > self.tolerancy:

            if self.end:
                break
            print("Generation", format(iter), ";Current best:", format(guess))
            print("evaluated tree ", guess.evalTree())
            self.reproduction()
            self.checkfitness()
            guess = self.population[self.getBestIndex()]
            guessFitness = self.fit[self.getBestIndex()]






            if len(last) < self.tolerancy:
                last.append(guess)
            else:
                last.pop(0)
                last.append(guess)
                if comp(last[0], guess):
                    for elem in last[1:]:
                        if not comp(elem, guess):
                            self.end = 0
                            break
                        else:
                            self.end = 1
                            continue

            iter = iter + 1
            self.generation.append(iter)
            self.allfit.append(self.fit)
            self.bestfit.append(guessFitness)

        print("best: ", guess)
        if self.end == 1:
            print("maximo local")


        return guess




class Metrics:

    def __init__(self, specs, npob, fitnessfunc, genfunc, mr, tol):

        self.ga = GeneticAlgorithm(specs, npob, fitnessfunc, genfunc, mr, tol)
        self.ga.run()

    def fitnesscurve(self):
        plt.plot(self.ga.getGenerations(), self.ga.getFitness())
        plt.ylabel("Fitness")
        plt.xlabel("Generación")
        plt.title("Curva de fitness")
        plt.show()

    def averagefitnesscurve(self):
        fits = self.ga.allfit

        averagefits = []
        for i in range(len(fits)):
            av = 0
            for j in range(len(fits[i])):
                av += fits[i][j]
            av =  av / len(fits[i])
            averagefits.append(av)
        plt.plot(self.ga.getGenerations(), averagefits, 'r-')
        plt.ylabel("Average Fitness")
        plt.xlabel("Generación")
        plt.title("Average fitness curve")
        plt.show()


ops=['*', '+','-']
terms= ["14", "18", "1", "4"]
m = Metrics([4, ops, terms], 100, fitness, gen, 0.01, 0)
# m = Metrics(3, 100, fitness, genstr, 0.01, 100)
m.fitnesscurve()
m.averagefitnesscurve()


