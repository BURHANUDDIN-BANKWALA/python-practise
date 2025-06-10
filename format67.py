## TO IGNORE THE CASE WE CAN USE re.IGNORECASE FEATURE INSIDE THE re.search() FUNCTION
## THIS CODE WILL GENERATE ERROR BECAUSE THE FUNCTION IS CALLING THE GROUP THAT IS BEEN ASSOCIATED WITH THE www. AT THE FIRST PLACE
import re
url=input("URL:")
matches=re.search(r"^https?://(www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)

if matches:
    print(f"USERNAME: {matches.group(1)}")

## TO CORRECT THE CODE WE CAN INSERT matches.group(2) AT THE REQUIRED PLACE
