def IsPointInSquare(x, y):
    return True if abs(x) <= 1 and abs(y) <= 1 else False
x, y = float(input()), float(input())
print('YES' if IsPointInSquare(x, y) else 'NO')
