## FLAGS
## WE CAN USE SYNTAX LIKE:
## re.IGNORECASE THIS IGNORES THE CASE OF THE STRING
## re.MULTILINE  IS USED WHEN MULTILINE STRINGS ARE NEEDED TO MATCH THE PATTERN 
## re.DOTALL     IT MATCHES EACH CHARACTER INCLUDING THE NEW LINE CHARACTER AND ID USED WHEN WE WANT TO MATCH PATTERN THAT SPAN ACROSS MULTIPLE LINES
import re
email=input("email--->")

if re.search(r"^\w+@\w+\.edu$",email,re.IGNORECASE):
 print("valid")

else:
 print("invlaid")

## WE HAVE SOME ANOTHER FUNCTIONS IN re THAT ARE re.match(PATTERN, STRING, flages=0) THIS RETURNS THE STRING IF THE MATCH IS FOUND AND IT ONLY 
## MATCHES THE START OF THE STRINGS
## NO NEED TO USE ^ IN THIS FUNCTION
## ALSO WE re.fullmatch() THIS FUNCTION MATCHES THE ENTIRE STRING SO NO NEED TO ADD ^ AND $