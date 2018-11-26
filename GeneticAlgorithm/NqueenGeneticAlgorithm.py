from math import floor
from random import randint, random

from sklearn.utils import shuffle


def comp(elem1, elem2):
    assert len(elem1) == len(elem2)
    for i in range(len(elem1)):
        if elem1[i] != elem2[i]:
            return False
    return True


def genqueen(n):
    return randint(0, n - 1)

def queenfitness(elem):
    ngenes = len(elem)
    # Verificar choces en las columnas
    duplicated_exc = set(elem)
    fitness = len(duplicated_exc)
    col_up=False
    col_down= False
    # Verificar choques en las diagonales
    for i in range(ngenes-1):
        gene = elem[i]
        for j in range(1, ngenes-i):
            next = elem[i+j]
            if next == gene + j:
                col_up=True
            elif next == gene - j:
                col_down=True
        if col_up== True:
            fitness -=1
        if col_down==True:
            fitness-=1
    return fitness



class GeneticAlgorithm:
    def __init__(self, ngens, npopulation, fitness, gen, mutationRate):
        self.ngens = ngens
        self.npopulation = npopulation
        self.population = []
        self.fit = []
        self.fitness = fitness
        self.gen = gen
        self.mutationRate = mutationRate

    # Step 1
    def initPopulation(self):
        for i in range(self.npopulation):
            element = []
            for j in range(self.ngens):
                element.append(self.gen(self.ngens))
            self.population.append(element)

    # Step 2

    def checkfitness(self):
        self.fit = []
        for elem in self.population:
            self.fit.append(self.fitness(elem))

    # Step 3: Tournament Selection
    def tournament_selection(self, pop, k):

        best = None
        if k == 0:
            best = 0
        for i in range(0, k):
            ind = randint(0, k)
            if (best == None) or (self.fit[ind] > self.fit[best]):
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
        for i in range(0, 2 * nparents):
            best = self.tournament_selection(shuffle(self.population), k)
            parents.append(self.population[best])

        # Crear a los hijos
        for i in range(0, len(self.population) * 2, 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            mixingPoint = randint(0, self.ngens)
            baby = []

            for j in range(0, self.ngens):
                # Cross Over
                if j < mixingPoint:
                    baby.append(parent1[j])
                else:
                    baby.append(parent2[j])
                # Mutation
                for k in range(len(baby)):
                    if random() < self.mutationRate:
                        baby[k] = self.gen(self.ngens)
            babies.append(baby)
            self.population = babies

    def getBestIndex(self):
        best = 0
        assert len(self.population) == len(self.fit)
        for i in range(len(self.fit)):
            if self.fit[i] > self.fit[best]:
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
        end = 0
        iter = 0
        while self.ngens > guessFitness:
            if end:
                break
            print("iteration", format(iter), ";current best:", format(guess))
            self.reproduction()
            self.checkfitness()
            guess = self.population[self.getBestIndex()]
            guessFitness = self.fit[self.getBestIndex()]
            if len(last) < 10:
                last.append(guess)
            else:
                last.pop(0)
                last.append(guess)
                if comp(last[0], guess):
                    for elem in last[1:]:
                        if not comp(elem, guess):
                            end = 0
                            break
                        else:
                            end = 1
                            continue

            iter = iter + 1
        print("best: ", guess)
        return guess


GeneticAlgorithm(5, 100, queenfitness, genqueen, 0.01).run()
