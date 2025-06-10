## MAKING MY OWN LIBRARY
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

## AFTER CORRECTION : WE ADD if __name__=="__main__":
if __name__=="__main__":
 main()
## NOW FROM THIS FILE WE WILL IMPORT hello() AND goodbye() FUNCTIONS