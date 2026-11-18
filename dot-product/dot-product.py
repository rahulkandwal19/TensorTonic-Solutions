import numpy as np

def dot_product(x, y):
    
    product = 0.0
    for i in range(0,len(x)):
        product += x[i]*y[i]

    return float(product)