from math import floor

from Tree import *



class Algorithm:
    class GeneticAlgorithm:
        def __init__(self, ngens, npopulation, fitness, gen, mutationRate, tolerancy=10):
            self.ngens = ngens
            self.npopulation = npopulation
            self.population = []
            self.fit = []
            self.fitness = fitness
            self.gen = gen
            self.mutationRate = mutationRate
            self.tolerancy = tolerancy
            self.bestfit = []
            self.generation = []

        def getGenerations(self):
            return self.generation

        def getFitness(self):
            return self.bestfit

        # Step 1
        def initPopulation(self):
            for i in range(self.npopulation):
                self.population.append(Tree())

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
                # Shuffle artesanal
                for index in range(len(self.population)):
                    a = randint(0, len(self.population) - 1)
                    b = randint(0, len(self.population) - 1)
                    self.population[a], self.population[b] = self.population[b], self.population[a]
                    self.fit[a], self.fit[b] = self.fit[b], self.fit[a]

                best = self.tournament_selection(k)
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
            self.end = 0
            iter = 1

            while self.ngens > guessFitness:

                if self.end:
                    break
                self.generation.append(iter)
                print("Generation", format(iter), ";Current best:", format(guess))
                self.reproduction()
                self.checkfitness()
                guess = self.population[self.getBestIndex()]
                guessFitness = self.fit[self.getBestIndex()]
                self.bestfit.append(guessFitness)
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

            print("best: ", guess)

            return guess