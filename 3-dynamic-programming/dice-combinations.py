x = int(input())

count = [0] * (x + 1)
count[0] = 1
for x in range(1, x + 1):
    for coin in range(1, 6 + 1):
        if x >= coin:
            count[x] += count[x - coin]
    count[x] %= 10 ** 9 + 7

print(count[x])
