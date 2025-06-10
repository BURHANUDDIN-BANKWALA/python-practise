## NOW WE WILL RETRIEVE THE DATA FROM A FILE
## FIRST WE WILL CREATE AN EMPTY LIST TO STORE THE RETRIEVED DATA
names=[]
with open("names.txt") as file:
 ## HERE WE ARE NOT USING a,r OR w so by default it only reads the file

 ## HERE WE ARE DIRECTLY USING THE FILE VARIABLE WHICH STORES OUR FILE TEMPORARILY

 for line in file:
      ## NOW WE WILL STORE THE DATA IN OUR EMPTY LIST

     names.append(line.rstrip())

 ## NOW USING LOOP WE WILL PRINT THE DATA BUT BEFORE THAT WE WILL SORT IT DOWN USING sorted() FUNCTION
 ## WE CAN SORT IN OPPOSITE WAY ALSO AS sorted(namer, reverse=True) 
 for name in sorted(names):
     print(name)
     