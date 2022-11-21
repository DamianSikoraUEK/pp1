file = open('numbers.txt','r')
suma = 0
for line in file:
    print(line,end="")
    suma = suma + int(line)
print("")
print(suma)
file.close()