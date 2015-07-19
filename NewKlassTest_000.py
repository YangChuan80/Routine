class KlassTest:
        x=0
        __slots__=['Name','Hospital','Title','Age']
                
        __m=40
                
        def default_hospital(this):
                this.Hospital='Shengjing Hospital of China Medical University'
                        
        def combine_name(self):
                return self.Name+' '+Title
                        
        @staticmethod
        def printall():
                print('What a wonderful day!')

m=KlassTest()
m.Name='Sun Yingxian'
m.Age=52
m.Title='Professor'

class SubKlass1(KlassTest):
        x=1

class SubKlass2(KlassTest):
        x=2

class BottomKlass(SubKlass1,SubKlass2):
        pass

n=BottomKlass()
print('n=',n.x)
