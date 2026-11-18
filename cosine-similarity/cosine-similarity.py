import numpy as np

def cosine_similarity(a, b):
    coss = 0.0
    coss = np.dot(a,b)

    # Magnitude A
    A = 0.0
    for x in a:
        A += x**2
    A = A**0.5

    #Magnitude B 
    B = 0.0
    for x in b:
        B += x**2
    B = B**0.5

    if(A*B == 0): return float(0)
    return float(coss/(A*B))
    