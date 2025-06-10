## pytest IS ALSO A LIBRARY 
## FIRST INSTALL pytest LIBRARY BY USING
## pip install pytest IN THE TERMINAL WINDOW
from unit_tests31 import square
def test_square():
    assert square(2)==4
    assert square(3)==9
    assert square(-2)==4
    assert square(-3)==9
    assert square(0)==0
    
test_square()
## NOW ENTER pytest test_calculator35.py IN THE TERMINAL WINDOW
## THE TERMINAL DISPLAYS THE FAILURE MESSAGE
