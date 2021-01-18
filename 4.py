def MinDivisor(n):
    sn = int(n ** 0.5)
    i = 2
    while i <= sn:
        if n % i:
            i += 1
        else:
            return i
    return n
n = int(input())
print(MinDivisor(n))
