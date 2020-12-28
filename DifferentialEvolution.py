import random
import threading
import time
from concurrent.futures import thread

from BoardRepresenter import BoardRepresenter
from PopulationGenerator import PopulationGenerator


class DifferentialEvolution:

    def __init__(self, numOfIterations, CR, F, dim, NP,timeLimit):
        self.iteration = 0
        self.numOfIterations = numOfIterations
        self.CR = CR
        self.F = F
        self.dim = dim
        self.NP = NP
        self.timeLimit = timeLimit
        self.pg = PopulationGenerator(self.dim, self.NP)
        self.br = BoardRepresenter(self.dim)

    def crossover(self, p4, mutant) -> list:
        trial = [0] * self.dim
        for i in range(self.dim):
            # if random.random() < self.CR and not mutant[i] >= self.dim and not mutant[i] < 0:
            #     trial[i] = round(int(mutant[i]))
            if random.random() < self.CR:
                if mutant[i] >= self.dim:
                    trial[i] = self.dim-1
                elif mutant[i] < 0:
                    trial[i] = 0
                else:
                    trial[i] = round(int(mutant[i]))
            else:
                trial[i] = p4[i]
        return trial

    def mutation(self, p1, p2, p3, p4) -> list:
        mutant = [0] * self.dim
        for i in range(self.dim):
            mutant[i] = p3[i] + self.F * (p1[i] - p2[i])
        return self.crossover(p4, mutant)

    def iterate(self,start,end):
        i = start
        j = end
        for i in range(j):
            p4 = self.pg.NPvectors[i]
            [p1, p2, p3] = random.sample(self.pg.NPvectors, 3)
            while p1 == p4 or p2 == p4 or p3 == p4:
                [p1, p2, p3] = random.sample(self.pg.NPvectors, 3)
            trial = self.mutation(p1, p2, p3, p4)
            if self.br.penaltyCounter(trial) < self.br.penaltyCounter(p4):
                self.pg.NPvectors[i] = trial

    def findSolutions(self):
        solutions = []
        for i in range(self.NP):
            if self.br.penaltyCounter(self.pg.NPvectors[i]) == 0 and self.pg.NPvectors[i] not in solutions:
                solutions.append(self.pg.NPvectors[i])
        return solutions

    def solve(self):
        startTime = time.time()
        solutions = self.findSolutions()
        numOfThreads = 1
        for i in range(4,11):
            if self.numOfIterations % i:
                numOfThreads = i
        threads = []
        while len(solutions) == 0 and self.iteration < self.numOfIterations and time.time()-startTime < self.timeLimit:
            for i in range(0, numOfThreads):
                threads.insert(i, threading.Thread(self.iterate((i*self.dim)%self.NP,(i*self.dim+self.dim)%self.NP)))
                threads[i].start()
            for t in threads:
                t.join()
            solutions = self.findSolutions()

            self.iteration += 1
        print(len(solutions),"solution(s) found in", round(time.time()-startTime,4),"s and", self.iteration, "iterations.")
        for i in solutions:
            self.br.printBoard(i)
