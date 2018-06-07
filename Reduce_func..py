from fractions import Fraction
from functools import reduce

n = int(input())
data = [Fraction("/".join(input().split())) for _ in range(n)]
t = reduce(lambda x, y: x*y, data)
print(t.numerator, t.denominator)

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
