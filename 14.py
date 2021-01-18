n = int(input())
print('+___ ' * n)
for i in range(n):
    print('|', i + 1, ' / ', sep='', end='')
print('\n', "|__\\ " * n, '\n', '|    ' * n, sep='')
