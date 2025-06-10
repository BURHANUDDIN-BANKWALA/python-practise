## OPERATOR OVERLOADING
## HERE IN THE CODE WE CREATED A LIST OF DICTIONARIES WITH NAMES AND HOUSES OF STUDENTS.
## NOW WE CREATE A NEW LIST TO FIND ALL THE HOUSES PRESENT IN THE PREVIOUS LIST.
## IN THE NEW LIST WE CREATED A LOGIC TO CHECK WHETHER HOUSES ARE PRESENT IN THE NEW LIST IF NOT WE USE .append() FUNCTION 
students=[
    {"name":"Hermione","house":"Red"},
    {"name":"Harry","house":"Red"},
    {"name":"Ron","house":"Blue"},
    {"name":"Draco","house":"Green"}
]

houses=[]
for stud in students:
    if stud["house"] not in houses:
        houses.append(stud["house"])

for _ in houses:
    print( _ ,end=" ")