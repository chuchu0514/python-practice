# 🎯 선형탐색 실습 문제

print("=== 📚 선형탐색 실습 문제 ===")
print("예제에서 본 선형탐색을 직접 구현해보세요!")
print("힌트: for 반복문으로 처음부터 끝까지 하나씩 확인!")

print("\n" + "="*50)

# 문제 1: 기본 선형탐색
print("📝 문제 1: 숫자 찾기")
print("리스트에서 특정 숫자의 인덱스를 찾는 함수를 만드세요")

def find_number(numbers, target):
    """
    숫자 리스트에서 target 값의 인덱스를 찾는 함수
    
    Args:
        numbers: 숫자 리스트
        target: 찾을 숫자
    
    Returns:
        int: 찾은 인덱스, 없으면 -1
    """
    for i, num in enumerate(numbers):  
        if num == target:
            return i
    return -1
    # TODO: 여기서 선형탐색으로 target을 찾아서 인덱스 반환하세요
    # 힌트: for i in range(len(numbers)): 사용

# 테스트
test_numbers = [10, 25, 33, 47, 52, 68, 71]
print(f"테스트 리스트: {test_numbers}")

# 테스트 케이스들
test_cases = [
    (25, "25를 찾으면 인덱스 1이 나와야 함"),
    (68, "68을 찾으면 인덱스 5가 나와야 함"), 
    (99, "99를 찾으면 -1이 나와야 함 (없음)")
]

for target, expected in test_cases:
    result = find_number(test_numbers, target)
    print(f"find_number({target}) = {result} ({expected})")

print("\n" + "="*50)

# 문제 2: 학생 성적 관리
print("📝 문제 2: 학생 성적 관리 시스템")
print("딕셔너리로 이루어진 학생 정보에서 다양한 탐색을 해보세요")

students = [
    {"name": "김철수", "score": 85, "grade": "B"},
    {"name": "이영희", "score": 92, "grade": "A"},
    {"name": "박민수", "score": 78, "grade": "C"},
    {"name": "최진성", "score": 96, "grade": "A"},
    {"name": "정수연", "score": 81, "grade": "B"}
]

print(f"학생 정보: {students}")

def find_student_by_name(students, name):
    """이름으로 학생 정보 찾기"""
    # TODO: 이름이 일치하는 학생의 인덱스를 반환하세요
    # 힌트: students[i]["name"] == name 조건 사용
    for i in range(len(students)):
        if students[i]["name"] == name:
            return i
    return -1

def find_top_student(students):
    """최고 점수 학생 찾기"""  
    # TODO: 가장 높은 점수를 가진 학생의 인덱스를 반환하세요
    # 힌트: 최고 점수를 기록해두면서 비교
    best_score = 0
    best_idx = None
    for i in range(len(students)):
        if students[i]["score"] > best_score:
            best_score = students[i]["score"]
            best_idx = i
    return best_idx

def find_students_by_grade(students, target_grade):
    """특정 등급의 학생들 찾기"""
    # TODO: 해당 등급인 모든 학생의 인덱스를 리스트로 반환하세요
    # 힌트: 결과 리스트를 만들고 조건 만족시 append
    result = []
    for i in range(len(students)):
        if students[i]["grade"] == target_grade:
            result.append(i)
    return result


# 테스트
print("\n--- 테스트 ---")
print("1. 이름으로 찾기:")
result = find_student_by_name(students, "이영희")
print(f"이영희 학생 인덱스: {result}")

print("\n2. 최고 점수 학생:")
result = find_top_student(students)  
print(f"최고 점수 학생 인덱스: {result}")

print("\n3. A등급 학생들:")
result = find_students_by_grade(students, "A")
print(f"A등급 학생 인덱스들: {result}")

print("\n" + "="*50)

# 문제 3: 전화번호부
print("📝 문제 3: 전화번호부 검색")
print("튜플로 된 연락처에서 다양한 검색 기능을 만드세요")

contacts = [
    ("김철수", "010-1234-5678", "친구"),
    ("이영희", "010-9876-5432", "동료"), 
    ("박민수", "010-5555-1234", "가족"),
    ("최진성", "010-1111-2222", "친구"),
    ("정수연", "010-9999-8888", "동료")
]

print(f"연락처: {contacts}")

def find_contact_by_name(contacts, name):
    """이름으로 연락처 찾기"""
    # TODO: 이름으로 연락처 전체 정보 반환 (튜플 반환)
    # 힌트: 찾으면 contacts[i] 반환, 없으면 None 반환
    for i in range(len(contacts)):
        if contacts[i][0] == name:
            return contacts[i] 
    return None

def find_contact_by_phone(contacts, phone):
    """전화번호로 연락처 찾기"""
    # TODO: 전화번호로 연락처 찾기
    for i in range(len(contacts)):
        if contacts[i][1] == phone:
            return contacts[i] 
    return None

def find_contacts_by_category(contacts, category):
    """카테고리로 연락처들 찾기"""
    # TODO: 같은 카테고리인 모든 연락처 반환
    result = []
    for i in range(len(contacts)):
        if contacts[i][2] == category:
            result.append(contacts[i])
    if len(result) > 0:
        return result
    else:
        return None

def search_name_partial(contacts, partial_name):
    """이름 부분 검색"""
    # TODO: 이름에 partial_name이 포함된 연락처들 찾기
    # 힌트: if partial_name in contact[0]: 사용
    result = []
    for i in range(len(contacts)):
        if partial_name in contacts[i][0]:
            result.append(contacts[i])
    if len(result) > 0:
        return result
    else:
        return None


