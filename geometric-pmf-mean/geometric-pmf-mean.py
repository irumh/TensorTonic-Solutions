import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    mean_geom=1/p
    k=np.asarray(k,dtype=float)
    pmf = (1 - p) ** (k - 1) * p 
    return pmf ,float(mean_geom)