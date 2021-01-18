def Sum(n):
    return sum(n)
arr = []
n = int(input())
while n:
    arr.append(n)
    n = int(input())
print(Sum(arr))
