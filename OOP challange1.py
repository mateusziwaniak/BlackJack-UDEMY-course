class Account:

    def __init__(self, name, ammount):
        self.owner = name
        self.ballance = ammount

    def deposit(self, x):
        self.ballance += x
        print("Deposit Accepted")

    def withdraw(self, x):
        if x > self.ballance:
            print("Founds Unavailable!")
        else:
            self.ballance -= x
            print("Withdrawal Accelted")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.ballance}"


acct1 = Account("Mateusz", 500)
print(acct1)
print(acct1.owner)
print(acct1.ballance)

acct1.deposit(20)

print(acct1.ballance)

acct1.withdraw(800)

print(acct1.ballance)
