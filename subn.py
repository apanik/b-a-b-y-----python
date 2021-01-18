import re

myC = re.compile('[a-z]') 
myS = myC.findall("Hello, Said Anik")
print(myS)
