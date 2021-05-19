t = int(input())

while t > 0:
    y, x = [int(num) for num in input().split(' ')]
    n = max(y, x)

    ans = 1 + (n - 1) ** 2
    if n % 2 == 0:
        ans += abs(x - n) + abs(y - 1)
    else:
        ans += abs(x - 1) + abs(y - n)

    print(ans)
    t -= 1
