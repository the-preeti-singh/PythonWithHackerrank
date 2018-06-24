A = set(map(int,input().split()))
for _ in range(int(input())):
    B = set(map(int,input().split()))
    if(not(A>B)or(len(A)<=len(B))):
        print("False"); exit()
print("True")
