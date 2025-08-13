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
    print("1. 수입 추가")
    print("2. 지출 추가") 
    print("3. 거래 내역 보기")
    print("4. 월별 분석")
    print("5. 거래 관리")     
    print("6. 종료")
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
    
    memo = input("메모: ")  
    
  
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
        "memo": memo,
        "date": date
    }
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
    
    print("ID  | 날짜     | 종류   |     금액     | 카테고리 , 메모")
    print("-" * 60)
    
    for transaction in transactions:
        print(f"{transaction['id']:<3} | "          
              f"{transaction['date']:<8} | "         
              f"{transaction['type']:^4} | "         
              f"{transaction['amount']:>10,}원 | "    
              f"{transaction.get('category', ''):<8} , "  
              f"{transaction.get('memo', '')}")      
        
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
        choice_modify = input("수정할 항목을 선택하세요 (date/type/amount/category/memo): ")
        if choice_modify in ["date", "type", "amount", "category", "memo"]:
            break
        else:
            print("올바른 항목을 선택하세요!")

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
    
    
    transactions.remove(found_transaction)
    print(f"ID {choice_ID} 거래가 삭제되었습니다!")
    save_data()
    return

def save_data():

    try:
        with open('file_storage/ledger.json', 'w', encoding='utf-8') as file:
            json.dump(transactions, file, ensure_ascii=False, indent=2)
        print("데이터가 저장되었습니다.")
    except Exception as e:
        print(f"저장실패: {e}")
    
def load_data():
    global transactions
    try:
        with open('file_storage/ledger.json', 'r', encoding='utf-8') as file:
            transactions = json.load(file)
        print("데이터를 불러왔습니다.")
    except FileNotFoundError:
        print("📁 저장된 데이터가 없습니다. 새로 시작합니다.")
        transactions = []
    except json.JSONDecodeError:
        print("❌ 파일이 손상되었습니다.")
        transactions = []
    except Exception as e:
        print(f"로드실패: {e}")
        transactions = []

def get_monthly_data(year, month):
    # 목표: 특정 월의 거래만 필터링
# 헬퍼 함수 (다른 함수들이 사용할 예정)
# 체크: 3월 데이터만 정확히 가져오는가?
    pass

def show_monthly_summary():
    # 목표: 특정 월 요약 보기 (핵심 기능!)
# 년/월 입력받기 → 해당 월 수입/지출/카테고리별 집계
# 체크: "3월에 식비 얼마 썼나?" 답할 수 있는가?
    pass

def show_category_analysis():
    # 목표: 카테고리별 월 분석
# 특정 카테고리의 월별 지출 추이
# 체크: "식비가 점점 늘고 있나?" 알 수 있는가?
    pass

def undo_transaction(transactions):
    # 목표: 잘못 입력한 거래 되돌리기
# 모든 거래 변경 시 스택에 상태 저장
# 체크: 실수로 입력한 거래를 되돌릴 수 있나?
 
    if undo_stack.is_empty():
        print("더 이상 실행 취소할 것이 없습니다!")
        return
    
    pass



def main():
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
            pass
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
            save_data()
            return
    
    

if __name__ == "__main__":
    load_data()
    main()
    print("종료되었습니다.")