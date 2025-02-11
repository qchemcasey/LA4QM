# Without Numpy (Fix for any number of vectors)

def subtract_vectors(vector1, vector2):
    """
    Subtracts two vectors of the same length.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    
    return [x - y for x, y in zip(vector1, vector2)]

# With Numpy

import numpy as np 

def subtract_vectors_np(*vectors):
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
