import numpy as np

def outer_product(ket, bra):
    # Compute the outer product of a ket and a bra
    outer_prod = np.outer(ket, bra)
    return outer_prod 

# Example
#ket = np.array([[1],[1j]])
#bra = np.array([[1,-1j]])
#print(outer_product(ket, bra))
