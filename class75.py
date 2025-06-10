class Student:
    def __init__(self,n,h):
        self.name=n
        self.house=h
    
def main():
    student=get_student()
    print(student.name,student.house)

def get_student():
    name=input("NAME:")
    house=input("HOUSE:")
    ## ANOTHER WAY OF DOING THIS IS 
    return Student(name,house)

if __name__=="__main__":
    main()