n = int(input())

def fat(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans

# for i in range(1, 210):
#     if i % 5 == 0:
#         print()
#     print(i, fat(i), i // 5)

# print(n // 5)

# two_counter = 0
# five_counter = 0
# pseudo_factorial = 1
# for k in range(2, n + 1):
    # if k % 2 == 0 or k % 5 == 0:
    #     pseudo_factorial *= k
    # k0 = k
    # while k0 > 0:
    #     if k0 % 2 == 0:
    #         two_counter += 1
    #         k0 >>= 1
    #     elif k0 % 5 == 0:
    #         five_counter += 1
    #         k0 //= 5
    #     else:
    #         break

# print(fat(n))
# print(pseudo_factorial)
# print(min(two_counter, five_counter))

import math

for k in range(1, 11):
    two_counter = k // 2
    five_counter = k // 5
    ten_counter = k // 10

    a = two_counter - ten_counter
    b = five_counter - ten_counter

    print(f'k = {k}, k! = {fat(k)}')
    print('trailing zeros:', math.ceil(a * math.log10(2) + b * math.log10(5)))
    print('-----')
