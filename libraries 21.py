## from IS A KEYWORD THAT IMPORTS A SPECIFIC FUNCTION FROM THE MODULE 
## REMEMBER THERE ARE NO BRACES IN FUNCTION CALLING FROM THE MODULE 

from random import choice
coin =choice(["heads","tails"])
print(coin)

## randint(a,b) IS A FUNCTION IN RANDOM LIBRARY THAT GIVES YOU A INT BETWEEN a AND b INCLUDING a AND b
import random
number=random.randint(0,10)
print(number)

## shuffle(x) SHUFFLES THE INPUT LIST
cards=["king","queen","joker","ace"]
random.shuffle(cards)
for i in cards:
    print(i)