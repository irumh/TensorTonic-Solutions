import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    pf=np.percentile(x,q,method='linear')
    return pf