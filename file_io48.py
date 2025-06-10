## csv  ARE ANOTHER TYPES OF FILE SYSTEM LIKE TEXT WHICH STORES DIFFERENT DATA WITH A INCLUDED COMMA IN IT
## HERE WE WILL CREATE AN csv FILE BY TYPING code students.csv IN THE TERMINAL

## NOW WE WILL INPUT SOME DATA IN THAT csv FILE MANUALLY ALSO REMEMBER TO SAVE THE csv FILE OR CODE WON'T WORK
## NOW WE WILL PRINT THE DATA

with open("students.csv") as file:

    ## HERE line IS A VARIABLE THAT WILL STORE INFO LINE BY LINE
    for line in file:

        ## HERE row IS A VARIABLE THAT WILL SPLIT THE NAME AND HOUSE INTO TWO AND STORE IT AS A LIST
        row=line.rstrip().split(",")

        ## THE NEXT SYNTAX WILL PRINT THE NAME AND HOUSE
        print(f"{row[0]}is in{row[1]}")

## WE CAN ALSO DO IT AS
with open("students.csv") as file:
     
 for line in file:
      name,house=line.rstrip().split(",")
      print(f"{name}is in{house}")

## AN ANOTHER WAY TO DO IT IS AS FOLLOWS
## CREATING AN EMPTY LIST TO STORE THE INFORMATION FROM THE FILE
students=[]

with open("students.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")

        ## INSERTING THE RETRIEVED INFO INTO THE LIST
        students.append(f"{name}is in{house}")


    for student in sorted(students):
        print(student)
