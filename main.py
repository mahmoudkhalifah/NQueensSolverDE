import random
import time

from DifferentialEvolution import DifferentialEvolution

numOfIterations = 1000
CR = .8
F = 1
timeLimit = 30
N = int(input("Enter number of queens\n"))
population = N * 10
print("CR =", CR, "F =", F)
solver = DifferentialEvolution(numOfIterations, CR, F, N, population, timeLimit)
solver.solve()
