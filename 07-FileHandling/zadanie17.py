file = open("loremIpsum.txt","r")
fileWrite = open("copylines.txt","w")
for i in file:
    fileWrite.write(i)
file.close()
fileWrite.close()
