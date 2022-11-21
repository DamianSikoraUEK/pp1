file = open("loremIpsum.txt","r")
i = 1
for line in file:
    if i <= 5:
        print(line)
        i = i+1
file.close()