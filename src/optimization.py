import numpy as np
from scipy.stats import norm

def calculate_optimal_stock(mean, std, price, cost, salvage=0):
    # Cu: Cost of Understocking (Profit lost per unit)
    cu = price - cost
    # Co: Cost of Overstocking (Loss per unit that spoils)
    co = cost - salvage
    
    # Critical Fractile (Optimal Service Level)
    critical_fractile = cu / (cu + co)
    
    # Calculate Optimal Quantity (Q*) using Inverse CDF
    z_score = norm.ppf(critical_fractile)
    optimal_q = mean + (z_score * std)
    
    return int(np.ceil(optimal_q)), critical_fractile
