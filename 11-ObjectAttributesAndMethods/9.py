import random

class Arrays():

    @staticmethod
    def a (number,value):
        list = []
        for i in range(1,number+1):
            list.append(value)
        print(list)

    @staticmethod
    def b (number,valuefr,valueto):
        list = []
        for i in range(1,number+1):
            list.append(random.randint(valuefr,valueto))
        print(list)

    @staticmethod
    def c(array,valuefr,valueto):
        contents  = 0
        list = []
        for i in range(1,array+1):
            list.append(random.randint(-7,8))
        for i in list:
            if i >= -1 and i <= 1:
                contents = contents+1
        print(list)
        print(contents)

        


            
Arrays.a(10,4)
Arrays.b(20,-7,8)
Arrays.c(20,-1,1)