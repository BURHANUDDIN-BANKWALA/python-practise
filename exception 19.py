## pass KEYWORD PASSES THE VALUE True TO THE FUNCTION SIMILIAR TO continue 
while True:
    try :
        x=(int(input("int-->")))
        break
    
    except ValueError:
        pass

## prompt SEE IT AGAIN
def main():
   
   get_int()

def get_int():
 while True:
       try :
           return int(input("enter int"))
        
       except ValueError:
         pass

main()