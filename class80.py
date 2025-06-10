class Student:
    def __init__(self,n,h,p):
     if not n:
         raise ValueError("MISSING NAME!!!")
     if h not in ["RED","YELLOW","GREEN","BLUE"]:
         raise ValueError("INVALID HOUSE!!!")
      
     self.name=n
     self.house=h
     self.patronus=p

    def __str__(self):
       return f"{self.name} is from {self.house}"
    
    def charm(self):
       match self.patronus:
          case "stag":
             return "horse"
          case "otter":
             return "mouse"
          case _:
             return "sssswisssshhhhh"
          
def main():
   student=get_student()
   print(student)
   print("EXXXPECCTO PETRRRONUM")
   print(student.charm())

def get_student():
   name=input("NAME--->")
   house=input("HOUSE--->")
   patronus=input("PATRONUS--->")
   return Student(name,house,patronus)

main()