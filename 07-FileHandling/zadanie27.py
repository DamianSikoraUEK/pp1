import re
file = open("grades.txt","r")
fileContent = file.read()
grades = re.findall("\d+\.\d+",fileContent)
arithmetic = 0
for i in grades:
    arithmetic = arithmetic + float(i)

arithmetic = arithmetic / len(grades)

print(arithmetic)