#  Without Numpy

def inner_product(bra, ket):
    """
    Calculate the inner product of two vectors.
    
    Parameters:
    bra (list): The bra vector.
    ket (list): The ket vector.
    
    Returns:
    float: The inner product of the two vectors.
    """
    # Ensure bra is a 1D list
    if isinstance(bra[0], list):
        bra = [b[0] for b in bra]

    return sum(b * k for b, k in zip(bra, ket))


# With Numpy

import numpy as np

def inner_product_np(bra, ket):
    """
    Calculate the inner product of two vectors using NumPy.
    
    Parameters:
    bra (numpy.ndarray): The bra vector.
    ket (numpy.ndarray): The ket vector.
    
    Returns:
    float: The inner product of the two vectors.
    """
    # Ensure bra is a 1D array
    bra = bra.reshape(-1)

    return np.dot(bra, ket)

bra = np.array([[1], [2], [3]])
ket = np.array([3, 4, 5])

print(inner_product_np(bra, ket))