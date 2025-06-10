## WE CAN DEFINE OUR OWN ERRORS IN CLASSES USING THE raise KEYWORD 
class Student:
    def __init__(self,n,house):
        if not n:
            raise ValueError("MISSING NAME!!!")
        if house not in ["RED","YELLOW","GREEN","BLUE"]:
            raise ValueError("INAVALID HOUSE!!!")
        
        self.name=n
        self.house=house

def main():
    student=get_student()
    print(student.name,student.house)

def get_student():
    name=input("ENTER NAME---")
    house=input("ENTER HOUSE---")
    student=Student(name,house)
    return student

if __name__=="__main__":
    main()

    