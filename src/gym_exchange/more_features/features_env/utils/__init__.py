"""Implementations of imitation and reward learning algorithms."""

def vwap_price(pairs):
    ''' pairs format
    price:    array([[ 1. ,  1. ,  1. ,  1.1,  0.9],
    quantity:        [ 2. , 23. ,  3. , 21. ,  3. ]])
    '''
    vwap_price = (pairs[0]*pairs[1]).sum()/pairs[1].sum()
    return vwap_price