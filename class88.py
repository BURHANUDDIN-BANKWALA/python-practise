## SIMILIAR TO THE PREVIOUS PROGRAM WE CAN DO IT ANOTHER WAY USING THE set() DATA STRUCTURE
students=[
    {"name":"Hermione","house":"Red"},
    {"name":"Harry","house":"Red"},
    {"name":"Ron","house":"Blue"},
    {"name":"Draco","house":"Green"}
]

houses=set()
for _ in students:
 ##    houses.append(_["house"])
 ## WE CAN'T USE .append() IN SET 
 ## WE NEED TO USE .add() FOR THE PURPOSE
 houses.add(_["house"])

for _ in sorted(houses):
 print(_ ,end=" ") 