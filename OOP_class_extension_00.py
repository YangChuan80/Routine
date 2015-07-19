class MainKlass:
    def showcurrent(self):
        print('This is Main.')

class SubKlass(MainKlass):
    def __init__(self, data):
        self.data=data
        
    def showcurrent(self):
        print('This is Sub.')
        MainKlass.showcurrent(self)

    def showvalue(self):
        print(self.data)

X=SubKlass('hello')
X.showcurrent()

def showmultiplied(self,times=3):
    self.data=self.data*times

print(X.data)

MainKlass.multiplied=showmultiplied

X.multiplied(10)
X.showvalue()
    
