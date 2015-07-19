class GeneralException(Exception):
    def displayit(self, a,b,c):
        print('a+b+c=',a+b+c)

class Exception1(GeneralException):
    pass

class Exception2(GeneralException):
    pass

try:
    X=Exception1()
    raise X
except GeneralException:
    M=Exception1()
    print(M.displayit(2,2,2))
