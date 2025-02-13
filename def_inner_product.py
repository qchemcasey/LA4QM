import numpy as np

def inner_product(bra, ket):
    """
    Calculate the inner product of two vectors using NumPy.
    
    Parameters:
    bra (numpy.ndarray): The bra vector (1 x n).
    ket (numpy.ndarray): The ket vector (n x 1).
    
    Returns:
    complex: The inner product of the two vectors.
    """
    if bra.shape[1] != ket.shape[0]:  # Check for correct dimensions
        raise ValueError("Bra and ket dimensions do not match for inner product.")
    inner_prod = (bra @ ket).item()  # Extract scalar value from 2D array
    return inner_prod

# Example Usage
ket = np.array([[1], [2]])  # Column vector (2 x 1)
bra = np.array([[3, 4]])    # Row vector (1 x 2), Hermitian conjugate of |ψ⟩

print(inner_product(bra, ket))  # Expected result: 3*1 + 4*2 = 11

print(ket.shape[0], bra.shape[1])  # Expected result: 2 2
