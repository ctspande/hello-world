"""
******
*    *
*    *
*    *
******

"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol needs to be length of 1.')
    if (width < 2) or (heigh < 2):
        raise Exception('Width and height must be greater to 2')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('l', 1, 1)
