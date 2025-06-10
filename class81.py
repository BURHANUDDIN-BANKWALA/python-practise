## @property IS A KEYWORD IN PYTHON THAT ALLOWS US PROHIBIT THE USER TO ABRUPTLY CHANGE THE INFORMATION PROVIDED 
class Student:
    def __init__(self,n,h):
        if not n:
            raise ValueError("MISSING NAME!!!")
        ## INSTEAD OF WRITING THIS CODE WE WILL ERROR CHECK IN GETTER AND SETTER
        ##if house not in ["red","yellow","green","blue"]:
        ##  raise ValueError("INVALID HOUSE")
        self.name=n
        self.house=h

    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    ## GETTER FUNCTION
    ## TO SET THE GETTER FUNCTION FIRST WE WILL TYPE @property ABOVE THE FUNCTION TO DENOTE IT AS GETTER FUNCTION
    ## GETTERS AND SETTERS ARE USED TO ENCAPSULATE THE DATA INSIDE THE PROGRAM
    ## BY USING GETTERS WE CAN MAKE THE DATA ONLY READABLE AND USING SETTERS WE CAN CHECK IF THE DATA BEING INPUT IS VALID OR NOT

    @property
    def house(self):
        ## HERE WE HAVE USED AN _ TO DIFFERENTIATE IT WITH THE ORIGINAL VARIABLE SO IT DOES NOT CREATES ERROR
        ## WE NEED A NEW VARIABLE HERE BECAUSE THE ONE WE WERE TRYING USE WAS ALREADY DECLARED
        return self._house
    
    @house.setter
    ## REMEMBER THAT WHEN WE CREATE SETTER WE NAME IT THE SAME AS THE FUNCTION NAME WE CREATED FOR GETTER AS SYNTAX
    def house(self,h):
        if h not in ["red","green","yellow","blue"]:
            raise ValueError("INVALID HOUSE!!!")
        self._house=h

def main():
    student=get_student()
    print (student)

def get_student():
    n=input("NAME--->")
    h=input("HOUSE--->")
    return Student(n,h)

main()