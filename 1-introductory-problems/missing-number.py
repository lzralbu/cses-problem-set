n = int(input())
s = sum([int(num) for num in input().split(' ')])
print(n * (n + 1) // 2 - s)
