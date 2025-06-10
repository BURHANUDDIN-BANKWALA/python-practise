## assert IS A KEYWORD WE CAN USE TO CHECK ERRORS IF THE VALUE IS TRUE THE PROGRAM PROCEEDS WITHOUT ANY ERROR WHILE IF IT IS FALSE THEN IT EXECUTES AN ERROR
## ALSO REMEMBER THAT WHILE IMPORTING YOUR OWN FILE DON'T ENTER THE .py EXTENSION WITH THE FILE NAME

from unit_tests31 import square
def main():
    test_square()

def test_square():
    assert square(2)==4
    assert square(3)==9

if __name__=="__main__":
    main()

    ## THE ERROR WAS SUCCESSFULLY CATCHED WITH THIS TEST PROGRAM
    