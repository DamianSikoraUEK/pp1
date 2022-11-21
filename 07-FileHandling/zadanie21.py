file = open("powers.txt","w")
for i in range(1,11):
    file.write(str(i))
    file.write(" ")
    file.write(str(i*i))
    file.write(" ")
    file.write(str(i*i*i))
    file.write("\n")
file.close()