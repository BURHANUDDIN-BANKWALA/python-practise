## THE PREVIOUS PROGRAMS ARE STILL IMPROPER 
## re IS A LIBRARY THAT STANDS FOR REGULAR EXPRESSIONS
import re

## IN THIS re LIBRARY WE HAVE A FUNCTION CALLED search(PATTERN , STRING , flags=0)

email=input("email--->").strip()

## IN re.search("@",email) @ is the pattern we need to search in the email
if re.search("@",email):
    print("valid")

else :
    print("invalid")

import re
email=input("email--->").strip()

## HERE 
## . IS USED FOR ANY CHARACTER EXCEPT A NEW LINE
## * IS USED FOR 0 OR MORE REPETITIONS
## + IS USED FOR 1 OR MORE REPETITIONS
## ? 0 OR 1 REPETITIONS
## {M} M REPETITIONS
## {M-N} M TO N REPETITIONS

if re.search(".*@.*",email):
    ## THIS CODE WILL NOT GENERATE ANY ERROR IF ONLY @ IS TYPED
    print("valid")

else :
    print("invalid")

## HERE SOME CORRECTIONS ARE MEANT TO BE DONE
## THIS CODE WILL GENERATE ERROR IF ONLY @ IS TYPED
if re.search("..*@..*",email):
 print("valid")

else :
   print("invalid")

## WE CAN USE .+@.+ INSTEAD ..*@..*
if re.search(".+@.+",email):
   print("valid")

else :
   print("invalid")

## THIS CODE STILL WORKS WITH ASD@ASDF