from lib.grammar import *

def testing_capital():
    result = capital("MY name is Liam!")
    assert result == True