class school:
    def __init__(self):
        self.name='arun'
        self.age=24

    def compare(self,c2):
        if self.age == c2.age:
            return True
        else:
            return False




c=school()
c1=school()
c1.name='athira'
c1.age=24

if c.compare(c1):
    print("They are same")
else:
    print("they are different")
print(c.name)
print(c.age)
print(c1.name)
print(c1.age)

#------------------------------------------------

