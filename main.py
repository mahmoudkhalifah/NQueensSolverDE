from random import randint


class PopulationGenerator:
    NPvectors = [[]]

    # constructor to generate population
    def __init__(self, dim, NP):
        self.NPvectors = [[-1 for i in range(dim)] for j in range(NP)]
        for i in range(0, NP):
            for j in range(0, dim):
                n = randint(0, dim - 1)
                while n in self.NPvectors[i]:
                    n = randint(0, dim - 1)
                self.NPvectors[i][j] = n

    def printPopulation(self):
        print(self.NPvectors)


class BoardRepresenter:
    # matrix to represent the vector
    board = [[]]
    # chosen vector to represent it
    vector = []
    # number of queens
    dim = 0

    # initialize the board matrix based on vector
    def boardRepresent(self, dim, vector):
        self.dim = dim
        self.vector = vector
        self.board = [[0 for i in range(dim)] for j in range(dim)]
        for i in vector:
            self.board[vector[i]][i] = 1

    # return number of mistakes to every single queen
    def isSafe(self, row, col):
        penalty = 0
        i = row - 1
        j = col - 1
        # left up diagonal check
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                penalty += 1
                break

            i -= 1
            j -= 1

        i = row + 1
        j = col - 1
        # left down diagonal check
        while i < self.dim and j >= 0:
            if self.board[i][j] == 1:
                penalty += 1
                break
            i += 1
            j -= 1
        return penalty

    # return total number of mistakes on the board
    def penaltyCounter(self):
        penalty = 0
        for i in range(0, self.dim):
            penalty += self.isSafe(self.vector[i], i)
        return penalty

    # print the matrix
    def printBoard(self):
        for row in range(self.dim):
            for col in range(self.dim):
                if self.board[row][col] == 1:
                    print('\033[93m', "♛", end="  ")
                else:
                    print('\033[0m', "-", end="  ")
            print()


N = int(input("Enter number of queens\n"))
pg = PopulationGenerator(N, 10 * N)
pg.printPopulation()
vector = pg.NPvectors[randint(0, (10 * N) - 1)]
print(vector)
bp = BoardRepresenter()
bp.boardRepresent(N, vector)
bp.printBoard()
print(bp.penaltyCounter())
