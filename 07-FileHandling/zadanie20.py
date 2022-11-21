file = open("integers.txt","w")

import random

for i in range(50):
    file.write(str(random.randint(100,999))+"\n")
file.close()
