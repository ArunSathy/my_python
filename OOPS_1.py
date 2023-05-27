# object oriented programming

class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

    def data(self):
        self.name=input('Enter your Name : ')
        self.mark=int(input('Enter your Mark : '))
        print('Name : ',self.name)
        print('Mark : ',self.mark)

object=student('','') # object creation(can give any object name)
object.data()



