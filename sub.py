import re

string = "at what time?"
match = re.sub("\s","!!!",string)
print (match)