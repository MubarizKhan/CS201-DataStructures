d = [
    {'name':'Mubariz',  'age' : 21},
    {'name' : 'saad', 'age': 7},
    {'name':'Mubasher','age' : 34}
    ]

def student_age(a):
    return a['age']

d.sort(key = student_age)
print (d)

# (d.sort(key = lambda x: x.age)


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (self.name + "--" + str(self.age))

tuples = [('Mubariz', 21), ('Saad', 32), ('Lolola', 4)]
s1 = student('Mubariz', 21)
s2 = student('Saad', 32)
s3 =  student('Lolola', 4)
list = [s1, s2, s3]

list.sort(key = lambda x: x.age)

# print(list)

# for i in tuples:
#     s = student(i[0], i[1])
#     print (i[0], i[1])
#     list.append(s)

for i in list:
    print(i)

class employee:
    def __init__(self, name, tenure):
        self.name = name
        self.tenure = tenure

    # def __str__(self):
    #     val = self.name + "---" + self.tenure
    #     return val

# def tenure_func(a):
#     return a['tenure']

e1 = employee('Mubariz', {'tenure': 21} )
e2 = employee( 'Saad', {'tenure': 11} )
e3 = employee( 'Ali', {'tenure': 1 } )

emp = [e1, e2, e3]

emp.sort(key = lambda x: x.tenure['tenure'])

for i in emp:
    print (i.tenure)
            
        


