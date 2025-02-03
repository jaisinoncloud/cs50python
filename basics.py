import re

'''
email = input("What is yor mail id? ")

if re.search(r"^\w+(\.\w*)?@(\w+.\)?\w+\.com",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
'''

'''
name = input("What is your name? ")

if searches := re.search(r"^(.+), *(.+)$",name,re.IGNORECASE):
    lname,fname = searches.groups()
    print(fname, lname)
'''

username = input("What is your username? ")
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)",username):
    print(matches.group(1))