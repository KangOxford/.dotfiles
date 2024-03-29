"""Implementations of imitation and reward learning algorithms."""

#................................................................................................
#...............UU.....UU....NN......N.......CCC......TTTTTTTTT...I......OOOOOO......NN......N...
#...FFFFFFFFFF.UUUU...UUUU..NNNN....NNN....CCCCCCCC..CTTTTTTTTTT.III....OOOOOOOOO...NNNN....NNN..
#...FFFFFFFFFF.UUUU...UUUU..NNNNN...NNN...CCCCCCCCCC.CTTTTTTTTTT.III...OOOOOOOOOO...NNNNN...NNN..
#...FFFFFFFFFF.UUUU...UUUU..NNNNN...NNN..CCCCCCCCCCC.CTTTTTTTTTT.III..OOOOOOOOOOOO..NNNNN...NNN..
#...FFFF.......UUUU...UUUU..NNNNNN..NNN..CCCC...CCCCC....TTTT....III..OOOO....OOOO..NNNNNN..NNN..
#...FFFF.......UUUU...UUUU..NNNNNNN.NNN.NCCCC....CCCC....TTTT....III..OOOO....OOOOO.NNNNNNN.NNN..
#...FFFFFFFFF..UUUU...UUUU..NNNNNNN.NNN.NCCC.............TTTT....III.IOOO......OOOO.NNNNNNN.NNN..
#...FFFFFFFFF..UUUU...UUUU..NNN.NNNNNNN.NCCC.............TTTT....III.IOOO......OOOO.NNN.NNNNNNN..
#...FFFFFFFFF..UUUU...UUUU..NNN.NNNNNNN.NCCC.............TTTT....III.IOOO......OOOO.NNN.NNNNNNN..
#...FFFF.......UUUU...UUUU..NNN..NNNNNN.NCCCC....CCCC....TTTT....III..OOOO....OOOOO.NNN..NNNNNN..
#...FFFF.......UUUU...UUUU..NNN..NNNNNN..CCCC...CCCCC....TTTT....III..OOOO....OOOO..NNN..NNNNNN..
#...FFFF.......UUUUUUUUUUU..NNN...NNNNN..CCCCCCCCCCC.....TTTT....III..OOOOOOOOOOOO..NNN...NNNNN..
#...FFFF.......UUUUUUUUUUU..NNN...NNNNN...CCCCCCCCCC.....TTTT....III...OOOOOOOOOO...NNN...NNNNN..
#...FFFF........UUUUUUUUU...NNN....NNNN....CCCCCCCC......TTTT....III....OOOOOOOOO...NNN....NNNN..
#.................UUUUU.....................CCCCC........................OOOOOO..................
#................................................................................................
from copy import deepcopy
from gym_exchange.data_orderbook_adapter import Configuration 

def cancel_by_price(order_book, Price):
    side = 'bid'
    order_list =  order_book.bids.get_price_list(Price)
    order = order_list.get_head_order()
    # order_id = order.order_id
    trade_id = order.trade_id
    timestamp = order.timestamp
    order_book.cancel_order(side, trade_id, time = timestamp)
    return order_book

def partly_cancel(order_book, right_order_price, wrong_order_price, side):
    tobe_returned_order_book = deepcopy(order_book)
    ranger = reversed(order_book.bids.price_map.items()) if side == 'bid' else order_book.asks.price_map.items()
    for price, order_list in ranger:
        sequence_condition = (right_order_price<price and price<=wrong_order_price) if side=='bid' else (wrong_order_price <= price  and price < right_order_price)
        if sequence_condition:
            for order in order_list:
                tobe_returned_order_book.cancel_order(side = side, 
                                        order_id = order.order_id,
                                        time = order.timestamp, 
                                        )
    return tobe_returned_order_book


def get_right_answer(index, d2):
    return d2.iloc[index,:].reset_index().drop(['index'],axis= 1).iloc[:,0].to_list()

def get_two_list4compare(order_book, index, d2, side):
    my_list =brief_order_book(order_book, side)[0:2*Configuration.price_level]
    # my_list = my_list[::-1] if side == 'ask' else my_list # if ask, reverse the price order
    # right_list = d2.iloc[index,:].reset_index().drop(['index'],axis= 1).iloc[:,0].to_list() # slower
    right_list = list(d2.iloc[index,:]) # faster
    return my_list, right_list
    
def is_right_answer(order_book, index, d2, side):
    my_list, right_list = get_two_list4compare(order_book, index, d2, side)
    # print("---my_list") ; print(my_list) #$
    # print('---right_list'); print(right_list) #$
    return len(list(set(right_list) - set(my_list))) == 0
    
    
def brief_order_book(order_book, side):
    my_list = []
    count = 0
    if side == 'bid': range_generater = reversed(order_book.bids.price_map.items())
    elif side=='ask': range_generater = order_book.asks.price_map.items()
    for key, value in range_generater:
        count +=1 
        quantity = value.volume
        price = value.head_order.price
        my_list.append(price)
        my_list.append(quantity)
        if count == Configuration.price_level:
            break
    return my_list

def update_id(message):
    if message['side'] == 'bid': Configuration.Adapter.type5_id_bid += 1; order_id = Configuration.Adapter.type5_id_bid
    else: Configuration.Adapter.type5_id_ask += 1; order_id = Configuration.Adapter.type5_id_ask
    message['order_id'] = order_id
    message['trade_id'] = order_id
    return message

def type5_update_id(previous_message, message):
    if message['side'] == 'bid': Configuration.Adapter.type5_id_bid += 1; order_id = Configuration.Adapter.type5_id_bid
    else: Configuration.Adapter.type5_id_ask += 1; order_id = Configuration.Adapter.type5_id_ask
    message['order_id'] = order_id
    message['trade_id'] = order_id
    previous_message['order_id'] = order_id
    previous_message['trade_id'] = order_id
    return previous_message, message
     