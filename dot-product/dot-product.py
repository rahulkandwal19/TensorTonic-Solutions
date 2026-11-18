import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    
    product = 0.0
    for i in range(0,len(x)):
        product += float(x[i])*float(y[i])

    return float(product)