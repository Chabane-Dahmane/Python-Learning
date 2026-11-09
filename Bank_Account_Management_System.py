class BankAccount :
    bank_name = "Algerian bank"
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
         if amount>0 :
             self.__balance += amount
             print("Deposit successful")
         else :
             print("Invalid amount")

    def withdraw(self,amount):
        if amount>0 & amount<= self.__balance :
            self.__balance -= amount
            print("Withdrawal successful")
        else :
            print("Invalid withdrawal")   

    def transfer(self,amount,target):
        if amount>0 & amount <= self.__balance :
            self.__balance -= amount
            target.__balance += amount
            print("Transfer successful")
        else :
              print("Transfer failed")

    def show_info(self):
        print("Owner:", self.owner)
        print("Balance:", self.__balance)
        print("Bank:", BankAccount.bank_name)

account1 = BankAccount("Ali",20000)
account2 = BankAccount("Ahmed",40000)

account1.deposit(10000)
account1.withdraw(5000)
account1.transfer(10000, account2)


print("\nAccount 1:")
account1.show_info()

print("\nAccount 2:")
account2.show_info()