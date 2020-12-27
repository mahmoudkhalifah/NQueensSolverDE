from DifferentialEvolution import DifferentialEvolution
from PopulationGenerator import PopulationGenerator

# numOfIterations = 15000
# CR = 0.25
# F = 1
# timeLimit = 10*60
# N = int(input("Enter number of queens\n"))
# NP = N * 5
# print("CR =", CR, "F =", F, "NP =", NP)
pg = PopulationGenerator(4,40)
pg.printPopulation()
# solver = DifferentialEvolution(numOfIterations, CR, F, N, NP, timeLimit)
# solver.solve()
