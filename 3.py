def IsPointInCircle(x, y, xc, uc, r):
    R = ((x - xc) ** 2 + (y - yc) ** 2) ** 0.5
    return True if R <= r else False
x, y = float(input()), float(input())
xc, yc = float(input()), float(input())
r = float(input())
print('YES' if IsPointInCircle(x, y, xc, yc, r) else 'NO')
