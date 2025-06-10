## AN ANOTHER WAY IF EXTRACTING USERNAME COULD BE USING THE re.sub() FUNCTION
## THE SYNTAX IS re.sub(PATTERN, REPLACE, STRING, count=0, flags=0)

import re
url=input("URL:").strip()
username=re.sub(r"https://twitter.com/","",url)
print(username)

## HERE THE PROGRAM WILL INTERPRETE THE DOT AS ANY CHARACTER

username=re.sub(r"^https://twitter\.com/","",url)
print(username)  

## BUT IF THE USER INSERTED THE URL IN http FORMAT THEN THE CODE WILL BREAK
username=re.sub(r"^(http|https)://twitter\.com/","",url)
print(username)

## AN ANOTHER WAY COULD BE
username=re.sub(r"^https?://(www\.)?twitter\.com/","",url)
print(username)

## ALSO AN ANOTHER WAY COULD BE 
## THIS CODE SAYS THAT EITHER THERE WILL BE www. OR NOTHING
username=re.sub(r"^https?://(www\.|)twitter\.com/","",url)
print(username)

