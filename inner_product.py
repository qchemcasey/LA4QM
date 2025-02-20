import numpy as np

def inner_product(bra, ket):
    # Compute the inner product of a bra and a ket
    # Check for correct dimensions
    if bra.shape[1] != ket.shape[0]:  
        raise ValueError("Bra and ket dimensions do not match for inner product.")
    # Compute the inner product
    inner_prod = (bra @ ket).item() 
    return inner_prod



# Test
#ket = np.array([[1],[1j]])
#bra = np.array([[1,-1j]])

#print(inner_product(bra, ket))  # Expected result: 3*1 + 4*2 = 11
#print(ket.shape[0], bra.shape[1])  # Expected result: 2 2