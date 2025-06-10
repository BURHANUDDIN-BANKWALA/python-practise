## NON CAPTURING GROUPS (?....)
## IN THESE TYPES OF GROUPS WE GROUP THE CHARACTERS AND OTHER USEFUL ELEMENTS BUT FIX THEM TO NOT ASSOCIATE AS "SPECIAL" WHILE CALL THE GROUPS
import re
url=input("URL:")
matches=re.search(r"^https://(?:www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)
print(matches.groups(1))

## THERE ARE OTHER FUNCTIONS IN THE re LIBRARY SUCH AS re.findall()