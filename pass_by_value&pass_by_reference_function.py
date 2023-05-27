# def update(x):
#     x=8
#     print('x',x)
#
# a=10
# update(a)
# print("a",a)

#=================================

# def update(x):
#     print('x1',id(x))
#     x=8
#     print('x2',id(x))
#     print('x',x)
#
# a=10
# print('a1',id(a))
# update(a)
# print('a2',id(a))
# print("a",a)
#=================================

# def value(x):
#     x=6
#     print('x ',x)
#     return x
#
# x=10
# value(x)
# print('x ',x)

#====================================

# def value(mylist):
#     print(id(mylist))
#     print("my list 1 : ",mylist)
#     mylist[2]=50
#     print("my list 2 : ",mylist)
#     return
#
# mylist=[10,20,30]
# print(id(mylist))
# value(mylist)
# print('my list 3 : ', mylist)
#
# print('----------------------------------------------')
#
# def update(list):
#     list=[1,2,3,4]
#     print(id(list))
#     print('my list 1 :',list)
#     return
# list=[10,20,30]
# print(id(list))
# update(list)
# print('my list 2 :',list)

#------types of arguments in python-------

# 1. keyword-----------------------------

# def person(name,age):
#     print('Name : ',name)
#     print('Age  : ',age)
# person(age=25,name='arun') # without knowing the order we can use keywords to mention the value correctly

# 2. default------------------------------

# def person(name,age=25): # we can defaulty value for the variable here; if it's not there while calling, it will take from here
#     print('Name : ',name)
#     print('Age  : ',age)
# person('arun') # if we gave the value, it will override the default value

# 3. variable length----------------------

# def sum(*b): # use * to convert it into tuple and all the other value will be stored in 'b' as a tuple
#     c=0
#     for i in b:
#         c=c+i
#     print(c)
#
# sum(5,6,7,8)


#--------Keyworded Variable Length Arguments-------------------------------

def person(name,**d): # ** means passing multiple arguments with keyword while calling
    print('name  : ',name)
    # print(d)
    for i,j in d.items():
        print(i,' : ',j)

person('arun',age=28,dist='kerala',mob=9895)
