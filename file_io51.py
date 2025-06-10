## csv IS ALSO A LIBRARY
import csv

students=[]
with open("students.csv") as file:
 ## HERE reader IS A VARIABLE
 reader=csv.reader(file)
 for name,house in reader:
      students.append({"name":name,"house":house})

 ## lambda FUNCTION IS USED WHERE A FUNCTION IS USED ONLY ONE TIME IN THE PROGRAM
 ## ITS SYNTAX IS lambda VAR: RETURN-VAR 
 ## WE CAN REMOVE THE REVERSE JUST BY CLEARING THE REVERSE COULMN
 
for stu in sorted(students,key=lambda students: students["name"],reverse=True):
         print(f"{stu['name']}is in{stu['house']}")