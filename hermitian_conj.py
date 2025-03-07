import numpy as np

def hermitian_conj(*vectors):
    """
    Takes one or more NumPy arrays (either bra or ket) and returns their Hermitian conjugates.

    Parameters:
        vectors (np.ndarray): One or more NumPy arrays representing kets (column vectors) or bras (row vectors).

    Returns:
        list: A list of Hermitian conjugates (or a single array if one input is provided).
    """
    
    results = []
    
    for v in vectors:
        if not isinstance(v, np.ndarray):
            raise TypeError("All arguments must be NumPy arrays")
        
        # Ensure input is at least 2D
        v = np.atleast_2d(v)
        
        # Compute the Hermitian conjugate
        results.append(v.conj().T)
    
    # Return a single array if only one vector was passed
    return results[0] if len(results) == 1 else results



# Test
ket = np.array([[1],[1j]])
bra = np.array([[1,-1j]])
matrix = np.array([[1+1j, 2, 3], [4, 5, 6], [7,8,9]])  # Matrix A


results = hermitian_conj(ket, bra, matrix)
for res in results:
    print(res, "\n") 