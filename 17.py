s = input()
s = s.split()
for i in s:
    if not int(i) % 2:
        print(i, end=' ')
