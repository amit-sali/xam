N = 4

def isSafe(board, row, col):
    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    if col >= N:
        return True

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUtil(board, col + 1) == True:
                return True
            board[i][col] = 0  # BACKTRACK
    return False

if __name__ == "__main__":
    board = [[0] * N for _ in range(N)]

    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
    else:
        for i in range(N):
            for j in range(N):
                print(" " + str(board[i][j]) + " ", end="")
            print()
