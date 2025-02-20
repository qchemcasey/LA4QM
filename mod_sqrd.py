import numpy as np

import sys
import os

from def_inner_product import inner_product

def mod_sqrd(bra, ket):
    # Compute the square of the modulus of a ket
    sqr_mod = inner_product(bra, ket) * inner_product(bra, ket).conjugate()
    return sqr_mod

#ket = np.array([[1],[1j]])
#bra = np.array([[1,-1]])
#print(mod_sqrd(bra, ket))