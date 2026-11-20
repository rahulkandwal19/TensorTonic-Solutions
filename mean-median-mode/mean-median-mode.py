from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    x = np.array(x, dtype=float);
    
    mean = float(np.mean(x))
    
    median = float(np.median(x))

    value, frequency = np.unique(x, return_counts=True)
    mode = float(value[np.argmax(frequency)])
    
    return {"mean": mean, "median": median, "mode": mode}