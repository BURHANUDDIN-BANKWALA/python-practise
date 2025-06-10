students=[]
with open("students.csv") as file:
    for line in file:
        name,house=line.strip().split(",")

        ## WE WILL STORE THE DATA INSIDE A EMPTY DICTIONARY AS A KEY VALUE PAIR
        student={}

        ## HERE WE WILL STORE THE name IN THE DICTIONARY WITH THE NAME name
        student["name"]=name

        ## NOW WE WILL STORE THE house IN THE house
        student["house"]=house

        ## NOW WE WILL STORE THE DICTIONARY IN EMPTY LIST students
        students.append(student)



## WE CAN ALSO WRITE IT AS
with open("students.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")

        ## HERE WE ARE DIRECTLY STORING THE DATA INSIDE THE DICTIONARY
        student={"name":name,"house":house}
        students.append(student)
    
for student in students:
    print(f"{student['name']}is in {student['house']}")