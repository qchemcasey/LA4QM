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
    if isinstance(ket[0], list):
        ket = [k[0] for k in ket]

    return sum(b * k for b, k in zip(bra, ket))

print(inner_product([3, 4], [[1], [2]]))

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
    if len(bra) != len(ket):
        raise ValueError("Vectors must be of the same length.")

    return np.dot(bra, ket)

ket = np.array([[1], [2]])
bra = np.array([3, 4])

print(inner_product_np(bra, ket))
