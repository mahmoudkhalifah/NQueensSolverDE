import random


class PopulationGenerator:

    def __init__(self, dim, NP):
        self.NPvectors = [[random.randint(0, dim - 1) for i in range(dim)] for j in range(NP)]

    def printPopulation(self):
        print(self.NPvectors)