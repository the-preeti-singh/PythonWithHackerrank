k = int(input())
L = str(input()).split(" ")
family = L
total = set(L)
for r in set(L):
    try:
        family.remove(r)
    except:
        pass
print ("".join((total - set(family))))
