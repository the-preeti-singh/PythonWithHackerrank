if __name__ == '__main__':
    num = int(input())
    list1 = []
    for i in range(num):
        N = str(input())
        N = N.split() 
        if "insert" in N:
            list1.insert(int(N[1]),int(N[2]))
        elif "print" in N:
            print(list1)
        elif "remove" in N:
            list1.remove(int(N[1]))
        elif "append" in N:
            list1.append(int(N[1]))
        elif "pop" in N:
            list1.pop()
        elif "reverse" in N:
            list1.reverse()
        elif "sort" in N:
            list1.sort()
