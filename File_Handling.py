#---------------write---------------------------

#file=open("first.txt","w")
#file.close()

# file=open('my.txt','w')
# file.write("Hi Mr.Arun")
# file.close()

#-----------------read--------------------------------

# file=open("arun.txt","r")
# x=file.read()
# print(x)
# file.close()

#-----------------append------------------------------

# file=open('my.txt','a')
# file.write('\nyou have to learn python')
# file.close()

#---------------------------------------------------

# file=open('charu.txt','w+')
# file.write("My charutty I LOVE U")
# l=file.read()
# print(l)
# file.close()

# file=open('mar.txt','w+')
# file.write("my dear chakkare")
# m=file.read()
# print(m)
# file.close()

# file=open('star.txt','w')
# for i in range(5):
#     for j in range(i):
#         file.write("*  ")
#     file.write("\n")
# file.close()


# file=open('star.txt','r')
# x=file.read()
# print(x)
# file.close()


# file=open('my.txt','r')
# print(file.readline(),end="")
# print(file.readline())

#----------copying from a file and pasting to aother file------------------

# f=open('my.txt','r')
# f1=open('star.txt','w')
# for data in f:
#     f1.write(data)

#--------------------------------------------------------------------

#file write and read

# file=open('m','w')
# file.write("my men are here....")
# file=open('m','r')
# x=file.read()
# print(x)
# file.close()

#-------------------read a pic and write a pic-------------------

# file=open('joker.jpg','rb')
# file1=open('mypic.jpg','wb')
# for i in file:
#     file1.write(i)

#---------------------------------------------------------------------


# x=open('charu.txt','r')
# y=open('first.txt','w')
# for i in x:
#     y.write(i)
z=open('charu.txt','a')
z.write("\nMore than anything")
z.close()