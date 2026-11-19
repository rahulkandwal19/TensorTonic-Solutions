import numpy as np

def matrix_transpose(A):
    A = np.array(A)
    N,M = A.shape
    
    T = np.zeros((M,N), dtype = A.dtype)
    
    for i in range(0,N):
        for j in range(0,M):
            T[j,i] = A[i,j]
    
    return T
