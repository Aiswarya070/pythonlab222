class bankaccount:
    def __init__(self):
        self.balance=0
        print("account number=00909111567")
        print("Name:Aiswarya")
        print("type of account=zero balance")
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance=self.balance+amount
        print("Amount Deposited: ",amount)
    def withdraw(self):
        amount=float(input("Enter the amount to be withdraw:"))
        if self.balance>=amount:
            self.balance-=amount
            print("Amount Deposited: ",amount)
        else:
                print("\ninsufficient balance")
    def display(self):
        print("your available balance is:",self.balance)
s=bankaccount()
while(True):
    print("\n1.Deposit money\n2.Withdraw money\n3.exit")
    ch=int(input("enter the choice:"))
    if(ch==1):
        s.deposit()
        s.display()
    elif(ch==2):
        s.withdraw()
        s.display()
    else:
        exit(0)
s.display()        
        
    

        
        
        
