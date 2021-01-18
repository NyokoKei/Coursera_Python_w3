def power(a, n):
    if n == 0:
        return 1
    elif n % 2:
        return a * power(a, n - 1)
    return power(a * a, n / 2)
print(power(float(input()), int(input())))
