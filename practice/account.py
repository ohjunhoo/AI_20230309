class BankAcoount:
    def __init__(self,acc_num, depo, name):
        self.acc_num = acc_num
        self.depo = depo
        self.name = name 
    def deposit(self,depo):
        self.depo=depo
        return self.depo
        
    def withdraw(self,withd):
        self.depo = withd
        return self.depo


account1 = BankAcoount("1234567890", 5000, "JOIN DOE")

print(f"{account1.deposit(1000)} deposited to {account1.acc_num}")
print(f"{account1.withdraw(2000)} withdrawn from {account1.acc_num}")