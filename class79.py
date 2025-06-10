## HERE WE WILL ADD THE PATRONUS ALSO
class Student:
    def __init__(self,name,house,patronus):
        if not name:
            raise ValueError("NAME MISSING!!!")
        if house not in ["red","yellow","green","blue"]:
         raise ValueError("INVALID HOUSE!!!")
        self.name=name
        self.house=house
        self.patronus=patronus

    def __str__(self):
       ## THIS FUNCTION WILL RETURN THE DATA TO THE main FUNCTION
       return f"{self.name} is from {self.house}"
    
def main():
   student=get_student()
   print(student)

def get_student():
   name=input("NAME-->")
   house=input("HOUSE-->")
   patronus=input("ENTER PATRONUS-->")
   return Student(name,house,patronus)

if __name__=="__main__":
 main()