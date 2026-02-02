import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    X=np.asarray(x,dtype=float)
   
    Y=np.asarray(y,dtype=float)
    return np.dot(X,Y)
    