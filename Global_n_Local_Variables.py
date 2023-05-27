
# a=10
#
# def value():
#     a=15
#     print('Local : ',a)
#
# value()
# print('Global : ',a)

#------------replacing the global variable value inside a function using the keyword 'global'------------------

a=10
def value():

    global a # using'global' keyword to change the global variable inside a function
    a=15
    print('local  : ',a)

def v():
    global a
    a=20
    print('local 2 : ',a)

def v1():
    global a
    a=25
    print('local 2 : ',a)


value()
v1()
v()
print('global : ',a)



#---------replacing the global variable value withour affecting the local variable using the keyword 'globals'------

# a=10
#
# def value():
#     a=5
#     x=globals()['a']
#     print('Local :',a)
#     # print('value x : ',x)
#     globals()['a']=15
# value()
# print('Global : ',a)

