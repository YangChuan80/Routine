import sys
class GeneralExce(Exception):
    pass
class Exce1(GeneralExce):
    pass
class Exce2(GeneralExce):
    pass

def raise1():
    raise Exce1()

def raise2():
    raise Exce2()

def raise0():
    raise GeneralExce()

for func in [raise0,raise1,raise2]:
    try:
        func()
    except GeneralExce:
        print(sys.exc_info())
