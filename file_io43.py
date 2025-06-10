##  TO OVERCOME THE PREVIOUS PROGRAM WE CAN SOLVE IT BY THIS METHOD

name=input("what is your name-->")

file=open("names.txt","a")
## HERE THE \n WILL INTRODUCE A NEW LINE TO THE FILE
file.write(f"{name} \n")
file.close()