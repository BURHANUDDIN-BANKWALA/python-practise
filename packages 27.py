## API STANDS FOR APPLICATION PROGRAMMING INTERFACE
## requests IS A LIBRARY USED FOR WEB REQUESTS
## TO INSTALL requests LIBRARY TYPE pip install requests IN THE TERMINAL WINDOW
## JSON FILE TYPE IS USED TO EXCHANGE DATA BETWEEN THE COMPUTERS
import requests
import sys 

if len(sys.argv)!=2:
    sys.exit("oops too few args")

## HERE RESPONSE IS A VARIABLE THAT WILL STORE THE DATA COLLECTED FROM THE INTERNET
## HERE requests IS A LIBRARY AND get IS A FUNCTION INSIDE IT WHICH SEARCHES THE WEB A GIVES RESULTS
## MENTION AS THE sys.argv[1]
response=requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1])    
print(response.json())

## THE CODE  WORKS ABSOLUTELY FINE BUT DOESN'T DISPLAY THE RESULTS IN READABLE FORMAT
