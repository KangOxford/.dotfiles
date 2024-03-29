"""Implementations of imitation and reward learning algorithms."""

import numpy as np
def vwap_price(pairs):
    ''' pairs format
    price:    array([[ 1. ,  1. ,  1. ,  1.1,  0.9],
    quantity:        [ 2. , 23. ,  3. , 21. ,  3. ]])
    '''
    vwap_price = (pairs[0]*pairs[1]).sum()/pairs[1].sum()
    return vwap_price

def broadcast_lists(list1, list2):
    shorter, longer = sorted([list1, list2], key=len)
    difference = 1000 if shorter is list1 else -1000
    for _ in range((len(longer) - len(shorter)) // 2):
        last_element = [shorter[-2] + difference, 0]
        shorter.extend(last_element)
    return np.array([list1, list2])
