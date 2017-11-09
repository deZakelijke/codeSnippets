# Returns the QR-decomposition of A using Householder reflections

import numpy as np
import copy

def householder(A):

    if not type(A) is np.ndarray:
        print("Input is not a numpy array, attemt to convert A.")
        try:
            A = np.array(A, dtype=float)
        except TypeError:
            print("Input cannot be converted to a numpy array. Aborting QR decomposition.")
            return None


    m,n = A.shape
    R = copy.deepcopy(A)
    Q = np.identity(m) 

    for i in range(n):
        x = A[i:m,i]
        s = np.sign(x[0])
        if not s:
            s = 1
        q = s*np.linalg.norm(x)*np.identity(m-i)[:,0] + x
        q = q/np.linalg.norm(q)
        P = np.identity(m)
        P[i:m,i:m] = P[i:m,i:m] - 2*np.outer(q,q)
        print(P)
        print(P@(np.linalg.inv(P)))
        R = P@R
        Q = Q@np.linalg.inv(P)

    return Q,R



A = np.ones((3,2))
Q,R = householder(A)
#print(R)
#print(Q)
