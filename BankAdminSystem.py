"""
 ******************************************************************************
 * CLASSES TO SETUP BANK ACCOUNT SYSTEM AND ACTUAL BANK USER INTERFACE SYSTEM *
 ******************************************************************************
"""

class NewBankAccountSetup():
    accountnumber= 0
    numberOfUsers = 0
    

    def __init__(self, owner, initial_deposit):
        maxUsers = 3

        if NewBankAccountSetup.numberOfUsers >= maxUsers:
            print("This bank has reached its maximum amount of users.")
        else:
            NewBankAccountSetup.new_usr()
            self.owner = owner
            NewBankAccountSetup.accountnumber += 1
            self.initial_deposit = initial_deposit

    


    @classmethod
    def new_usr(cls):
        cls.numberOfUsers += 1


class BankSystem(NewBankAccountSetup):
    
    def ShowUserInfo(self):
        self.ShowUserInfo = str("Account Owner Name:" + self.owner + "\n" + self + "'s Account number:" + self.accountnumber + "\n" + self + "'s Initial Deposit:" + self.initial_deposit)


"""
/***********************
 * TESTING THE CLASSES *
 ***********************/
"""



JaredsAcc = NewBankAccountSetup("Jared", 500)
JaredInBank = BankSystem("Jared", 500)

print(JaredInBank.ShowUserInfo)
#print(JaredsAcc.accountnumber)
#print(JaredsAcc.owner)
#print(JaredsAcc.initial_deposit)
#print(BankSystem.numberOfUsers)


"""
MauriesAcc = NewBankAccountSetup("Maurie", 200)
print(MauriesAcc.accountnumber)
print(MauriesAcc.owner)
print(MauriesAcc.initial_deposit)
print(NewBankAccountSetup.numberOfUsers)

BerrysAcc = NewBankAccountSetup("Berry", 9000)
print(BerrysAcc.accountnumber)
print(BerrysAcc.owner)
print(BerrysAcc.initial_deposit)
print(NewBankAccountSetup.numberOfUsers)

SallysAcc = NewBankAccountSetup("Sally", 5)
print(SallysAcc.accountnumber)
print(SallysAcc.owner)
print(SallysAcc.initial_deposit)
print(NewBankAccountSetup.numberOfUsers)

person5 = NewBankAccountSetup("person", 5)
print(person5.accountnumber)
print(person5.owner)
print(person5.initial_deposit)
print(NewBankAccountSetup.numberOfUsers)
"""