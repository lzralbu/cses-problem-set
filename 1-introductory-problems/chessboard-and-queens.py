board = []

try:
    while True:
        board.append(input())
except EOFError:
    pass

n = len(board)

col = [0] * n
diag1 = [0] * (2 * n - 1)
diag2 = [0] * (2 * n - 1)

count = 0
def backtrack(y):
    global board, n, col, diag1, diag2, count
    if y == n:
        count += 1
        return
    
    for x in range(n):
        if board[y][x] == '*' or col[x] or diag1[x - y + n - 1] or diag2[x + y]:
            continue
        col[x] = diag1[x - y + n - 1] = diag2[x + y] = 1
        backtrack(y + 1)
        col[x] = diag1[x - y + n - 1] = diag2[x + y] = 0

backtrack(0)
print(count)
