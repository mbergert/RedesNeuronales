from random import randint

word = [1, 0, 1, 0, 1]


def fitness(elem):
    fitness = 0
    assert len(elem) == len(word)
    for i in range(len(word)):
        if elem[i] == word[i]:
            fitness = fitness + 1
    return fitness


def gen():
    return randint(0, 1)


class GeneticAlgorithm:
    def __init__(self, nbits, npopulation, word, fitness, gen):
        self.nbits = nbits
        self.npopulation = npopulation
        self.population = []
        self.word = word
        self.fit = []
        self.fitness = fitness
        self.gen = gen

    def __call__(self, *args, **kwargs):
        self.initPopulation()

    # Step 1
    def initPopulation(self):
        for i in range(self.npopulation):
            element = []
            for j in range(self.nbits):
                element.append(self.gen())
            self.population.append(element)

    # Step 2

    def checkfitness(self):
        for elem in self.population:
            self.fit.append(self.fitness(elem))

    # Step 3: Tournament Selection
    def tournament_selection(self, pop, k):
        best = None
        for i in range(0, k):
            ind = pop[randint(1, k)]
            if (best == None) or self.fit[ind] > self.fit[best]:
                best = ind
        return best

    # Step4: Reproduction. Each baby must be created with cross over
    #and mutation



