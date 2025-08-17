import datetime
import json

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

transactions = []  # 거래 리스트
undo_stack = Stack()
   

def show_menu():
    print("=== 진성이의 가계부 ===")
    balance = calculate_balance()
    if balance >= 0:
        print(f"💰 현재 잔액: +{balance:,}원")
    else:
        print(f"💸 현재 잔액: {balance:,}원")
    print("-" * 25)
    print("1. 지출 추가")
    print("2. 수입 추가") 
    print("3. 거래 내역 보기")
    print("4. 월별 분석")
    print("5. 거래 관리")     
    print("6. 종료")
    print("7. 거래기록 초기화.")
    print("=" * 25)

def manage_transactions():
    print("=== 거래 관리 ===")
    print("1. 거래 수정")
    print("2. 거래 삭제") 
    print("3. 되돌리기") 
    print("4. 돌아가기")
    choice = input("입력: ")
    return choice

def add_expense():
   
    while True:
        try:
            amount = int(input("지출 금액: "))
            if amount > 0:
                break
            else:
                print("0보다 큰 금액을 입력하세요!")
        except ValueError:
            print("숫자만 입력하세요!")
    
    
    expense_categories = ["식비", "교통비", "생활비", "취미", "데이트", "저축", "필수품", "기타"]
    while True:
        try:
            print("카테고리 선택:")
            for i, cat in enumerate(expense_categories, 1):
                print(f"{i}. {cat}")
            cat_choice = int(input("선택: "))
            if 1 <= cat_choice <= len(expense_categories):
                category = expense_categories[cat_choice - 1]
                break
            else:
                print(f"1~{len(expense_categories)} 사이의 숫자를 입력하세요!")
        except ValueError:
            print("숫자만 입력하세요!")
     
    
  
    while True:
        try:
            date = input("날짜(YYYY-MM): ")
            datetime.datetime.strptime(date, "%Y-%m")
            break
        except ValueError:
            print("올바른 날짜 형식을 입력하세요! (예: 2024-03)")
    
   
    transaction = {
        "id": len(transactions) + 1,
        "type": "지출",
        "amount": amount,      
        "category": category,
        "date": date
    }
    save_stack()
    transactions.append(transaction)
    print(f"지출 {amount}원이 추가되었습니다!")
    save_data()
    return

def add_income():

    try:
        while True:
            try:
                amount = int(input("수입: "))
                if amount > 0:
                    break
                else:
                    print("0보다 큰 금액을 입력하세요!")
            except ValueError:
                print("숫자만 입력하세요!")
        while True:
            try:
                date = input("날짜(YYYY-MM): ")
                datetime.datetime.strptime(date, "%Y-%m")
                break
            except ValueError:
                print("올바른 날짜 형식을 입력하세요! (예: 2024-03)")
        transaction = {
            "id": len(transactions) + 1,
            "type": "수입",
            "amount": amount,      
            "date": date
        }
        save_stack()
        transactions.append(transaction)
        print(f"수입 {amount}원이 추가되었습니다!")
        save_data()
        return
    except ValueError:
        print("올바른 값을 입력해주세요.")
    
def show_transactions():
    if not transactions:
        print("거래 내역이 없습니다.")
        return
    
    print("ID  | 날짜     | 종류   |     금액     | 카테고리 ")
    print("-" * 60)
    
    for transaction in transactions:
        print(f"{transaction['id']:<3} | "          
              f"{transaction['date']:<8} | "         
              f"{transaction['type']:^4} | "         
              f"{transaction['amount']:>10,}원 | "    
              f"{transaction.get('category', ''):<8}")  
        
def calculate_balance():
    balance = 0
   
    for transaction in transactions:
        if transaction['type'] == "지출":
            balance -= transaction['amount']
        elif transaction['type'] == "수입":
            balance += transaction['amount']
    return balance

def modify_transaction():
    if not transactions:
        print("수정할 거래가 없습니다.")
        return
   
    show_transactions()

    while True: 
        try:   
            choice_ID = int(input("ID를 입력하세요:"))
            found = False

            for transaction in transactions:
                if transaction["id"] == choice_ID:
                    found = True
                    break

            if found:
                break
            else:
                print("존재하지 않는 ID입니다.")        
        except ValueError:
            print("올바른 숫자를 입력하세요.")

    while True:
        choice_modify = input("수정할 항목을 선택하세요 (date/type/amount/category): ")
        if choice_modify in ["date", "type", "amount", "category"]:
            break
        else:
            print("올바른 항목을 선택하세요!")
    save_stack()
    modify_value = input("수정할 내용을 입력하세요:")
    for transaction in transactions:
        if transaction["id"] == choice_ID:
            transaction[choice_modify] = modify_value
            print("수정 완료")
            save_data()
            return
             
