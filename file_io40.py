## TO STORE MULTIPLE NAMES IN THE LIST WE FIRST CREATE AN EMPTY LIST
names=[]

## NOW TO INPUT MULTIPLE NAMES INSIDE THIS LIST WE USE A LOOP WITH A RANGE
for _ in range(3):
    name=input("enter a name-->")
    ## HERE THE append() FUNCTION WILL JOIN OUR input IN THE LIST
    names.append(name)

## NOW HERE THE sorted() FUNCTION WILL SORT THE NAMES INSIDE THE LIST
for i in sorted(names):
 print(f"heyyyy, {i}")
 