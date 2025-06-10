## SIMILIAR TO THE PREVIOUS PROGRAM WE CAN UPDATE IT LITTLE BIT 
def get_int():
    while True: 
     try :
         x=int(input("ENTER A INT ---->"))
      
     except ValueError :
       print("THE INPUT IS INVALID")

         ## NOW HERE INSTEAD OF USING break WE CAN DIRECTLY USE return() WHICH WILL DIRECTLY BREAK THE LOOP
     else :
         return(x)
     
get_int()