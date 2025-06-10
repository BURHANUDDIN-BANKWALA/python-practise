## with IS ANOTHER KEYWORD THAT AUTOMATICALLY OPEN AND CLOSES A FILE
name=input("enter a name --->")

## HERE file IS A VARIABLE
with open("names.txt","a") as file:
    file.write(f"{name} \n")