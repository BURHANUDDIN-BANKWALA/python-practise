## THERE ARE OTHER FUNCTIONS AVAILABLE IN PYTHONLIKE @staticmethod THAT CAN BE USED 
## INHERITENCE IS A PROPERTY OF OOP DUE TO WHICH WE CAN ACCESS ON OBJECT FROM ANOTHER OBJECT OR PARENT OBJECT
## TO USE A FUNCTION PRESENT IN ANOTHER CLASS THE SYNTAX IS class Student(*SUPERCLASS):
## ALSO USE THE SPECIFIC FUNCTION FROM THE SUPER CLASS WE USE super().__init__(*the variable that is to be sent in parent class) HERE THE __init__ IS THE DESIRED FUNCTION TO BE CALLED

class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("MISSING NAME!!!")
        self.name=name
        print(self.name)

class Student(Wizard):
 def __init__(self,name,house):
     super().__init__(name)
     self.house=house
     print(self.house)

class Professor(Wizard):
   def __init__(self,name,subject):
     super().__init__(name)
     self.subject=subject
     print(self.subject)

Wizard("albus")
Student("snape","slytherin")
Professor("snape","jadu-tona")