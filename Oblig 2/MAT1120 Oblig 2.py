import numpy as np
from numpy import random
from scipy.linalg import null_space

def randlinkmatrix(n):
    A = np.round(np.random.rand(n,n))
    for k in range(n-1):
        A[k,k] = 0
        if np.all(A[:,k]) == 0:
            A[n-1,k] = 1
        s = np.sum(A[:,k])
        A[:,k] = 1/s * A[:,k]
        
    A[n-1,n-1] = 0
    if np.all(A[:,n-1]) == 0:
        A[1,n-1] = 1
    s = np.sum(A[:,n-1])
    A[:,n-1] = 1/s * A[:,n-1]
    
    return A

def ranking(A):
    n = A.shape[0]
    if A.shape[0] != A.shape[1]:
        raise ValueError("This matrix is not a n x n matrix")
    
    if np.count_nonzero(np.diag(A)) != 0:
        raise ValueError("This matrix has non zero values along its diagonal")
    
    for k in range(n):
        if np.sum(A[:,k]) != 1:
            raise ValueError("The sum of this matrix's colums does not equal 1")
        
    if any(A) < 0:
        raise ValueError("There are negative values in this matrix")
    
    m = .1
    S = np.full((n,n), 1/n)
    M =  (1-m)*A + m*S
    I = np.eye(n)
    nullspace = null_space(M-I)
    score = nullspace/np.sum(nullspace)
    return score
    
def rankingApprox(A, delta):
    
    n = A.shape[0]
    if A.shape[0] != A.shape[1]:
        raise ValueError("This matrix is not a n x n matrix")
    
    if np.count_nonzero(np.diag(A)) != 0:
        raise ValueError("This matrix has non zero values along its diagonal")
    
    for k in range(n):
        if np.sum(A[:,k]) != 1:
            raise ValueError("The sum of this matrix's columns does not equal 1")
        
    if np.any(A) < 0:
        raise ValueError('There are negative values in the matrix')
    
    n = A.shape[0]
    m = .1
    S = np.full((n,n), 1/n)
    M =  (1-m)*A + m*S
    x0 = np.full((n,1), 1/n)
    x = [x0]
    x.append(np.matmul(M,x0)) 
    k = 1
    while np.any(x[k] - x[k-1]) >= delta:
        x.append(np.matmul(M,x[k]))
        k += 1
    return x[-1]  

A = np.array([[  0, 1/2,   0, 0, 1/4], 
              [1/2,   0, 1/2, 0, 1/4], 
              [  0,   0,   0, 0, 1/4], 
              [  0,   0,   0, 0, 1/4], 
              [1/2, 1/2, 1/2, 1,   0]])

print(f'Score vektor ved bruk av ranking \n{ranking(A)}')
print()
print(f'Score vektor ved bruk av rankingApprox \n{rankingApprox(A, .01)}')
