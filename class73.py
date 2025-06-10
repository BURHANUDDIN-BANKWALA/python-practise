## CLASS IS THE TOOL IN OOP THAT ENABLES THE USER TO CREATE HIS OWN DATA TYPES
## THE SYNTAX TO DEFINE A CLASS IS class *Name*: 
## REMEMBER THAT THE NAME OF CLASS SHOULD HAVE THE FIRST ALPHABET CAPITAL
class Student:
    ## HERE THESE THREE DOTS ARE FOR SOME REASON
    ...

def main():
    student=get_student()
   ## HERE THE student IS COPY PASTED THE WHOLE CLASS WHICH HAS THESE name AND house VARIABLES 
    print(student.name,student.house)

def get_student():
    ## HERE THE EMPTY CLASS IS PASTED INSIDE THE VARIABLE THAT ACTS LIKE A CLASS NOW
    student=Student()
    ## NOW HERE THE student.name IS CREATING A NEW VARAIBLE INSIDE THE student 
    student.name=input("NAME:")
    student.house=input("HOUSE:")
    ## HERE THE student IS RETURNING A WHOLE CLASS
    return student

if __name__=="__main__":
 main()