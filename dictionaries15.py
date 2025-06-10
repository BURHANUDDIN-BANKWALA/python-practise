## DICTIONARIES
## IN DICTIONARIES WE CAN ADD KEY-VALUE PAIRS 
## WE USE CURLY BRACKETS TO DEFINE A DICTIONARY
students={
    "harry":"red",
    "ron":"red",
    "draco":"green"
}
for stu in students:
 ## REMEMBER TO USE SQUARE BRACKETS INSTEAD OF ROUND BRACKETS JUST LIKE LISTS
 print(stu,students[stu] , sep=" ,")

## LISTS OF DICTIONARIES
## WE CAN MAKE LIST OF DICTIONARIES
employee=[
 {"name":"a","id":"1","sal":"10"},
 {"name":"b","id":"2","sal":"20"},
 {"name":"c","sal":"30","id":"3"}
]

##THIS SYNTAX PRINTS THE WHOLE LIST IN TABULAR FORMAT
for emp in employee:
 print(emp)

## BUT TO PRINT IT IN SEPARATE FORMAT WE NEED TO ENTER THE KEYS IN THE LIST SQUARE BRACKETS
## print(stu["name"],stu["id"],stu["sal"])
## REMEMBER THAT STU IS DEFINED INSIDE THE FOR LOOP AND IS NOT THE NAME OF LIST
for empl in employee:
 print(empl["name"],empl["sal"],empl["id"])


 ##THE NEXT SYNTAX CREATES ERROR ON EXECUTION IN LIST OF DICTIONARIES
 ##print(empl,employee[empl])
 ## THIS IS BECAUSE IT ASSUMES THE WHOLE DICTIONARY AS A KEY 
 ## NOW FOR FURTHER CLASSIFICATION USER ENTERS THE KEY PRESENTED IN THAT DICTIONARY TO GET ITS VALUE
 