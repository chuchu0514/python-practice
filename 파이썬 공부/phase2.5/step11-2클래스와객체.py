class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"내 계좌엔 {self.balance}만큼 들어있어요")
    def deposit(self, amount):
        
        self.balance += amount
        print(f"{amount}원을 입금했습니다.")

    def withdraw(self, amount):
        
        if self.balance >= amount:
             self.balance -= amount
             print(f"{amount}원을 출금했습니다.")
        else:
            print("잔액이 부족합니다.")

    def get_balance(self):
        return self.balance

my_account = BankAccount("김철수", 10000)
my_account.deposit(5000)
my_account.withdraw(3000)    
my_account.withdraw(20000)
print(my_account.get_balance())