## LISTS
## THE [] REPRESENTS THE LIST AND LOOP WILL RUN TILL ALL THE NO. OF VALUES INSIDE THE LIST IS GONE THROUGH

for i in [0,1,3]:
    print("hi")

## RANGE
## INSTEAD OF TYPING NO.S WE CAN USE RANGE TO PRINT MULTIPLE TIMES
## RANGE RUNS TILL THE n GIVEN. EX IF range(1) THEN "HELLO"

for i in range(3):
    print("hello")

## WHEN A VARIABLE IS NEEDED TO BE DEFINED IN PYTHON BUT HAS NO MEANING OF ITS NAMING WE CAN USE _ UNDERSCORE INSTEAD OF NAMING THEM
for _ in range(5):
    print("go")

## ALSO WE CAN SIMPLY USE THIS TECCHNIQUE
print("start"*2)

## BUT THIS DOESNT ADD ANY SPACE AND NEW LINE SO WE CAN USE THIS TECHNIQUE
## HERE MENTION A COMMA BETWEEN end AND THE REPEATED ARGUMENT 
print("jupyter \n"*3, end="")

## IF WE NEED TO PRINT ELEMENTS OF THE LIST FROM BACK WE CAN USE THIS SYNTAX
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

## IF WE NEED TO ADD AN ELEMENT AT A PARTICULAR POSITION IN THE LIST THEN WE CAN DO IT AS FOLLOWS
motorcycles = ['honda', 'yamaha', 'suzuki'] 
motorcycles.insert(0, 'ducati')
print(motorcycles)

## WE CAN ALSO REMOVE ELEMENTS FROM THE LIST AS
del motorcycles[0] 
print(motorcycles)

## pop FUNCTION REMOVES THE LAST ELEMENT FROM THE LIST AND RETURNS THE POPPED ELEMENT
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycle)

## TO POP THE ELEMENT FROM A PARTICULAR POSITION WE CAN DO IT AS
x=motorcycles.pop(1)
print(x)

## remove("ELEMENT") FUNCTION CAN BE USED TO REMOVE THE ELEMENT USING ITS  VALUE 
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

##The remove() method deletes only the first occurrence of the value you specify. If there’s 
##a possibility the value appears more than once in the list, you’ll need to use a loop to 
##determine if all occurrences of the value have been removed.