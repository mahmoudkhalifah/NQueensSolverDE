from DifferentialEvolution import DifferentialEvolution

numOfIterations = 15000
CR = 0.25
F = 1
timeLimit = 3*60
N = int(input("Enter number of queens\n"))
NP = N * 10
print("CR =", CR, "F =", F, "NP =", NP)
solver = DifferentialEvolution(numOfIterations, CR, F, N, NP, timeLimit)
solver.solve()
