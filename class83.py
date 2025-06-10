## CLASS METHODS ARE USED TO DIRECTLY CREATE VARIABLES AND USE THEM WITHOUT CREATING ANY OBJEC/FUNCTION IN A CLASS IF THE VARIABLE IS IN USE MORE GENERALLY
## TO DENOTE CLASS METHODS THE SYNTAX USED IS @classmethod
import random

class Hat:
    def __init__(self):
        self.houses=["red","green","blue","yellow"]

    def sort(self,name):
        print(name,"is in",random.choice(self.houses))

hat=Hat()
hat.sort("harry")