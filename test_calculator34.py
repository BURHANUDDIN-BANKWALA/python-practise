## AssertionError
## USING try AND except WE WILL AGAIN CREATE A TEST PROGRAM
from unit_tests31 import square
def main():
    test_square()

def test_square():
    try:
        assert square(2)==4

    except AssertionError :
        print("bug was found in 2 sq 4")

    try :
        assert square(3)==9

    except AssertionError :
        print("bug was found in 3 sq 9")

if __name__=="__main__":
    main() 

## THIS PROGRAM ALSO SUCCESSFULLY CATCHES THE BUG
