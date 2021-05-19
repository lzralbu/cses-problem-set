n = int(input())
ans = []
while n > 1:
    ans.append(str(n))
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
ans.append('1')
print(' '.join(ans))
