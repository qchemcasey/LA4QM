# Without Numpy

def add_vectors(*vectors):
    """
    Adds vectors of the same length.

     Returns:
        list: A new vector that is the sum of all vectors.
    
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
        result = [x + y for x, y in zip(result, v)]

    return result

# With Numpy

import numpy as np 

def add_vectors_np(*vectors):
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


