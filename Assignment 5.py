import re
string=input("Enter a String")
if re.fullmatch(r'[a-zA-Z0-9]+',string):
    print("String contains only a-z A-Z 0-9")
else:
    print("String contains other characters")
