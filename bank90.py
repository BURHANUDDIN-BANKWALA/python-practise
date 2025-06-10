## HERE THE balance IS GLOBAL KEYWORD
balance=0
def main():
    print("Balance: ",balance)
    deposit(100)
    withdraw(50)
    print("Balance: ",balance)

def deposit(n):
   ## TO CHANGE THE VALUE IN THE GLOBAL VARIABLE WE NEED TO USE THE global KEYWORD TO FIRST RECALL THAT THE VARIABLE IS GLOBAL 
   ## AND THEN WE WILL MODIFY THE DATA INSIDE THE VARIABLE IN THE NEXT LINE
   global balance
   balance +=n

def withdraw(n):
   global balance
   balance -=n

main()