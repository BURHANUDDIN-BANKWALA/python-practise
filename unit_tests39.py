from unit_tests38 import hello

def test_def():
    assert hello()=="hello, world"

def test_arg():
    assert hello("david")=="hello, david"

def test_c():
    for name in ["alif","be","te","se"]:
        assert hello(name)==f"hello, {name}"
## ENTER THE pytest SYNTAX IN THE TERMINAL TO CHECK THE CODE