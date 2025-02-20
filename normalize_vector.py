import numpy as np

def normalize_vector(vec):
    # Normalize a vector (ket or bra) to have unit norm
    norm = np.sqrt(np.sum(vec * vec.conj())) 
    
    if norm == 0:
        raise ValueError("Cannot normalize a zero vector.")
    # Check if the vector is already normalized
    if np.isclose(norm, 1.0):  
        print("Vector is already normalized.")
        return vec
    
    return vec / norm

# Example usage:
ket = np.array([[1 + 1j], [2 - 1j]])  # Complex column vector (2 x 1)
bra = np.array([[3 - 2j, 4 + 3j]])    # Complex row vector (1 x 2)

normalized_ket = normalize_vector(ket)
normalized_bra = normalize_vector(bra)

print("Normalized ket:\n", normalized_ket)
print("Normalized bra:\n", normalized_bra)
