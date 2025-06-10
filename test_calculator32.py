## HERE WE WILL FIRST IMPORT THE LIBRARY AND THE SQUARE FUNCTION FROM THE PREVIOUS PROGRAM
from unit_tests31 import square

def main():
    test_square()

def test_square():
    if square(2)!=4:
        print("bug in 2 sq 4")

    if square(3)!=9:
        print("bug in 3 sq 9")


if __name__=="__main__":
        main()
