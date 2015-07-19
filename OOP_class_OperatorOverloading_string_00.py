class FifthExample:
    def __init__(self,value='what a wonderful world!'):
        self.content=value

    def __repr__(self):
        return 'This is %s'%self.content

R=FifthExample(100)
