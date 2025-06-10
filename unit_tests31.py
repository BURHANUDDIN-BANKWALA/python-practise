## HERE WE HAVE CREATED A SIMPLE PROGRAM THAT RETURNS THE USER SQUARE OF A NO.
## TO TEST THE PROGRAM WE ARE GOING TO CREATE A TEST PROGRAM

def main():
    x=int(input("whats x-->"))
    print("x squared is--",square(x))

def square(x):
    ## SINCE THE PROGRAM RAN SUCCESSFULLY WHEN THE WRITTEN CODE WAS CORRECT, WE INSERTED A BUG ADDITIONALLY TO EXPERIMENT
    ## HERE x*x IS INTENTIONALLY CHANGED TO x+x
    return x+x

if __name__=="__main__":
    main()