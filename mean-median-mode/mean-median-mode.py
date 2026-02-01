import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    mean=float(np.mean(x))
    med=float(np.median(x))
    values, counts = np.unique(x, return_counts=True)
    mode = float(values[np.argmax(counts)])
    # Write code here
    return mean, med, mode