def scale_vector(vector, scalar):
    """
    Scale a vector by a given scalar.

    Args:
        vector (list of float): The vector to scale.
        scalar (float): The scalar to multiply the vector by.

    Returns:
        list of float: The scaled vector.
    """
    return [component * scalar for component in vector]