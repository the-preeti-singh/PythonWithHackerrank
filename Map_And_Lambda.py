from sys import stdin

f = lambda x, y, z : f(y, y+x, z-1) if z > 0 else x 

length = int(stdin.readline())

print ([f( 0, 1, t)**3 for t in range(0, length)])
