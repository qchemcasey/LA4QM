import numpy as np 

def add_vectors(*vectors):
    """
    Adds all given vectors in order using Numpy.
    
    Args:
        vectors: The vectors to add.
    
    Returns:
        A new vector that is the sum of the input vectors.
    
    Raises:
        ValueError: If the vectors are not the same length.
    """
    if not vectors:
        raise ValueError("At least one vector is required")
    
    if any(len(v) != len(vectors[0]) for v in vectors):
        raise ValueError("All vectors must be of the same length")
    
    # Start with the first vector, then add the rest
    result = vectors[0]
    for v in vectors[1:]:
        result = np.add(result, v)

    return result



# Test
ket1 = np.array([[1], [0]])
ket2 = np.array([[0], [1]])

bra1 = np.array([[1, 0]])
bra2 = np.array([[0, 1]])

print(add_vectors(ket1, ket2))  # Should output [[1], [1]]
print(add_vectors(bra1, bra2))  # Should output [[1, 1]]