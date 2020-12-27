import random


class PopulationGenerator:

    def __init__(self, dim, NP):
        # self.NPvectors = [[random.randint(0, dim - 1) for i in range(dim)] for j in range(NP)]
        self.NPvectors = [[-1 for i in range(dim)] for j in range(NP)]
        for i in range(NP):
            for j in range(dim):
                r = random.randint(0, dim - 1)
                while r in self.NPvectors[i]:
                    r = random.randint(0, dim - 1)
                self.NPvectors[i][j] = r

    def printPopulation(self):
        print(self.NPvectors)
