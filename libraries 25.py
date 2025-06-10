## SIMILIAR TO REMOVAL OF THE FIRST ELEMENT OF sys.argv[1:] WE CAN REMOVE LAST ELEMENTS ALSO BY USING SYNTAX sys.argv[1:-1]
## HERE NEGATIVE NO.S SLICES REMOVES THE NO OF STRINGS FROM BEHIND

import sys
if len(sys.argv)<2:
    print("too few args")

for arg in sys.argv[1:-2]:
    print(arg)
