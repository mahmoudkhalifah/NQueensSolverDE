class BoardRepresenter:

    def __init__(self, dim):
        self.dim = dim

    # initialize the board matrix based on vector

    # def boardRepresent(self):
    #     self.board = [[0 for i in range(self.dim)] for j in range(self.dim)]
    #     for i in self.vector:
    #         self.board[self.vector[i]][i] = 1
    #         print(i)
    
    def boardRepresent(self):
        self.board = [[0 for i in range(self.dim)] for j in range(self.dim)]
        for i in range(self.dim):
            self.board[self.vector[i]][i] = 1
            # print(i)
    
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
    def penaltyCounter(self, vector):
        self.vector = vector
        self.boardRepresent()
        penalty = 0
        visited = []
        # row check
        for i in self.vector:
            count = self.vector.count(i)
            if count > 1 and i not in visited:
                visited.append(i)
                penalty += count - 1
        for i in range(0, self.dim):
            penalty += self.isSafe(self.vector[i], i)
        return penalty

    # print the matrix
    def printBoard(self,vector):
        self.vector = vector
        self.boardRepresent()
        for row in range(self.dim):
            for col in range(self.dim):
                if self.board[row][col] == 1:
                    print('\033[93m', "♛", end="  ")
                else:
                    print('\033[0m', "-", end="  ")
            print()
        print('\033[0m')