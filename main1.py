## to print we use print("")
## to scan or take input we use input()
## take the name of user and print hello
## one space after the question mark to give space while inputting 

name=input("What is your name? ")
print("hello")

## now hello with the name input
## the comma between the inverted commas and name specifies that the these are seprate things also it automatically separates the two with a space
## here automatic settings adds space to the name
print("hello,",name,"!")

## syntax of print is print(*object , sep=" ",end"\n")

## to print in inverted commas use backslash ##
print("hello \"friend\"")

## format string is special symbol that hints the compiler to know that this line of code needs SPECIAL consideration


print(f"hello {name}")

# to REMOVE EMPTY SPACES from the left side strip() is used with a dot attached with the variable to strip
name=name.strip()
print(f"{name} is after the strip")

# to CAPITALIZE THE USERS NAME we use .capitalize()
# it only capitalizes the FIRST LETTER of the FIRST WORD
name=name.capitalize()
print(f"{name} this is after capitalization")

# for the capitalization of EVERY FIRST LETTER of WORDS we use .title()
name=name.title()
print(f"{name} this is after using title")

#chaining two parameters
name=name.strip().title()

## also we can directly add to the variable or string
name=input("what's your name ?").strip().title()
print(f"{name} this is after chaining")

# to split the name into two ie first and last we use .split() function
first,last=name.split()
print(first)
print(last)

## TO CONVERT EITHER EACH WORD TO CAPITAL OR SMALL WE CAN USE
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

## IF WE NEED A INT IN STRING THEN
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)