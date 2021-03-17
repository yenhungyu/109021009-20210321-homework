class Student:
    def __init__ (self,name,number,gender,height,weight):
        self.studentName=name
        self.studentNumber=number
        self.studentGender=gender
        self.studentHeight=height
        self.studentWeight=weight
    def showinfo(self):
        print(self.studentName)
        print(self.studentNumber)
        print(self.studentGender)
        print(self.studentHeight)
        print(self.studentWeight)

x1=Student("林小白","109021000","女","168","55")
x2=Student("陳小黑","109021777","男","180","72")
x3=Student("張小胖","109021666","女","159","50")

x1.showinfo()
x2.showinfo()
x3.showinfo()