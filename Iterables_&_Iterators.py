from itertools import combinations 

N = int(input())
S = input().split(' ')
K = int(input())

num = 0
den = 0

for c in combinations(S,K):
    den+=1
    num+='a' in c
    
print (float(num)/den)
