## OR ELSE WE CAN CREATE A WHOLE FUNCTION THAT ASKS FOR THE NAME AND THE HOUSE
def main():
    name,house=get_student()
    print(name,house)
    
def get_student():
    name=input("name:")
    house=input("house:")
 ## HERE WE ARE USING A TUPLE TO RETURN THE VALUES
 ## THE TUPLES ARE SIMILIAR TO LIST BUT CANT BE CHANGED BY SOMEONE
 ## THEY ARE IMMUTABLE 
    return (name,house)

if __name__=="__main__":
    main()
