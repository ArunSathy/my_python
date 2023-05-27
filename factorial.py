# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
#
# x=5
# result=fact(x)
# print(result)

#================================

#--------using for loop-----------

n=int(input('Enter a number : '))

def fact(n):
    z=1
    if n==0 or n==1:
        return z
    for i in range(1,n+1):
        z=z*i
    return z

op=fact(n)
print("Factorial of",n,"is : ",op)

#--------using math module-----------

# import math
# n=int(input('Enter a number : '))
# op=math.factorial(n)
# print("Factorial of",n,"is : ",op)

#=================================================================

