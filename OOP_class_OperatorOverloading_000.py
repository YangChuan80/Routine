class FirstExample:
    def __init__(self,value):
        self.data=value
        
    def __add__(self, other):
        self.data=self.data+other

X=FirstExample(100)

X+100

print('X=',X.data)

#////////////////////////////////////////////

class SecondExample:
    def __init__(self, value=2):
        self.data=value

    def __mul__(self, times):
        self.data=self.data*times

A=SecondExample()
A*2

print('A=',A.data)
#///////////////////////////////////////////////

class ThirdExample:
    def __init__(self, value=3):
        self.data=value

    def __getitem__(self, indexing):
        self.data=self.data**indexing

M=ThirdExample()
M[2]

print('M=', M.data)
#///////////////////////////////////////////////////

class FourthExample:
    def __getattr__(self, attrname):
        if attrname=='age':
            return 100
        else:
            print('No such attribute.')

N=FourthExample()
print('N.age=',N.age)
