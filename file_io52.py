import csv
students=[]
with open("students.csv") as file:
    ## REMEMBER WHILE USING A DictReader() WE MUST HAVE HEADERS INSIDE OUR CSV FILE LIKE NAME AND HOUSE
    reader=csv.DictReader(file)
    for row in reader:
     students.append({"n":row["name"],"h":row["house"]})

for st in sorted(students, key = lambda stu: stu["n"]) :    
 print(f"{st['n']}is in{st['h']}")

     ## THE PROGRAM IS COMPLETED