# def two_knights(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 6
#     elif n == 3:
#         return 28
#     elif n == 4:
#         return 96
#     n2 = n ** 2
#     return two_knights(n - 1) \
#             + 3 * (n2 - 3) + 4 * (n2 - 4) + (2 * n - 8) * (n2 - 5) \
#             - (2 * n - 1) * (2 * n - 2) // 2 + 2

# n = int(input())

# for k in range(1, n + 1):
#     print(two_knights(k))

n = int(input())

two_knights = [-1, 0, 6, 28, 96]
for k in range(5, n + 1):
    two_knights.append(two_knights[k - 1] \
        + 3 * (k ** 2 - 3) + 4 * (k ** 2 - 4) + (2 * k - 8) * (k ** 2 - 5) \
        - (2 * k - 1) * (2 * k - 2) // 2 + 2)

for k in range(1, n + 1):
    print(two_knights[k])

# def inside_board(n, i, j):
#     return 0 <= i and i < n and 0 <= j and j < n

# knight_moves = []
# for i in range(-2, 3):
#     if i == 0:
#         continue
#     for j in range(-2, 3):
#         if j == 0 or i == j:
#             continue
#         knight_moves.append((i, j))

# n = int(input())
# for k in range(1, n + 1):
#     board = [[0] * k for i in range(k)]
#     kxk_ways = 0
#     for i in range(k):
#         for j in range(k):
#             if board[i][j] == 1:
#                 continue
#             board[i][j] = 1
#             total_valid_moves = 0
#             top_left = [i, j]
#             bottom_right = [i, j]
#             for move in knight_moves:
#                 pos = [i + move[0], j + move[1]]
#                 if inside_board(k, pos[0], pos[1]):
#                     board[pos[0]][pos[1]] = 1
#                     total_valid_moves += 1
#                     top_left = [min(top_left[0], pos[0]), min(top_left[1], pos[1])]
#                     bottom_right = [max(bottom_right[0], pos[0]), max(bottom_right[1], pos[1])]
#                 kxk_ways += (bottom_right[0] - top_left[0]) * (bottom_right[1] - top_left[1]) - total_valid_moves - 1
#     print(kxk_ways)
