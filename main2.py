#concatenation error

## if input is used like this it will treat as string
x=input("enter an integer x ")
y=input("enter an integer y ")
z=x+y
print(z)

## to solve this error we can convert the string into int
z=int(x)+int(y)
print(z)

## we can also solve this by
p=int(input("p? "))
q=int(input("q? "))
r=p+q
print(r)

#similarily float() can be used
p=float(p)
print(p)