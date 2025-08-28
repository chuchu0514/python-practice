# 📚 이진탐색 완전 가이드

print("=== 📚 이진탐색이란? ===")
print("이진탐색 = 중간부터 확인해서 반절씩 제거!")
print("- 조건: 데이터가 정렬되어 있어야 함")
print("- 방법: 중간값과 비교해서 반절 버리기")
print("- 시간복잡도: O(log n) - 선형탐색보다 훨씬 빠름!")

print("\n💡 실생활 예시:")
print("📖 사전에서 단어 찾기: 중간 페이지부터 확인")
print("🎯 1~100 숫자 맞추기: 50부터 시작해서 범위 좁히기")
print("📚 도서관: 책 번호로 책 찾기")

print("\n🔥 속도 차이:")
print("1,000,000개 데이터에서")
print("📌 선형탐색: 최대 1,000,000번 비교")
print("📌 이진탐색: 최대 20번 비교! (5만배 차이!)")

print("\n" + "="*50)

# 1. 숫자 맞추기 게임으로 이해하기
print("1. 숫자 맞추기 게임으로 이해하기")

def number_guessing_simulation():
    """1~100 숫자 맞추기 - 이진탐색 방식"""
    target = 67  # 정답
    low = 1
    high = 100
    attempts = 0
    
    print(f"🎯 1~100 중에서 {target}을 찾아보세요!")
    print("이진탐색 방식으로 찾는 과정:")
    
    while low <= high:
        attempts += 1
        mid = (low + high) // 2
        
        print(f"시도 {attempts}: 범위[{low}~{high}] → 중간값 {mid} 확인")
        
        if mid == target:
            print(f"🎉 정답! {attempts}번만에 찾았습니다!")
            return attempts
        elif mid < target:
            print(f"   {mid} < {target} → 더 큰 수! 왼쪽 절반 버리기")
            low = mid + 1
        else:
            print(f"   {mid} > {target} → 더 작은 수! 오른쪽 절반 버리기")
            high = mid - 1
    
    print("❌ 찾지 못했습니다.")
    return -1

print("\n=== 숫자 맞추기 시뮬레이션 ===")
number_guessing_simulation()

print(f"\n💡 선형탐색이었다면? 1, 2, 3, ..., 67까지 67번 확인!")
print(f"💡 이진탐색은? 단 7번만에 완료!")

print("\n" + "="*50)

# 2. 기본 이진탐색 구현 (반복문 버전)
print("2. 기본 이진탐색 구현")

