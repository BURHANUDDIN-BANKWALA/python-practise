## HERE WE WILL UPDATE THE PROGRAM BY DOUBLE CHECKING THE PROGRAM
email=input("email---->")

if "@" in email:
 
 ## HERE WE WILL SPLIT THE email BY USING split() FUNCTION ACROSS THE @ CHARACTER
 username,domain=email.split("@")

 ## HERE WE WILL CHECK THE BOOLEAN CONDITION IF IT IS TRUE AND ALSO WE CHECK THAT . IS PRESENT IN THE DOMAIN
 if username and "." in domain:
     print("valid")

 else :
     print("invalid")

else :
   print("invalid")


## ALSO WE CAN  FURTHER UPDATE THE PROGRAM SUCH THAT THE EMAIL
## HERE IN THIS PROGRAM WE WILL CHECK IF .edu IS PRESENT IN THE email

email=input("email--->").strip()
username,domain=email.split("@")

## endswith() IS A FUNCTION THAT CHECKS WHETHER GIVEN VARIABLE ENDS WITH A PARTICULAR STRING
if username and domain.endswith(".edu"):
   print("valid")

else :
   print("invalid")