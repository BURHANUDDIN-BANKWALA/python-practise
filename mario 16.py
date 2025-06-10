## MARIO FUNCTION TO CREATE A 4 BLOCK LAYER OF QUESTION MARKS
def main():
    print_row(4)

def print_row(width):
    print("?"*width)

main()

## CREATING A MARIO SQUARE PATTERN
def square():
    layer(3)

def layer(size):
    for i in range(size):
        for j in range(size):
            print("#",end="")

        ## HERE THE EMPTY print() CREATES A NEW LINE
        print()
    
     
    
square()