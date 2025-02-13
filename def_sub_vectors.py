import numpy as np 

def subtract_vectors(*vectors):
    """
    Subtracts all given vectors (bras or kets) in order using Numpy.
    
    Args:
        vectors: The vectors to subtract.
    
    Returns:
        A new vector that is the difference of the input vectors.
    
    Raises:
        ValueError: If the vectors are not the same length.
    """
    if not vectors:
        raise ValueError("At least one vector is required")
    
    if any(len(v) != len(vectors[0]) for v in vectors):
        raise ValueError("All vectors must be of the same length")
    
    # Start with the first vector, then subtract the rest
    result = vectors[0]
    for v in vectors[1:]:
        result = np.subtract(result, v)

    return result

ket1 = np.array([[1], [0]])
ket2 = np.array([[0], [1]])

bra1 = np.array([[1, 0]])
bra2 = np.array([[0, 1]])

print(subtract_vectors(ket1, ket2))  # Should output [[1], [-1]]
print(subtract_vectors(bra1, bra2))  # Should output [[1, -1]]