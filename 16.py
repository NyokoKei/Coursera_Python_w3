s = input()
s = s.split()
for i in range(len(s)):
    print(s[i] if not i % 2 else ' ', end='')
