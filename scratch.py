balance=4000
class account:
    def deposit(amount):
        global balance
        print("depositing:",amount)
        balance=balance+amount
        print("deposited")
        return
    def withdraw(amount):
        global balance
        print("trying to withdraw:",amount)
        print("available bal:",balance)
        if amount<=balance:
            print("collect cash")
            balance=balance-amount
        else:
            print("in sufficcient bal")
        return
class bank:
    def main():
        print("initial bal:",balance)
        amount=int(input("enter amount to deposite:"))
        account.deposit(amount1)
        print("balance:",balance)
        amount=int(input("enter withdraw"))
        account.withdraw(amount)
        print("final balance:",balance)
        return
bank.main()