import numpy as np

def dist_matrix(M1, M2):
    # Your code goes here
    # We use mathematical equality (a-b)**2 = a**2 + b**2 - 2*a*b
    # 
    # Sum of the squares of the elements of the rows
    sum_M1 = (M1**2).sum(axis=1, keepdims=True)
    sum_M2 = (M2**2).sum(axis=1, keepdims=True)
    # In order to get 2*a*b we do the dot product
    two_M1_M2 = 2*np.dot(M1, M2.T)
    # now we do the sum and sqrt
    return np.sqrt(sum_M1 + sum_M2.T - two_M1_M2)
    
