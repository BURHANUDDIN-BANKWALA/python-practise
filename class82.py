class Student:
    def __init__(self,n,h): 
        self.name=n
        self.house=h

    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    ## SIMILIAR TO THE PREVIOUS PROGRAM WE CAN CREATE GETTERS AND SETTERS FOR NAME ALSO
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
 
      if name=="":
        raise ValueError("MISSING NAME")
      self._name=name


    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self,h):
        if h not in ["red","green","yellow","blue"]:
            raise ValueError("INVALID HOUSE!!!")
        self._house=h

def main():
    student=get_student()
    print (student)

def get_student():
    n=input("NAME--->")
    h=input("HOUSE--->")
    return Student(n,h)

main()