def binary_search(arr, target):
    """
    정렬된 배열에서 target을 이진탐색으로 찾기
    
    Args:
        arr: 정렬된 리스트
        target: 찾을 값
        
    Returns:
        int: 찾은 인덱스, 없으면 -1
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # 찾았다!
        elif arr[mid] < target:
            left = mid + 1  # 오른쪽 절반에서 찾기
        else:
            right = mid - 1  # 왼쪽 절반에서 찾기
    
    return -1  # 못찾음

# 테스트
sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"정렬된 리스트: {sorted_numbers}")

test_cases = [7, 15, 20]
for target in test_cases:
    result = binary_search(sorted_numbers, target)
    if result != -1:
        print(f"값 {target}: 인덱스 {result}에서 발견!")
    else:
        print(f"값 {target}: 찾지 못함")

print("\n" + "="*50)

# 3. 단계별 과정 시각화
print("3. 이진탐색 과정 시각화")

def binary_search_verbose(arr, target):
    """이진탐색 과정을 자세히 보여주는 버전"""
    left = 0
    right = len(arr) - 1
    step = 0
    
    print(f"🔍 {target} 찾기 시작!")
    print(f"배열: {arr}")
    
    while left <= right:
        step += 1
        mid = (left + right) // 2
        
        print(f"\n단계 {step}:")
        print(f"  범위: 인덱스 [{left}~{right}] = 값 [{arr[left]}~{arr[right]}]")
        print(f"  중간: 인덱스 {mid} = 값 {arr[mid]}")
        
        if arr[mid] == target:
            print(f"  🎉 찾았다! {target} == {arr[mid]}")
            return mid
        elif arr[mid] < target:
            print(f"  📈 {arr[mid]} < {target} → 오른쪽으로!")
            left = mid + 1
        else:
            print(f"  📉 {arr[mid]} > {target} → 왼쪽으로!")
            right = mid - 1
    
    print(f"  ❌ 못찾음! 범위가 비었음")
    return -1

print("\n=== 15 찾기 과정 ===")
result = binary_search_verbose(sorted_numbers, 15)

print("\n=== 20 찾기 과정 (실패) ===")
result = binary_search_verbose(sorted_numbers, 20)

print("\n" + "="*50)

# 4. 재귀 버전 구현
print("4. 이진탐색 재귀 버전")

def binary_search_recursive(arr, target, left=0, right=None):
    """재귀로 구현한 이진탐색"""
    if right is None:
        right = len(arr) - 1
    
    # 기저 조건: 범위가 잘못되면 못찾음
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# 테스트
print("재귀 버전 테스트:")
for target in [7, 15, 20]:
    result = binary_search_recursive(sorted_numbers, target)
    if result != -1:
        print(f"값 {target}: 인덱스 {result}에서 발견!")
    else:
        print(f"값 {target}: 찾지 못함")

print("\n" + "="*50)

# 5. 성능 비교
print("5. 선형탐색 vs 이진탐색 성능 비교")

import time
import random

def linear_search(arr, target):
    """비교용 선형탐색"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def performance_comparison():
    """성능 비교 테스트"""
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        # 정렬된 테스트 데이터 생성
        test_data = list(range(0, size * 2, 2))  # [0, 2, 4, 6, ...]
        target = random.choice(test_data)  # 랜덤한 타겟 선택
        
        print(f"\n📊 데이터 크기: {size:,}개")
        print(f"찾는 값: {target}")
        
        # 선형탐색 시간 측정
        start_time = time.time()
        linear_result = linear_search(test_data, target)
        linear_time = time.time() - start_time
        
        # 이진탐색 시간 측정
        start_time = time.time()
        binary_result = binary_search(test_data, target)
        binary_time = time.time() - start_time
        
        print(f"선형탐색: {linear_time*1000:.3f}ms")
        print(f"이진탐색: {binary_time*1000:.3f}ms")
        
        if binary_time > 0:
            speedup = linear_time / binary_time
            print(f"🚀 이진탐색이 {speedup:.1f}배 빠름!")

performance_comparison()

print("\n" + "="*50)

# 6. 실생활 예시 - 도서관 시스템
print("6. 실생활 예시: 도서관 도서 검색")

class LibrarySystem:
    def __init__(self):
        # 도서 정보 (도서번호, 제목) - 도서번호로 정렬됨
        self.books = [
            (1001, "파이썬 기초"),
            (1005, "알고리즘 입문"),
            (1010, "데이터구조"),
            (1015, "웹 개발"),
            (1020, "AI 머신러닝"),
            (1025, "데이터베이스"),
            (1030, "네트워크 기초")
        ]
        print("📚 도서관 시스템 시작!")
    
    def find_book_by_id(self, book_id):
        """도서번호로 책 찾기 (이진탐색 사용)"""
        left = 0
        right = len(self.books) - 1
        
        print(f"🔍 도서번호 {book_id} 검색 시작...")
        
        while left <= right:
            mid = (left + right) // 2
            mid_id = self.books[mid][0]
            
            print(f"  중간 위치 확인: 도서번호 {mid_id}")
            
            if mid_id == book_id:
                book = self.books[mid]
                print(f"  📖 찾았습니다: {book[1]}")
                return book
            elif mid_id < book_id:
                print(f"  📈 {mid_id} < {book_id} → 뒤쪽에서 찾기")
                left = mid + 1
            else:
                print(f"  📉 {mid_id} > {book_id} → 앞쪽에서 찾기")
                right = mid - 1
        
        print(f"  ❌ 도서번호 {book_id}를 찾을 수 없습니다")
        return None
    
    def show_books(self):
        """전체 도서 목록"""
        print("\n📚 전체 도서 목록:")
        for book_id, title in self.books:
            print(f"  {book_id}: {title}")

