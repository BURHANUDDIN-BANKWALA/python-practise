## sys.exit() IS A FUNCTION IN sys LIBRARY THAT EXITS THE PROGRAM
## SIMILIAR TO THE PREVIOUS PROGRAM THIS ALSO NEEDS SOME CONSIDERATIONS
import sys

if len(sys.argv)<2:
    sys.exit("too few args")

elif len(sys.argv)>2:
   sys.exit("too many args")

else:
    print("hello I am", sys.argv[1])

## TO IMPORT EVERY INPUT THAT HAS BEEN ENTRED
 
if len(sys.argv)<2:
    sys.exit("too few args")

elif len(sys.argv)>2:
   sys.exit("too many args")

else:
    for arg in sys.argv:
     print("hello I am", arg)

## BUT THIS DOUBLE PRINTS THE FILE NAME
## SO
## THE NEXT PROGRAM MAY NOT RUN IN THIS FILE BUT IS SUCCESSFUL IN NEW FILE BECAUSE THE PREVIOUS WRITTEN CODE IS INTERVAINING 
## BEFORE THIS CODE RUNS

if len(sys.argv)<2:
     sys.exit("too few args")

elif len(sys.argv)>2:
    sys.exit("too many args")

else :
 ## USING THE SYNTAX for arg in sys.argv[1:] SPECIFIES THAT THE arg VARIABLE SHOULD TAKE VALUE LEAVING THE FIRST INPUT THAT IS FILE NAME
 ## ALSO IF WE WANT TO REMOVE THE LAST INPUT WE CAN WRITE THIS AS for arg in sys.argv[1:-1] WHICH SPECIFIES REMOVAL OF FIRST AND THE FIRST FROM LAST ELEMENT ENTERED

 for arg in sys.argv[1: ] :
      print("hello I am", arg)