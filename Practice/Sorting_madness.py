#write a function, using the selection sort algorithm, which'll sort each student, in the 
# list by the key-value kof the dictionary, they are in, all of them are located in the first
# tuple, CN students are stored in th next tuple

# list = [ ( {2: obj()} , {3: obj()}, {4: obj()}) , {2: obj()} , {3: obj()}, {4: obj()}) ]

class obj:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        print ("My name is", self.name)

s1  = obj("mubariz",21)
s2 = obj("saad", 22)
s3 = obj("mubasher", 23)

dict1 = {1: s1}
dict2 = {2 : s2}
dict3 = {3 : s3}


datastructures = [dict1,dict2,dict3]
print(datastructures[0] )
# for k in datastructures:
#     print (k.items())

l = [s1, s2, s3]
l.sort(key = lambda x: x.age)
# for i in l:
#     print (i.age)
# print(l)
# ls[]
    # for j,v in k:
    #     print(j, "---", v)





