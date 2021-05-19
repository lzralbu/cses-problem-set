n = int(input())

# print((2 ** n) % (10 ** 9 + 7))

def fast_exp_2_mod(n):
    if n == 0:
        return 1
    ans = fast_exp_2_mod(n // 2)
    ans *= ans
    if n % 2 == 1:
        ans *= 2
    return ans % (10 ** 9 + 7)

print(fast_exp_2_mod(n))
