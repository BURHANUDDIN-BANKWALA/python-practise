import re
name=input("name").strip()
matches=re.search(r"^(.+), (.+)$",name)

if matches :
    ## HERE THE GROUPING OF (.+) AUTOMATICALLY HINTS THE groups() FUNCTION TO TREAT THEM SPECIALLY AS DIFFERENT GROUPS
    last,first=matches.groups()
    name=f"{first} {last}"
print(f"hello {name}")

## ANOTHER WAY OF DOING THIS WOULD BE
last=matches.groups(1)
first=matches.groups(2)
name=f"{first} {last}"
## THE ERROR HERE GENERATED IS THAT IT PRINTS THE GROUPS TWO TIMES
print(name)

## ANOTHER SYNTAX COULD BE
name=matches.groups(1)+matches.groups(2)
print(name)