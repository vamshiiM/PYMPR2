#defining a function
# def func():
#     print("hello world")
#
# func()

# def func1(fname,lname,name):
#     print(name + fname + lname + " hiii")
#
# func1(" vamshi "," marri "," vam ")
#
# def func2(*kids):
#     print("HERE ARE MY KIDS " + kids[0] + kids[1] + kids[2])
#
# func2("ASH"," asb "," bsd "," fbghdfb ")

# def mul(x):
#     i = 1
#     for i in range(11):
#         print(i * x)
#
# mul(6)
#
# #creating a class in pythin and its object
# class first: # syntax to create the class
#     x = 10 # this are the properties of the class
#
# obj = first() # calling the properties using obj of the class.
# print(obj.x) # printing the result

# USING THE INIT FUNCTION WHICH IS BUILT IN

class person:
    def __init__(self,name,age):# init function are the built in functions which are initalized when the class is initialized

        self.name=name
        self.age=age


print(person("shinchan",30))#this will give the address of the properties
print(person("hiroshi",45))#same here

p1 = person("shinchan",30)
print(p1.name)
print(p1.age)


