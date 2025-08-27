# 📚 선형탐색 완전 가이드

print("=== 📚 선형탐색이란? ===")
print("선형탐색 = 처음부터 끝까지 하나씩 확인!")
print("- 가장 단순하고 확실한 방법")
print("- 정렬되지 않은 데이터에서도 사용 가능")
print("- 시간복잡도: O(n)")

print("\n💡 실생활 예시:")
print("📚 도서관에서 책 찾기: 첫 번째 책장부터 차례로 확인")
print("🎮 게임 인벤토리: 첫 번째 슬롯부터 아이템 찾기")
print("📞 전화번호부: 맨 위부터 이름 찾기")

print("\n" + "="*50)

# 1. 기본 선형탐색 구현
print("1. 기본 선형탐색")

def linear_search(arr, target):
    """선형탐색으로 target 값의 인덱스 찾기"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # 찾으면 인덱스 반환
    return -1  # 못찾으면 -1 반환

# 테스트
numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"리스트: {numbers}")

search_value = 22
result = linear_search(numbers, search_value)

if result != -1:
    print(f"값 {search_value}을(를) 인덱스 {result}에서 찾았습니다!")
else:
    print(f"값 {search_value}을(를) 찾지 못했습니다.")

print("\n" + "="*50)

# 2. 문자열 리스트에서 탐색
print("2. 문자열 탐색")

def search_student(students, name):
    """학생 목록에서 특정 학생 찾기"""
    for i, student in enumerate(students):
        if student == name:
            return i
    return -1

students = ["김철수", "이영희", "박민수", "최진성", "정수연"]
print(f"학생 목록: {students}")

find_name = "박민수"
index = search_student(students, find_name)

if index != -1:
    print(f"{find_name} 학생을 {index+1}번째에서 찾았습니다!")
else:
    print(f"{find_name} 학생을 찾지 못했습니다.")

print("\n" + "="*50)

# 3. 조건부 탐색
print("3. 조건부 탐색 (특정 조건 만족하는 첫 번째 값)")

def find_first_even(numbers):
    """첫 번째 짝수 찾기"""
    for i, num in enumerate(numbers):
        if num % 2 == 0:
            return i
    return -1

def find_first_greater_than(numbers, threshold):
    """임계값보다 큰 첫 번째 수 찾기"""
    for i, num in enumerate(numbers):
        if num > threshold:
            return i
    return -1

test_numbers = [1, 3, 7, 8, 15, 20, 25]
print(f"숫자 목록: {test_numbers}")

even_index = find_first_even(test_numbers)
if even_index != -1:
    print(f"첫 번째 짝수: {test_numbers[even_index]} (인덱스 {even_index})")

greater_index = find_first_greater_than(test_numbers, 10)
if greater_index != -1:
    print(f"10보다 큰 첫 번째 수: {test_numbers[greater_index]} (인덱스 {greater_index})")

print("\n" + "="*50)

# 4. 실생활 예시 - 게임 인벤토리
print("4. 실생활 예시: 게임 인벤토리")

class GameInventory:
    def __init__(self):
        self.items = []
        print("🎮 게임 인벤토리 시스템 시작!")
    
    def add_item(self, item_name):
        """아이템 추가"""
        self.items.append(item_name)
        print(f"📦 {item_name} 획득!")
    
    def find_item(self, item_name):
        """아이템 찾기 (선형탐색 사용)"""
        for i, item in enumerate(self.items):
            if item == item_name:
                return i
        return -1
    
    def use_item(self, item_name):
        """아이템 사용하기"""
        index = self.find_item(item_name)
        if index != -1:
            used_item = self.items.pop(index)
            print(f"✨ {used_item} 사용!")
            return True
        else:
            print(f"❌ {item_name}이(가) 인벤토리에 없습니다!")
            return False
    
    def show_inventory(self):
        """인벤토리 보기"""
        if not self.items:
            print("📦 인벤토리가 비어있습니다")
            return
        
        print("🎒 현재 인벤토리:")
        for i, item in enumerate(self.items):
            print(f"  {i+1}. {item}")

# 게임 시뮬레이션
print("\n=== 게임 인벤토리 테스트 ===")
inventory = GameInventory()

print("\n--- 아이템 획득 ---")
inventory.add_item("체력 포션")
inventory.add_item("마법 검")
inventory.add_item("방패")
inventory.add_item("마나 포션")

inventory.show_inventory()

print("\n--- 아이템 사용 ---")
inventory.use_item("마법 검")  # 성공
inventory.use_item("화염 마법서")  # 실패 (없는 아이템)

inventory.show_inventory()

print("\n" + "="*50)

# 5. 성능 분석
print("5. 선형탐색 성능 분석")

import time

def performance_test():
    """선형탐색 성능 테스트"""
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        # 테스트 데이터 생성
        test_data = list(range(size))
        target = size - 1  # 가장 마지막 원소 (최악의 경우)
        
        # 시간 측정
        start_time = time.time()
        result = linear_search(test_data, target)
        end_time = time.time()
        
        print(f"데이터 크기: {size:,}개")
        print(f"탐색 시간: {(end_time - start_time)*1000:.2f}ms")
        print(f"비교 횟수: {result + 1}회")
        print()

performance_test()

print("📊 성능 특징:")
print("✅ 최선의 경우: O(1) - 첫 번째에서 발견")
print("❌ 최악의 경우: O(n) - 마지막에서 발견 또는 없음")
print("📈 평균: O(n/2) - 중간 정도에서 발견")

print("\n" + "="*50)

# 6. 선형탐색의 장단점
print("6. 선형탐색 장단점")

advantages = [
    "✅ 구현이 매우 간단",
    "✅ 정렬되지 않은 데이터에서도 사용 가능", 
    "✅ 추가 메모리 불필요",
    "✅ 작은 데이터에서는 충분히 빠름"
]

disadvantages = [
    "❌ 큰 데이터에서는 매우 느림",
    "❌ 항상 모든 원소를 확인할 수도 있음",
    "❌ 데이터가 정렬되어 있어도 활용 못함"
]

print("🔥 장점:")
for advantage in advantages:
    print(f"  {advantage}")

print("\n💔 단점:")
for disadvantage in disadvantages:
    print(f"  {disadvantage}")

print("\n💡 언제 사용할까?")
when_to_use = [
    "📌 데이터가 작을 때 (100개 이하)",
    "📌 데이터가 정렬되지 않았을 때",
    "📌 한 번만 탐색할 때",
    "📌 구현 속도가 중요할 때"
]

for use_case in when_to_use:
    print(f"  {use_case}")

print("\n✅ 선형탐색 기초 완료!")