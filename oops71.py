def main():
    student=get_student()
 ## TUPLE ELEMENTS CAN BE ACCESSSED JUST LIKE LIST ELEMENTS 
    print(student[0],student[1])
    
def get_student():
    name=input("name:")
    house=input("house:")
    return (name,house)

if __name__=="__main__":
    main()
    