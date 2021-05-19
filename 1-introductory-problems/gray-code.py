n = int(input())

cols = []
for k in range(n - 1, -1, -1):
    col = []
    two_power_k = 1 << k
    for i in range(1 << (n - k - 1)):
        col.extend([i & 1] * two_power_k + [~i & 1] * two_power_k)
    cols.append(col)

rows = zip(*cols)
gray_code = []
for row in rows:
    gray_code.append(''.join(map(str, row)))
print('\n'.join(gray_code))