# 도서관 시뮬레이션
print("\n=== 도서관 검색 시뮬레이션 ===")
library = LibrarySystem()
library.show_books()

print("\n--- 도서 검색 ---")
library.find_book_by_id(1015)  # 있는 책
print()
library.find_book_by_id(1018)  # 없는 책

print("\n" + "="*50)

# 7. 이진탐색의 조건과 한계
print("7. 이진탐색의 조건과 한계")

print("\n✅ 이진탐색 사용 조건:")
conditions = [
    "📌 데이터가 정렬되어 있어야 함",
    "📌 랜덤 접근이 가능해야 함 (리스트, 배열)",
    "📌 데이터 크기가 클수록 효과 극대화"
]
for condition in conditions:
    print(f"  {condition}")

print("\n❌ 이진탐색 사용 불가:")
limitations = [
    "📌 정렬되지 않은 데이터",
    "📌 연결 리스트 (인덱스 접근 불가)",
    "📌 데이터가 자주 변경되는 경우",
    "📌 데이터가 매우 작은 경우 (오버헤드)"
]
for limitation in limitations:
    print(f"  {limitation}")

print("\n🤔 언제 어떤 탐색을 사용할까?")
comparison = [
    "📊 데이터 작음 (100개 이하) → 선형탐색도 충분",
    "📊 데이터 큼 + 정렬됨 → 이진탐색 (압도적 승리)",
    "📊 데이터 큼 + 정렬안됨 → 선형탐색 (어쩔 수 없음)",
    "📊 한번만 검색 → 정렬비용 vs 검색속도 고려",
    "📊 여러번 검색 → 미리 정렬해두고 이진탐색"
]
for item in comparison:
    print(f"  {item}")

print("\n" + "="*50)

# 8. 시간복잡도 비교
print("8. 시간복잡도 완전 비교")

def complexity_comparison():
    """다양한 데이터 크기에서 비교 횟수 계산"""
    import math
    
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    
    print("데이터 크기 | 선형탐색(최악) | 이진탐색(최악) | 차이")
    print("-" * 50)
    
    for size in sizes:
        linear_worst = size
        binary_worst = math.ceil(math.log2(size))
        difference = linear_worst / binary_worst
        
        print(f"{size:8,}개 | {linear_worst:10,}번 | {binary_worst:10}번 | {difference:6.0f}배")

complexity_comparison()

print("\n💡 결론:")
print("✅ 이진탐색은 데이터가 클수록 압도적으로 빠름!")
print("✅ 정렬된 데이터에서는 반드시 이진탐색 사용!")
print("✅ 1,000개 이상 데이터부터 확실한 차이!")

print("\n" + "="*50)

# 9. 정리
print("9. 📋 이진탐색 완전 정리")

summary = [
    "🔥 핵심 아이디어: 중간값으로 반절씩 제거",
    "⚡ 시간복잡도: O(log n) - 매우 빠름",
    "📋 필수 조건: 데이터가 정렬되어 있어야 함",
    "🎯 최적 상황: 큰 정렬된 데이터에서 여러 번 검색",
    "💻 구현 방법: 반복문 또는 재귀",
    "🚀 실무 활용: 데이터베이스 인덱스, 검색 엔진 등"
]

for item in summary:
    print(f"  {item}")

print("\n🎮 다음 학습:")
next_topics = [
    "📝 이진탐색 실습: 직접 구현해보기",
    "🏗️ 탐색 프로젝트: 선형 vs 이진 비교 시스템",
    "🌳 트리 자료구조: 이진탐색트리 (BST)",
    "📊 해시 테이블: O(1) 탐색의 끝판왕"
]

for topic in next_topics:
    print(f"  {topic}")

print("\n✅ 이진탐색 개념 완전 마스터!")