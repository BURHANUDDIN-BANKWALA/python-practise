import csv
name=input("enter name--->").rstrip()
sal=input("enter sal---->").rstrip()

with open("workers.csv","a") as file:
    writer=csv.writer(file)
    writer.rstrip()
    writer.writerow([name,sal])
    ## MORE RECONSIDERATION IS REQUIRED FOR THIS PROGRAM