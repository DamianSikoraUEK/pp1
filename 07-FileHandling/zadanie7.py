file = open('countries.txt','r')
# file_content = file.read()
i = 1
for line in file:
    print(i,line,end="")    
    i = i+1
file.close()
