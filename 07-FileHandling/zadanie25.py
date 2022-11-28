import re

message = "To be, or not to be, that is the question"
spaces = re.findall(" ",message)

words = len(spaces) + 2

print(words)