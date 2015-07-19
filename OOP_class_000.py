#class statement

class gwncc:
    def getname(self, name):
        self.name=name

    def gethospital(self, hospital):
        self.hospital=hospital

    def gettitle(self, title):
        self.title=title

    def showinformation(self):
        print('Name: ', self.name)
        print('Title: ', self.title)
        print('Hospital: ', self.hospital)
        print('Nationality: ', self.nationality, '\n')
        

class gwncc_staff(gwncc):
    def getfield(self, field):
        self.field=field

    def getdepartment(self, department):
        self.department=department

    def showinformation(self):
        print('Name: ', self.name)
        print('Title: ', self.title)
        print('Hospital: ', self.hospital)
        print('Nationality: ', self.nationality)
        print('Staff Field: ', self.field)
        print('Staff Department: ', self.department)
        print('Staff Profession: ', self.profession, '\n')

#Add attribute outside the class statement
gwncc.nationality='China'

#Generate Instances
sunyingxian=gwncc()
wangfangzheng=gwncc()
pangwenyue=gwncc()
yangchuan=gwncc_staff()

#Instances implement methods
sunyingxian.getname('Sun Yingxian')
sunyingxian.gettitle('Professor')
sunyingxian.gethospital('First Affiliated Hospital of China Medical University')

#Instances implement methods:
yangchuan.getfield('Registration')
yangchuan.getdepartment('Cardiology 3')

yangchuan.getname('Yang Chuan')
yangchuan.gettitle('Attending Doctor')
yangchuan.title='Visiting Scientist'
yangchuan.gethospital('Shengjing Hospital of China Medical University')

yangchuan.profession='Bioinformation'

#Add a attribute outside the class
sunyingxian.age=52

#Output the information
sunyingxian.showinformation()
yangchuan.showinformation()

