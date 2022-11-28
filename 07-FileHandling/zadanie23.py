import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)

average = 0

for i in temperatures:
    average = average + int(i)

average = average // len(temperatures)

print(average)