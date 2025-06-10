## to use exponentials we can use it as
## x**n or pow(x,n)
print(4**8)
print(pow(4,8))

## CONDITIONALS

## comparing two func using if 

def main():
    x=int(input("enter an int x "))
    y=int(input("enter an int y "))
    if x>y:
        print("x>y")
    if y>x:
        print("y>x")
    
## also we can do it using the elif :   
def main2():
 x=5
 y=9
 if x>y:
         print("ok")
 elif y>x:
      print("ok elif")


main()  
main2()     
