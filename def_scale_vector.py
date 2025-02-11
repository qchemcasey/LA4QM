# Without Numpy

def scale_vector(vector, scalar):
    """
    Scale a vector (bra or ket) by a given scalar.

    Args:
        vector (list of float): The vector to scale.
        scalar (float): The scalar to multiply the vector by.

    Returns:
        list of float: The scaled vector.
    """
    return [component * scalar for component in vector]

# With Numpy

import numpy as np 

def scale_vector_np(vector, scalar):
    """
    Scale a vector by a given scalar using Numpy.

    Args:
        vector (numpy array): The vector to scale.
        scalar (float): The scalar to multiply the vector by.

    Returns:
        numpy array: The scaled vector.
    """
    return np.multiply(vector, scalar)
