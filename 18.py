s = input()
s = [int(i) for i in s.split()]
k = 0
for i in s:
    if i > 0:
        k += 1
print(k)
