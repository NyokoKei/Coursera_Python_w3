import math


def ReduceFraction(n, m):
    if m % n == 0:
        return 1, m // n
    return n // math.gcd(n, m), m // math.gcd(n, m)
n, m = int(input()), int(input())
print(*ReduceFraction(n, m))
