class inp(Exception):
    pass
def input():
    raise inp
class order(Exception):
    pass
def order_input():
    raise order