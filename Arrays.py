# Arrays are similar to list, but need to have all the values of same type
# when creating an array at the start we have to mention the type code like ; int, float, double

from array import *

# val=array('i',[3,4,5,6,7,4])

# print(val.buffer_info())
# print(val.typecode)
# val.reverse()
# print(val[0])

# for i in range(len(val)):
#     print(val[i])

# different way to print the array one by one

# for i in val:
#     print(i)



#=======================================================

# val=array('u',['a','U','e'])
#
# for i in val:
#     print(i)

#======================================================


# val=array('i',[4,5,6,7,8,9])
#
# new=array(val.typecode,(a for a in val)) # creating a new array with the same type and values of old array
# # new1=array(val.typecode,(a*a for a in val)) # creating new array with the square value of the old array
#
# for i in new:
#     print(i)

#=========================================================

# also doing the same with while loop instead of for loop ( better is for loop )

# val=array('i',[4,5,6,7,8,9])
#
# i=0
# while i<len(val):
#     print(val[i])
#     i+=1

#======================================================

#-----------Array values from user--------------------

# ar=array('i',[])
#
# n=int(input('Enter the Length of the Array : '))
#
# for i in range(n):
#     x=int(input('Enter the values : '))
#     ar.append(x)
#
# print(ar)

# searching the index by getting input value array value from the user

# val=int(input('Enter the value for search : '))
#
# k=0
#
# for e in ar:
#     if e==val:
#         print(k)
#         break
#     k+=1

#===================================================

ar=array('i',[])

x=int(input('Enter the length of the array : '))

for i in range(x):
    z=int(input('Enter the values : '))
    ar.append(z)

print(ar)

m=int(input('Enter the search value : '))

v=0

for e in ar:
    if e==m:
        print(v)
        break
    v+=1

#--------------------------------------------------

# print(ar.index(m)) # getting index with the function

#===========================================================

# defautly array doesn't support multidimensional array so we are using Numpy



