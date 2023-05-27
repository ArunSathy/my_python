# # types of inheritance
# 1. single inheritance
# 2. multilevel inheritance
# 3. Multiple inheritance
# 4. Hierarchical inheritance
#----------------------------------------------------------------

#-----------single inheritance---------------

# class student:
#     def __init__(self,name):
#         self.name=name
#     def data(self):
#         self.name=input('enter your name : ')
# class details(student):
#     def __init__(self,mark):
#         self.mark=mark
#     def get(self):
#         self.mark=int(input("enter your mark : "))
#         print('Name : ',self.name)
#         print('Mark : ',self.mark)
#
# obj=details('')
# obj.data()
# obj.get()

#------------------------------------------------------------------

#-----------------multilevel inheritance-------------

# class A:
#     def __init__(self,name):
#         self.name=name
#     def data(self):
#         self.name=input('enter your name : ')
# class B(A):
#     def __init__(self,mark):
#         self.mark=mark
#     def get(self):
#         self.mark=int(input("enter your mark : "))
#         print('Name : ', self.name)
#         print('Mark : ', self.mark)
# class C(B):
#     def hoo(self):
#         print('Hiii.... Habibiessss')
#
# obj=C('')
# obj.data()
# obj.get()
# obj.hoo()

#---------------------another example for multilevel inheritance----------------------------------

# class A:
#     def __init__(self,name):
#         self.name=name
#     def data(self):
#         self.name=input('enter your name : ')
# class B(A):
#     def __init__(self,mark):
#         self.mark=mark
#     def get(self):
#         self.mark=int(input("enter your mark : "))
#
# class C(B):
#     def __init__(self,hod):
#         self.hod=hod
#     def put(self):
#         self.hod=input('enter hod name : ')
#         print('Name : ', self.name)
#         print('Mark : ', self.mark)
#         print('HOD : ',self.hod)
#
# obj=C('')
# obj.data()
# obj.get()
# obj.put()

#-------------------------------------------------------

#----------multiple inheritance--------------------

# class A:
#     def __init__(self,name):
#         self.name=name
#     def first(self):
#         self.name=input('enter A : ')
# class B:
#     def __init__(self,age):
#         self.age=age
#     def second(self):
#         self.age=int(input('enter B : '))
# class C(A,B):
#     def third(self):
#         print('\nStudent details')
#         print('Name : ',self.name)
#         print('Age  : ',self.age)
# og=C('')
# og.first()
# og.second()
# og.third()

#-----another example for multiple inheritance-----

# class A:
#     def first(self):
#         print('Class A')
# class B:
#     def second(self):
#         print('Class B')
# class C(A,B):
#     def third(self):
#         print("Class C has A & B")
#
# ob=C()
# ob.first()
# ob.second()
# ob.third()

#=========================================================================

# class A:
#     def d1(self):
#         print(1,2,3,4,end=' ')
# class B:
#     def d2(self):
#         print(5,6,7,8,end=' ')
# class C(A,B):
#     def d3(self):
#         print(9,10)
#
#
# a=C()
# a.d1()
# a.d2()
# a.d3()

#--------------------------------------------

#------constructor in inheritance----------

class A:
    def __init__(self):
        print("A init")
    def d1(self):
        print('A1')
    def d2(self):
        print('A2')
class B:

    def __init__(self):
        # super().__init__()
        print('B init')
        # super().__init__()
    def d3(self):
        print('B1')
    def d4(self):
        print('B2')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('C init')
    def d5(self):
        print('C1')
    def d6(self):
        print('C2')

a=C()
