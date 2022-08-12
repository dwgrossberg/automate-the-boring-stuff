import traceback

"""

***********
*         *
*         *
*         *
***********

"""


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to a string of length 1')
    if width <= 2:
        raise Exception('width must be greater than 2')
    if height <= 2:
        raise Exception('height must be greater than 2')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 15, 5), ('9', 60, 3), ('X0)', 20, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))
