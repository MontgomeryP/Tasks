a = int(input())
b = int(input())
c = int(input())

D = b**2-4*a*c
from math import sqrt

if D < 0:
    print('error', 'D<0')

if D == 0:
    x = (-b / (2 * a))
    print(x)

if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(x1, x2)





