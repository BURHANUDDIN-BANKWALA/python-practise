class Accnt:
    def __init__(self):
        self._balance=0
    
    def balance(self):
        return self._balance

    def deposit(self,n):
        self._balance+=n
    
    def withdraw(self,n):
        self._balance-=n

def main():
    accnt=Accnt()
    print("Balance: ",accnt._balance)
    accnt.balance()
    print("Balance: ",accnt._balance)
    accnt.deposit(50000)
    print("Balance: ",accnt._balance)
    accnt.withdraw(40000)
    print("Balance: ",accnt._balance)

main()