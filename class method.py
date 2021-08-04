class Bank:
    bank_name='SBI'
    ifsc = 'sbin000'
    bank_branch = 'bangalore'

    def __init__(self,cname,cage,cphno,cemail):
        self.cname=cname
        self.cage=cage
        self.cphno=cphno
        self.email=cemail

    @classmethod
    def getmethod(cls):
        print(cls.bank_name)
        print(cls.ifsc)
        print(cls.bank_branch)


    @classmethod
    def setmethod(cls):
        modify=input("enter the data to be modified")
        if modify=='bankname':
            cls.bank_name=input("enter the bank name")

            Bank.getmethod()
        elif modify=='ifsc':
            cls.ifsc=input("enter ifsc code")
            Bank.getmethod()
        elif modify=='bankbranch':
            cls.bank_branch=input("enter the bank branch")

            Bank.getmethod()
        else:
            print("no data to be modified")


c1 = Bank("Balayya","29","898985645","balu@gmail.com")
c1.getmethod()
c1.setmethod()

