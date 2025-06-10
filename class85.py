class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house
        
    def __str__(self):
        return f"{self.name} is from {self.house},{self}"
    
    @classmethod
    def get(cls):
     name=input("NAME--->")
     house=input("HOUSE--->")
     return cls(name,house)
    
def main():
   student=Student.get()
   print(student.name)

main()