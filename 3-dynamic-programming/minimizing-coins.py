n, x = [int(word) for word in input().split(' ')]
coins = sorted([int(word) for word in input().split(' ')])

solution = [0] * (x + 1)
for value in range(1, x + 1):
    solution[value] = n + 1
    for coin in coins:
        if value >= coin:
            solution[value] = min(solution[value], solution[value - coin] + 1)
        else:
            break

# print([a for a in solution if a > 2])
print(solution)

if solution[-1] == n + 1:
    print(-1)
else:
    print(solution[-1])
