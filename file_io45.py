## FILE READING
with open("names.txt","r") as file:
    ## REMEBER ITS readlines() NOT readline() BOTH ARE DIFFERENT FUNC
    ## readline() READS ONLY THE FIRST ELEMENT AND PRINTS ITS EACH CHARACTER IN NEW LINE
    ## WHILE readlines() PRINTS ALL ELEMENTS EACH IN NEW LINE
    ## HERE line IS THE VARIABLE THAT STORES THE LINES

    line=file.readlines()
    ## HERE THE lines IS THE VARIABLE THAT GETS VALUE LINE BY LINE

    for lines in line:
        print(lines)

        ## THE PROBLEM WITH THIS CODE IS THAT IT PRINTS EXTRA NEW LINE THAT IS NOT REQUIRED
        ## FOR THIS PROBLEM WE USE rstrip() FUNCTION
    
    for lines in line:
     print(lines.rstrip())