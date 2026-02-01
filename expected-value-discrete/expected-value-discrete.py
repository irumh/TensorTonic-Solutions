import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)
    if not np.allclose(np.sum(p), 1.0):
        raise ValueError("Probabilities must sum to 1")
    expected_value = np.sum(x * p)
    return float(expected_value)
