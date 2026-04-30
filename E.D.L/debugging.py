# 1. print statement
# 2. pdb

import pdb

def calculate_total(price, tax_rate):
    pdb.set_trace()
    total = price + (price + tax_rate)
    return total

calculate_total(100, 0.1)
