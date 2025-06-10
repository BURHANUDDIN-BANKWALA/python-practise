class Student:
    ## WE HAVE CREATED A FUNCTION THAT IS BEEN CALLED WHENEVER THE CLASS Student IS CALLED 
    ## IT IS KNOWN AS CONSTRUCTOR
    ## HERE __init__ IS THE DEFAULT SETTINGS DONE BY THE PYTHON AUTHORS THAT STANDS INITIALIZATION INSTANCES
    ## ALSO HERE THE self IS AN DEFAULT CONVENTION THAT MUST BE TYPED FIRST 
    ## THE self STORES THE OTHER VARIABLE INSIDE THE CLASS
    def __init__(self,n,h):
        self.name=n
        self.house=h
    
def main():
    student=get_student()
    print(student.name,student.house)

def get_student():
    name=input("NAME:")
    house=input("HOUSE:")
    student=Student(name,house)
    return student

if __name__=="__main__":
    main()