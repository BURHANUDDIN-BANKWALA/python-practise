name= input("NAME:")
house=input("HOUSE:")
print(f"{name} is from {house}")

## NOW INSTEAD TYPING INPUTS AND CREATING VARIABLES AGAIN AND AGAIN WE CAN JUST CREATE FUNCTIONS
def main():
 name= get_name()
 house= get_house()
 print(f"{name} is from {house}")

def get_name():
 return(input("ENTER NAME:"))

def get_house():
 return (input("ENTER HOUSE:"))

if __name__=="__main__":
 main()