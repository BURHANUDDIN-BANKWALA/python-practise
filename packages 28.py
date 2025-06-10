import json
import requests
import sys

if len(sys.argv)!=2:
    sys.exit()

## response IS THE VARIABLE THAT COLLECTS THE INFO FROM THE WEB
response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])

## HERE json.dumps() CONVERTS THE FILE INTO NEAT FORMAT TO EASILY READ
## HERE indent=2 CREATES SPACES BETWEEN DIFFERENT KEY AND VALUE PAIRS TO READ EASILY
print(json.dumps(response.json(),indent=2) ) 


o=response.json()
for result in o["results"]:
    print(result["trackName"]) 

    ## THIS PROGRAM IS COMPLETED