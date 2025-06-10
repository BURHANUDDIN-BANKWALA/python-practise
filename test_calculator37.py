## TypeError IS AN ANOTHER TYPE OF ERROR THAT OCCURS WHEN SOME WRONG VALUE HAS RECIEVED
import pytest
from unit_tests31 import square
##def test_p():
  ##  assert square(2)==4
    ##assert square(3)==9

def test_n():
    assert square(-2)==4
    assert square(-3)==9

def test_z():
    assert square(0)==0
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")


##test_p()
test_n()
test_z()
test_str()

## SIMILIAR TO THE PREVIOUS CODE IT STOPS AT THE FIRST BUG APPEARED