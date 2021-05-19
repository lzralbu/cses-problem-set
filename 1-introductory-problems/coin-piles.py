t = int(input())

while t > 0:
    a, b = map(int, input().split(' '))
    a2_b = a * 2 - b
    b2_a = b * 2 - a
    if a2_b >= 0 and a2_b % 3 == 0 and b2_a >= 0 and b2_a % 3 == 0:
        print('YES')
    else:
        print('NO')
    t -= 1
