## WE USE THE KEYWORD __str__ WHEN SOME FUNCTION WANTS TO SEE YOUR OBJECT AS STRING
class Student:
    def __init__(self,name,house):
        if not name:
            raise ValueError("NAME MISSING!!!")
        if house not in ["red","yellow","green","blue"]:
         raise ValueError("INVALID HOUSE!!!")
        self.name=name
        self.house=house

    def __str__(self):
       ## THIS FUNCTION WILL RETURN THE DATA TO THE main FUNCTION
       return f"{self.name} is from {self.house}"
    
def main():
   student=get_student()
   print(student)

def get_student():
   name=input("NAME-->")
   house=input("HOUSE-->")
   return Student(name,house)

if __name__=="__main__":
 main()