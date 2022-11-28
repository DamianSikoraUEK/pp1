import re
file = open("countries.txt","r")
file_content = file.read()
atLeastSix = re.findall("......+",file_content)
print(atLeastSix)