"""Implementations of imitation and reward learning algorithms."""

def latest_timestamp(order_book):
    '''ought to return the latest timestamp in the exchange.prev_trades 
       and exchange.prev_orders_in_book'''
    timestamp_list = []
    for tree in [order_book.asks, order_book.bids]:
        if tree != None and len(tree) > 0:
            for key, list_ in  reversed(tree.price_map.items()):
                for order in list_:
                    timestamp_list.append(order.timestamp)
    return max(timestamp_list) #max_timestamp 

def timestamp_increase(timestamp, order_flow):
    str_int_timestamp = str(int(timestamp[0:5]) * int(1e9) + (int(timestamp[6:15]) +1))
    order_flow.timestamp = str(str_int_timestamp[0:5])+'.'+str(str_int_timestamp[5:15])
    return order_flow