from collections import defaultdict
n, m = map(int, input().split())
d = defaultdict(list)
[d[input()].append(i+1) for i in range(n)]
for j in [' '.join(map(str, d[input()])) or -1 for i in range(m)]: 
    print (j)
