##LISTS
students = ["alif","be","te","se","jeem"]
n=0
while n>=0 and n<=4:
 print(students[n])
 n=n+1

## ANOTHER WAY
## THIS PRINTS IN THE SQUARE BRACKETS AS WELL AS IN INVERTED COMMAS
employee=["a","b","c"]
print(employee)

## ONE ANOTHER WAY
## USING len() FUNCTION WE CAN FIND OUT THE LENGTH OF THE LIST AND PUT IT IN RANGE

workers=["ron","harry","tommy"]
for i in range(len(workers)):
 print(i+1,workers[i])

## WE CAN ALSO DO THIS BY DECLARING A VARIABLE IN THE for LOOP 
## SUCH THAT IT TAKES THE VALUE OF EACH ELEMENT OF LIST AND PRINTS IT TILL ALL THE ELEMENTS ARE NOT PRINTED
work =["a","b","c"]
for i in work:
 print(i)