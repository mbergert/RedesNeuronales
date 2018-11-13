from random import randint, shuffle, random

word = [1, 0, 1, 0, 1]


def fitness(elem):
    fitting = 0
    assert len(elem) == len(word)
    for i in range(len(word)):
        if elem[i] == word[i]:
            fitting = fitting + 1
    return fitting


def gen():
    return randint(0, 1)


class GeneticAlgorithm:
    def __init__(self, ngens, npopulation, word, fitness, gen, mutationRate):
        self.ngens = ngens
        self.npopulation = npopulation
        self.population = []
        self.word = word
        self.fit = []
        self.fitness = fitness
        self.gen = gen
        self.mutationRate = mutationRate

    def __call__(self, *args, **kwargs):
        self.initPopulation()

    # Step 1
    def initPopulation(self):
        for i in range(self.npopulation):
            element = []
            for j in range(self.ngens):
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
            if (best == None) or (self.fit[ind] > self.fit[best]):
                best = ind
        return best

    # Step4: Reproduction. Each baby must be created with cross over
    # and mutation
    def reproduction(self, nparents):
        parents = []
        babies = []
        k = randint(0, len(self.population))
        # elejir a los padres
        for i in range(0, nparents):
            best = self.tournament_selection(shuffle(self.population), k)
            parents.append(self.population[best])

        # Crear a los hijos
        for i in range(0, len(self.population)):
            parent1 = parents[randint(0, len(parents))]
            parent2 = parents[randint(0, len(parents))]
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
                        if baby[k] == 0:
                            baby[k] = 1
                        else:
                            baby[k] = 0
            babies.append(baby)
