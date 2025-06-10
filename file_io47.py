## WE CAN USE ANOTHER WAY TO PRINT THE DATA

with open("names.txt") as file:
    for line in sorted(file):
        print(f"{line.rstrip()}")