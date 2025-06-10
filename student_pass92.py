age=int(input('Enter Your Age:'))
is_student=input('Are You A Student? (yes/no)').lower()

if age<26 and age>18:
    if is_student=='yes':
        fare=30
    else :
        fare=50

if age<18:
    fare=0

if age>26:
    fare=56

print(fare)