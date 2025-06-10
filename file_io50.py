students=[]

with open("students.csv") as file:
    for line in file:
        name,house=line.strip().split(",")

        ## WE WILL STORE THE DATA INSIDE A EMPTY DICTIONARY AS A KEY VALUE PAIR
        stu={}

        ## HERE WE WILL STORE THE name IN THE DICTIONARY WITH THE NAME name
        stu["n"]=name

        ## NOW WE WILL STORE THE house IN THE house
        stu["h"]=house

        ## NOW WE WILL STORE THE DICTIONARY IN EMPTY LIST students
        students.append(stu)
        ## SINCE NOW THE DATA IS STORED INSIDE THE EMPTY LIST WE WILL DISPLAY IT

## HERE s IS VARIABLE 
def get_name(s):
   return s["n"]

## HERE STUDENTS IS SENT TO THE get_name FUNCTION WHICH RETURNS THE NAME OF THE STUDENT
for student in sorted(students,key=get_name,reverse=True):
     print(f"{student['n']}is in {student['h']}")

     ## THE PROGRAM IS COMPLETED
     
