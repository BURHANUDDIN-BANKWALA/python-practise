import csv 
name=input("name--->").strip()
sal=input("sal--->").strip()
with open("workers2.csv","a") as file:
    writer=csv.DictWriter(file,fieldnames=["name","sal"])
    writer.writerow({"name":name,"sal":sal})

    ## THIS CODE WORKS PERFECTLY BUT THE EXTRA LINE IS CREATING ISSUES
    