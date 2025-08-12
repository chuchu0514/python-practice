import datetime

transactions = []  # 거래 리스트



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
    print("3. 삭제된 거래 복구")  # ← 여기서 스택 활용!
    print("4. 돌아가기")
    choice = input("입력: ")
    return choice

def add_expense():
    # 금액 입력 (반복)
    while True:
        try:
            amount = int(input("지출 금액: "))
            if amount > 0:
                break
            else:
                print("❌ 0보다 큰 금액을 입력하세요!")
        except ValueError:
            print("❌ 숫자만 입력하세요!")
    
    # 카테고리 선택 (반복)
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
                print(f"❌ 1~{len(expense_categories)} 사이의 숫자를 입력하세요!")
        except ValueError:
            print("❌ 숫자만 입력하세요!")
    
    memo = input("메모: ")  
    
    # 날짜 입력 (반복)
    while True:
        try:
            date = input("날짜(YYYY-MM): ")
            datetime.datetime.strptime(date, "%Y-%m")
            break
        except ValueError:
            print("❌ 올바른 날짜 형식을 입력하세요! (예: 2024-03)")
    
    # 거래 저장
    transaction = {
        "id": len(transactions) + 1,
        "type": "지출",
        "amount": amount,      
        "category": category,
        "memo": memo,
        "date": date
    }
    transactions.append(transaction)
    print(f"✅ 지출 {amount}원이 추가되었습니다!")

def add_income():
    # 수입 추가
    # 목표: 수입 입력받기
# add_expense()와 비슷하지만 수입 카테고리 사용
# 체크: 수입이 제대로 입력되는가?
    try:
        while True:
            try:
                amount = int(input("수입: "))
                if amount > 0:
                    break
                else:
                    print("❌ 0보다 큰 금액을 입력하세요!")
            except ValueError:
                print("❌ 숫자만 입력하세요!")
        while True:
            try:
                date = input("날짜(YYYY-MM): ")
                datetime.datetime.strptime(date, "%Y-%m")
                break
            except ValueError:
                print("❌ 올바른 날짜 형식을 입력하세요! (예: 2024-03)")
        transaction = {
            "id": len(transactions) + 1,
            "type": "수입",
            "amount": amount,      
            "date": date
        }
        transactions.append(transaction)
        print(f"✅ 수입 {amount}원이 추가되었습니다!")
    except ValueError:
        print("올바른 값을 입력해주세요.")

def show_transactions():
    if not transactions:
        print("거래 내역이 없습니다.")
        return
    
    print("ID  | 날짜     | 종류   |     금액     | 카테고리   | 메모")
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
    # 잔액 계산
    # 목표: 현재 잔액 계산
# 모든 수입 - 모든 지출
# 체크: 잔액이 정확히 계산되는가?
    for transaction in transactions:
        if transaction['type'] == "지출":
            balance -= transaction['amount']
        elif transaction['type'] == "수입":
            balance += transaction['amount']
    return balance
# 수입/지출 입력 → 내역 보기 → 잔액 확인
# 기본 가계부가 동작하는지 확인

def modify_transaction():
# 거래 수정 실제 기능
    pass

def delete_transaction():
# 거래 삭제 실제 기능
    pass

def save_data():
    # JSON 파일로 저장
    # 목표: JSON 파일로 저장
# transactions 리스트를 파일에 저장
# 체크: 파일이 생성되고 데이터가 저장되는가?
    pass

def load_data():
    # JSON 파일에서 불러오기
    # 목표: JSON 파일에서 불러오기
# 파일이 없으면 에러 처리
# 체크: 저장한 데이터가 제대로 불러와지는가?
    pass

# 거래 입력 → 저장 → 프로그램 종료 → 재시작 → 불러오기
# 데이터가 유지되는지 확인

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

# 기존에 만든 Stack 클래스 사용
# undo_stack, redo_stack 생성

def undo_transaction():
    # 목표: 잘못 입력한 거래 되돌리기
# 모든 거래 변경 시 스택에 상태 저장
# 체크: 실수로 입력한 거래를 되돌릴 수 있나?
    pass

def redo_transaction():
    # 목표: 되돌린 거래 다시 적용
# 체크: 되돌린 거래를 다시 되돌릴 수 있나?
    pass

def compare_months():
    # 목표: 두 달 비교하기
# "3월 vs 2월 식비 비교"
# 체크: 증감률까지 계산되는가?
    pass

# 모든 기능 종합 테스트
# 에러 처리 추가
# 사용자 경험 개선

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
                pass
            elif choice2 == '2':
                pass
            elif choice2 == '3':
                pass
            elif choice2 == '4':
                pass

        elif choice == '6':
            return
    
    

if __name__ == "__main__":
    main()
    print("종료되었습니다.")