import sys

if len(sys.argv)<2:
     sys.exit("too few args")

elif len(sys.argv)>2:
    sys.exit("too many args")

else :
 ## USING THE SYNTAX for arg in sys.argv[1:] SPECIFIES THAT THE arg VARIABLE SHOULD TAKE VALUE LEAVING THE FIRST INPUT THAT IS FILE NAME
 ## ALSO IF WE WANT TO REMOVE THE LAST INPUT WE CAN WRITE THIS AS for arg in sys.argv[1:-1] WHICH SPECIFIES REMOVAL OF FIRST AND THE FIRST FROM LAST ELEMENT ENTERED

 for arg in sys.argv[1: ] :
      print("hello I am", arg)