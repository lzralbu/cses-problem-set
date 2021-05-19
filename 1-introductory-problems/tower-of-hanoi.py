n = int(input())

def solve_hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        solve_hanoi(n - 1, a, c, b)
        print(a, c)
        solve_hanoi(n - 1, b, a, c)

print(2 ** n - 1)
solve_hanoi(n, 1, 2, 3)
