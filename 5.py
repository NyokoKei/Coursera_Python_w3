def IsPrime(n):
    sn = n ** 0.5
    i = 2
    while i <= sn:
        if n % i:
            i += 1
        else:
            return 'NO'
    return 'YES'
n = int(input())
print(IsPrime(n))
