import numpy as np

n, m, p = map(int, input().split())    #assign n,m,p

source = " ".join(input() for _ in range(n))  #matrix1
matrix1 = np.array(source.split(), int)
matrix1.shape = (n, p)

source = " ".join(input() for _ in range(m)) #matrix2
matrix2 = np.array(source.split(), int)    
matrix2.shape = (m, p)

print(np.concatenate((matrix1, matrix2), axis=0)) #vertical axis=0
