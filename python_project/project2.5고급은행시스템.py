# 기본 은행 계좌 클래스
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f"{owner}님의 계좌가 개설되었습니다. 잔액: {balance}원")
    
    def deposit(self, amount):
        self.balance += amount
        return f"{amount}원 입금완료. 잔액: {self.balance}원"
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"{amount}원 출금완료. 잔액: {self.balance}원"
        else:
            return "잔액이 부족합니다."
    
    def get_info(self):
        return f"계좌주: {self.owner}, 잔액: {self.balance}원"

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance = self.balance * self.interest_rate
        return f"이자로 인해 잔액이 {self.balance}원이 되었습니다."
    

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, fee):
        super().__init__(owner, balance)
        self.fee = fee

    def withdraw(self, amount):
        if self.balance >= amount + self.fee:
            self.balance -= amount + self.fee
            return f"{amount}원 출금완료, 수수료가 {self.fee}원 차감되었습니다. 잔액: {self.balance}원"
        else:
            return "잔액이 부족합니다."
    # 또는 이런 방법이 있음
    # def withdraw(self, amount):
    #     # 부모의 withdraw를 먼저 실행하고, 수수료만 추가로 차감
    #     result = super().withdraw(amount)  # 부모 메소드 실행
    #     if "출금완료" in result:  # 출금이 성공했다면
    #         self.balance -= self.fee  # 수수료 추가 차감
    #     return result 
        


# 테스트 코드
if __name__ == "__main__":
    # 기본 계좌
    basic = BankAccount("김철수", 10000)
    print(basic.deposit(5000))
    print(basic.withdraw(3000))
    savings = SavingsAccount("추추진성", 15000, 1.05)
    print(savings.deposit(5000))
    print(savings.add_interest())
    checking = CheckingAccount("추추추진성", 20000, 500)
    print(checking.deposit(4000))
    print(checking.withdraw(5000))

accounts = [basic, savings, checking]

for account in accounts:
         print(account.get_info()) 