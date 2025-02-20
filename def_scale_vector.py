import numpy as np 

def scale_vector(vector, scalar):
    """
    Scale a vector (bra or ket) by a given scalar using Numpy.
    Args:
        vector (numpy array): The vector to scale.
        scalar (float): The scalar to multiply the vector by.

    Returns:
        numpy array: The scaled vector.
    """
    return np.multiply(vector, scalar)



# Test
ket = np.array([[1],[1j]])
bra = np.array([[1,-1j]])

print(scale_vector(ket, 2))  # Should output [[2], [0]]
print(scale_vector(bra, 2))  # Should output [[2, 0]]

