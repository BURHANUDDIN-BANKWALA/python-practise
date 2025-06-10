## NOW UNLIKE PREVIOUS CODE WE CAN DIRECTLY SORT AND ALLOCATE HOUSE TO THE INPUT NAME
import random
class Hat:
    houses=["R","G","B","Y"]
    @classmethod
    ## REMEMBER THAT WE USED cls INSTEAD OF self OR class BECAUSE WE ARE USING CLASS METHOD AND ON OTHER HAND CLASS IS A KEYWORD
    def sort(cls,name):
        print(name,"is in",random.choice(cls.houses))

Hat.sort("HARRY")

## THERE IS AN ANOTHER FUNCTION CALLED type() THAT RETURNS THE TYPE OF VALUE THAT HAS BEEN FEEDED INSIDE OF IT
print(type("hi"))