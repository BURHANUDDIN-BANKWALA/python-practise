## HERE IN THIS PROGRAM WE WILL SPECIFY TO END THE EMAIL WITH .edu

import re
email=input("email--->").strip()

## IN THE re.search() WE WILL FIND OUT IF THERE ARE ANY CHARACTERS ON THE LEFT OF @ AND ON THE RIGHT OF THE @ ALSO IT MUST END WITH .edu
## HERE THE USE OF \.edu IS DONE TO SPECIFY THAT .edu IS A LITERAL SYMBOL TO BE CHECKED IN THE EMAIL

if re.search(".+@.+\.edu",email):
    print("valid")

else :
    print("invalid")

## CODE IN SUCCESS STILL SHOWS A SLIGHT WARNING OF SYNTAX WHICH CAN BE RESOLVED BY ADDING RAW STRING IN THE search() FUNCTION
## HERE RAW STRING TELLS THAT THE BACKSLASH IS REFFERING TO A PARTICULAR TYPE OF SYMBOL OR EXPRESSION
if re.search(r".+@.+\.edu",email):
    print("v")

else:
    print("iv")

## FURTHER THE CODE WOULD VALIDATE IF MULTIPLE @@@ ARE ADDED
## WE CAN SOLVE THIS BY
if re.search(r".+@.+\.edu",email):
    print("V")

else:
    print("IV")

## MORE RECONSIDERATIONS REQUIRED
