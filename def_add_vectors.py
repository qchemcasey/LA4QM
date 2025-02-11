# Without Numpy(fix for any number of vectors)

def add_vectors(vector1, vector2):
    """
    Adds two vectors of the same length.
    
    Args:
        vector1 (list): The first vector.
        vector2 (list): The second vector.
    
    Returns:
        list: A new vector that is the sum of vector1 and vector2.
    
    Raises:
        ValueError: If the vectors are not the same length.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")
    
    return [x + y for x, y in zip(vector1, vector2)]


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
    
    # Start with the first vector, then subtract the rest
    result = vectors[0]
    for v in vectors[1:]:
        result = np.add(result, v)

    return result


