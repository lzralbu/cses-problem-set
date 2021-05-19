import math
import collections

n = int(input())

if 2 <= n and n <= 3:
    print('NO SOLUTION')
else:
    permutation = []
    permutation += [str(2 * i + 2) for i in range(math.floor(n / 2))]
    permutation += [str(2 * i + 1) for i in range(math.ceil(n / 2))]
    print(' '.join(permutation))
