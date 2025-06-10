from unit_tests31 import square

    
##def test_positive():
  ##  assert square(2)==4
    ##assert square(3)==9

def test_negative():
    assert square(-2)==4
    assert square(-3)==9
    
def test_zero():
    assert square(0)==0

##test_positive()
test_negative()
test_zero()

## THE CODE CATCHES THE BUG BUT ONLY IN SEQUENCE, IT DOESN'T PROCEED FORWARD AFTER THE FIRST TEST
## TYPE pytest test_calculator36.py