# 테스트
print("\n--- 테스트 ---")
print("1. 이름으로 찾기:")
result = find_contact_by_name(contacts, "박민수")
print(f"박민수 연락처: {result}")

print("\n2. 전화번호로 찾기:")
result = find_contact_by_phone(contacts, "010-1111-2222")
print(f"010-1111-2222 연락처: {result}")

print("\n3. 친구 카테고리 찾기:")
result = find_contacts_by_category(contacts, "친구")
print(f"친구들: {result}")

print("\n4. 이름 부분 검색 ('김'):")
result = search_name_partial(contacts, "김")
print(f"'김'이 포함된 연락처: {result}")

print("\n" + "="*50)

# 문제 4: 조건부 탐색 (도전!)
print("📝 문제 4: 조건부 탐색 (도전 문제)")
print("첫 번째로 조건을 만족하는 항목을 찾는 함수들을 만드세요")

numbers = [1, 3, 5, 8, 12, 15, 20, 25, 30]
print(f"숫자 리스트: {numbers}")

def find_first_even(numbers):
    """첫 번째 짝수 찾기"""
    # TODO: 첫 번째 짝수의 인덱스 반환
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            return i
    return -1

def find_first_greater_than(numbers, threshold):
    """임계값보다 큰 첫 번째 수 찾기"""
    # TODO: threshold보다 큰 첫 번째 수의 인덱스 반환
    for i in range(len(numbers)):
        if numbers[i] > threshold:
            return i
    return -1
    

def find_first_divisible_by(numbers, divisor):
    """특정 수로 나누어떨어지는 첫 번째 수 찾기"""
    # TODO: divisor로 나누어떨어지는 첫 번째 수의 인덱스 반환
    for i in range(len(numbers)):
        if numbers[i] % divisor == 0:
            return i
    return -1

# 테스트  
print("\n--- 테스트 ---")
result = find_first_even(numbers)
print(f"첫 번째 짝수 인덱스: {result}")

result = find_first_greater_than(numbers, 10)
print(f"10보다 큰 첫 번째 수 인덱스: {result}")

result = find_first_divisible_by(numbers, 5)
print(f"5로 나누어떨어지는 첫 번째 수 인덱스: {result}")

print("\n" + "="*50)

# 문제 5: 실전 응용 - 게임 인벤토리
print("📝 문제 5: 게임 인벤토리 시스템 (종합 문제)")
print("게임 아이템 인벤토리를 관리하는 클래스를 완성하세요")

class GameInventory:
    def __init__(self):
        # 아이템 정보: [이름, 수량, 타입]
        self.items = [
            ["체력 포션", 5, "소비템"],
            ["마나 포션", 3, "소비템"],
            ["철 검", 1, "무기"],
            ["가죽 갑옷", 1, "방어구"],
            ["마법 반지", 1, "액세서리"]
        ]
        print("🎮 게임 인벤토리 시스템 시작!")
    
    def find_item_by_name(self, item_name):
        """아이템 이름으로 찾기"""
        # TODO: 아이템 이름으로 인덱스 찾기
        for i in range(len(self.items)):
            if self.items[i][0] == item_name:
                return i
        return -1
    
    def find_items_by_type(self, item_type):
        """타입별 아이템들 찾기"""
        # TODO: 같은 타입인 모든 아이템의 인덱스들 반환
        result = []
        for i in range(len(self.items)):
            if self.items[i][2] == item_type:
                result.append(i)
        return result
        
    
    def has_enough_items(self, item_name, required_count):
        """충분한 수량이 있는지 확인"""
        # TODO: 해당 아이템이 required_count 이상 있는지 확인
        # 반환: True/False
        for i in range(len(self.items)):
            if self.items[i][0] == item_name:
                if self.items[i][1] >= required_count:
                    return True
                else:
                    return False
        return None
    
    def show_inventory(self):
        """인벤토리 보기"""
        print("🎒 현재 인벤토리:")
        for i, item in enumerate(self.items):
            name, count, item_type = item
            print(f"  {i}: {name} x{count} ({item_type})")

# 테스트
inventory = GameInventory()
inventory.show_inventory()

print("\n--- 테스트 ---")
print("1. 아이템 찾기:")
result = inventory.find_item_by_name("철 검")
print(f"철 검 인덱스: {result}")

print("\n2. 소비템 찾기:")
result = inventory.find_items_by_type("소비템")
print(f"소비템 인덱스들: {result}")

print("\n3. 수량 확인:")
result = inventory.has_enough_items("체력 포션", 3)
print(f"체력 포션 3개 이상? {result}")

print("\n" + "="*50)

print("🎯 실습 완료 후 체크리스트:")
checklist = [
    "✅ 문제 1: 기본 선형탐색이 올바르게 작동하나요?",
    "✅ 문제 2: 딕셔너리에서 탐색이 잘 되나요?", 
    "✅ 문제 3: 튜플에서 다양한 검색이 가능한가요?",
    "✅ 문제 4: 조건부 탐색을 구현했나요?",
    "✅ 문제 5: 게임 인벤토리가 완전히 작동하나요?"
]

for item in checklist:
    print(item)

print("\n💡 막히는 부분이 있으면 언제든 질문하세요!")
print("📚 핵심: for 반복문으로 처음부터 끝까지 하나씩 확인!")
print("🔥 다음 단계: 이진탐색으로 속도 업그레이드!")