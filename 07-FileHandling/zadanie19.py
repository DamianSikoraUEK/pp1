file = open("AnotherIntegers.txt","w")
for i in range(1,51):
    if i == 50:
        file.write(str(i))
    else:
        file.write(str(i))
        file.write("\n")
file.close()