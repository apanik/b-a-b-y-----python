import re

string = "at what time?"
match = re.search('time',string)
if (match):
    print "String found at: " ,match.start()
else:
    print "String not found!"