## Creating a odd even func and calling it
def main():
    x=int(input("type an int"))
    print(odd_eve(x))

def odd_eve(a):
    if a%2==0:
        return("even")
    else:
        return("odd")
    
main()