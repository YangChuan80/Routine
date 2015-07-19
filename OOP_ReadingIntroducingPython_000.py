class Bill:
    def __init__(self, description):
        self.description=description

class Duck:
    def __init__(self, billname):
        self.bill=billname

    def about(self):
        print(self.bill.description)

bills=Bill('wide orange')

duck=Duck(bills)


        