def delete_transaction():
    if not transactions:
        print("삭제할 거래가 없습니다.")
        return
   
    show_transactions()

    while True: 
        try:   
            choice_ID = int(input("삭제할 거래의 ID를 입력하세요: "))
            found_transaction = None

            for transaction in transactions:
                if transaction["id"] == choice_ID:
                    found_transaction = transaction
                    break

            if found_transaction:
                break
            else:
                print("존재하지 않는 ID입니다.")        
        except ValueError:
            print("올바른 숫자를 입력하세요.")
    
    save_stack()
    transactions.remove(found_transaction)
    print(f"ID {choice_ID} 거래가 삭제되었습니다!")
    save_data()
    return

def save_data():

    try:
        with open('ledger.json', 'w', encoding='utf-8') as file:
            json.dump(transactions, file, ensure_ascii=False, indent=2)
        print("데이터가 저장되었습니다.")
    except Exception as e:
        print(f"저장실패: {e}")
    
def load_data():
    global transactions
    try:
        with open('ledger.json', 'r', encoding='utf-8') as file:
            transactions = json.load(file)
        print("데이터를 불러왔습니다.")
    except FileNotFoundError:
        print("📁 저장된 데이터가 없습니다. 새로 시작합니다.")
        transactions = []
    except json.JSONDecodeError:
        print("❌ 파일이 손상되었습니다.")
        transactions = []
        save_data()
    except Exception as e:
        print(f"로드실패: {e}")
        transactions = []

def get_monthly_data(year, month):
    result = []
    date = f"{year}-{month:02d}" 
    for transaction in transactions:
        if transaction['date'] == date and transaction['type'] == '지출':
            result.append(transaction)
    return result

def show_monthly_summary(year, month):
    filtered_data = get_monthly_data(year, month)
    if not filtered_data:  # 빈 데이터 체크 추가
        print(f"{year}-{month:02d}월에는 지출이 없습니다.")
        return
    
    category_sum = {}  

    for transaction in filtered_data:
        category = transaction['category']  
        amount = transaction['amount']    
        category_sum[category] = category_sum.get(category, 0) + amount

    print(f"\n📊 {year}-{month:02d}월 지출 분석")
    print("-" * 30)
    for category, total in category_sum.items():
        print(f"{category}: {total:,}원")
    print("-" * 30)
    print(f"총 지출: {sum(category_sum.values()):,}원")

def save_stack():
    """변경 전 상태를 스택에 저장"""

    undo_stack.push(transactions.copy())

def undo_transaction():
    # 목표: 잘못 입력한 거래 되돌리기
# 모든 거래 변경 시 스택에 상태 저장
# 체크: 실수로 입력한 거래를 되돌릴 수 있나?
 
    if undo_stack.is_empty():
        print("더 이상 실행 취소할 것이 없습니다!")
        return
    
    global transactions
    transactions = undo_stack.pop()    
    print("마지막 작업이 되돌려졌습니다.")
    save_data()
    show_transactions()



def main():
    global transactions
    while True:
        show_menu()
        choice = input("입력: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            add_income()
        elif choice == '3':
            show_transactions()
        elif choice == '4':
            year, month = map(int, input("ex 2024 03 띄어쓰기로 구분 연도와 월을 입력하세요: ").split())
            show_monthly_summary(year, month)
        elif choice == '5':
            choice2 = manage_transactions()
            if choice2 == '1':
                modify_transaction()
            elif choice2 == '2':
                delete_transaction()
            elif choice2 == '3':
                undo_transaction()
            elif choice2 == '4':
                pass
        elif choice == '6':          
            return
        elif choice == '7':
            while True:
                choice_2 = input("정말 초기화 하겠습니까?  (y/n):")
                if choice_2 == 'y':
                    save_stack()
                    transactions = []
                    save_data()
                    print("✅ 모든 거래 기록이 초기화되었습니다! 실수로 삭제하였다면 거래관리-> 되돌리기를 이용해주세요.")
                    break
                elif choice_2 == 'n':
                    print("초기화를 취소했습니다.")
                    pass
                else:
                    print("y 또는 n을 입력하세요.")

    
    

if __name__ == "__main__":
    load_data()
    main()
    save_data()
    print("종료되었습니다.")