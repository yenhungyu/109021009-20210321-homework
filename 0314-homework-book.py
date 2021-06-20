class Book:
    def __init__ (self,name,writer,translator,money,company):
        self.bookName=name
        self.bookWriter=writer
        self.bookTranslator=translator
        self.bookMoney=money
        self.bookCompany=company
    def showinfo(self):
        print(self.bookName)
        print(self.bookWriter)
        print(self.bookTranslator)
        print(self.bookMoney)
        print(self.bookCompany)

x1=Book("離散數學","Richard Johnsonbaugh","吳世弘","700","華泰文化")
x2=Book("6分鐘日記本","Dominik Spenst","吳宜蓁","224","方智")
x3=Book("此生，你我皆短暫燦爛","Ocean Vuong","何穎怡","284","時報出版")

x1.showinfo()
x2.showinfo()
x3.showinfo()
