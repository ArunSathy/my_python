# import sys
#
# sys.setrecursionlimit(2000) # setting the recursion limit
# print("Recursion limit is : ",sys.getrecursionlimit())     # getting the recusrion limit
#
# def a():
#     print('Arun')
#     a()
# a()

#-----------------------------

# def greet():
#     print('Hello')
#     greet()
# greet()

#========================================================

#-------------------factorial using recursion--------------------------------------

# n=int(input('number : '))
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
#
# op=fact(n)
# print(op)