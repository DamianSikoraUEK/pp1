fileFirst = open("MeatAndFish.txt","r")
fileSecond = open("GrainsAndBread.txt","r")
fileFinal = open("shoppinglist.txt","w")

for i in fileFirst:
    fileFinal.write(i)
fileFinal.write("\n")
for i in fileSecond:
    fileFinal.write(i)
fileFirst.close()
fileSecond.close()
fileFinal.close()