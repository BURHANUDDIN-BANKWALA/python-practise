## AN ANOTHER WAY DOING THIS IS BY
def main():
    student=get_student()
    print(student["name"],student["house"])
    
def get_student():
    ##HERE WE HAVE CREATED AN EMPTY DICTIONARY AND IT STORE THE NAME AND HOUSE AS THE VALUES
    stud={}
    stud["name"]=input("name:")
    stud["house"]=input("house:")
    return (stud)

if __name__=="__main__":
    main()
    