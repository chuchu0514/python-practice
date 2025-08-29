# 🎯 이진탐색 실습 문제

print("=== 📚 이진탐색 실습 문제 ===")
print("정렬된 데이터에서 이진탐색을 직접 구현해보세요!")
print("핵심: while left <= right 패턴 완전 마스터!")

print("\n" + "="*50)

# 문제 1: 기본 이진탐색
print("📝 문제 1: 정렬된 숫자에서 찾기")
print("정렬된 리스트에서 이진탐색으로 값을 찾는 함수를 만드세요")

def binary_search(arr, target):
    """
    정렬된 배열에서 이진탐색으로 target 찾기
    
    Args:
        arr: 정렬된 리스트
        target: 찾을 값
        
    Returns:
        int: 찾은 인덱스, 없으면 -1
    """
    # TODO: 이진탐색으로 target의 인덱스 찾기
    # 힌트: left = 0, right = len(arr) - 1
    # 힌트: while left <= right:
    # 힌트: mid = (left + right) // 2
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(f"해당 인덱스는 {mid}입니다")
            return mid
        elif arr[mid] > target:
            print(f"중간값'{arr[mid]}'이 목표'{target}'보다 큽니다.")
            right = mid - 1
        elif arr[mid] < target:
            print(f"중간값'{arr[mid]}'이 목표'{target}'보다 작습니다.")
            left = mid + 1

    print("해당 인덱스가 존재하지 않습니다.")
    return -1


# 테스트
sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 45, 67, 78, 84, 91]
print(f"정렬된 리스트: {sorted_numbers}")

test_cases = [
    (23, "23을 찾으면 인덱스 5가 나와야 함"),
    (67, "67을 찾으면 인덱스 8이 나와야 함"),
    (99, "99를 찾으면 -1이 나와야 함 (없음)")
]

for target, expected in test_cases:
    result = binary_search(sorted_numbers, target)
    print(f"binary_search({target}) = {result} ({expected})")

print("\n" + "="*50)

# 문제 2: 학생 성적 시스템
print("📝 문제 2: 학생 성적 검색 시스템")
print("점수로 정렬된 학생 데이터에서 이진탐색을 사용하세요")

# 점수순으로 정렬된 학생 데이터
students_by_score = [
    ("박민수", 78),
    ("정수연", 81), 
    ("김철수", 85),
    ("이영희", 92),
    ("최진성", 96)
]

print(f"점수순 정렬된 학생: {students_by_score}")

def find_student_by_score(students, target_score):
    """점수로 학생 찾기 (이진탐색)"""
    # TODO: 점수를 기준으로 이진탐색
    # 힌트: students[mid][1]이 점수
    # 찾으면 학생 전체 정보 반환, 없으면 None
    left = 0
    right = len(students) - 1
    while left <= right:
        mid = (left + right) // 2
        if students[mid][1] == target_score:
            print(f"해당 인덱스는 {mid}입니다")
            return students[mid]
        elif students[mid][1] > target_score:
            right = mid - 1
        elif students[mid][1] < target_score:
            left = mid + 1
    print("해당 인덱스가 존재하지 않습니다.")
    return None

def find_first_ge(students, target_score):
    """target_score 이상의 첫 번째 인덱스"""
    left, right = 0, len(students) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if students[mid][1] >= target_score:
            result = mid
            right = mid - 1  # 더 작은 인덱스 찾기
        else:
            left = mid + 1
    return result

def find_students_score_range(students, min_score, max_score):
    min_idx = find_first_ge(students, min_score)
    max_idx = find_first_ge(students, max_score + 1)  # max_score 초과의 첫 번째
    
    if max_idx == -1:  # max_score 초과가 없으면
        max_idx = len(students)  # 전체 길이
    
    max_idx = max_idx - 1  # max_score 이하의 마지막
        
    if min_idx != -1 and max_idx != -1 and min_idx <= max_idx:
        return (min_idx, max_idx)
    return -1

# 테스트
print("\n--- 테스트 ---")
print("1. 점수로 학생 찾기:")
result = find_student_by_score(students_by_score, 85)
print(f"85점 학생: {result}")

print("\n2. 점수 범위로 학생들 찾기:")
result = find_students_score_range(students_by_score, 80, 90)
print(f"80-90점 학생들: {result}")

print("\n" + "="*50)

# 문제 3: 도서관 도서 검색
print("📝 문제 3: 도서관 도서번호 검색")
print("도서번호로 정렬된 도서에서 이진탐색으로 찾으세요")

library_books = [
    (1001, "파이썬 기초", "프로그래밍"),
    (1005, "알고리즘 입문", "컴퓨터과학"),
    (1010, "데이터구조", "컴퓨터과학"), 
    (1015, "웹 개발", "프로그래밍"),
    (1020, "AI 머신러닝", "인공지능"),
    (1025, "데이터베이스", "컴퓨터과학"),
    (1030, "네트워크 기초", "컴퓨터과학"),
    (1035, "앱 개발", "프로그래밍")
]

print(f"도서 목록 (도서번호순): {library_books}")

def find_book_by_id(books, book_id):
    """도서번호로 책 찾기"""
    # TODO: 도서번호(books[i][0])로 이진탐색
    # 찾으면 책 전체 정보 반환, 없으면 None
    left = 0
    right = len(books) - 1
    while left <= right:
        mid = (left + right) // 2
        if books[mid][0] == book_id:
            return books[mid]
        elif books[mid][0] > book_id:
            right = mid -1
        else:
            left = mid + 1
    return None

def find_books_in_id_range(books, start_id, end_id):
    """도서번호 범위에 있는 책들 찾기"""
    # TODO: start_id 이상 end_id 이하인 모든 책 반환
    result = []
    for i in range(len(books)):
        if start_id <= books[i][0] <= end_id:
            result.append(books[i])
    return result

def count_books_by_category(books, category):
    """특정 카테고리 책 개수 세기 (도전!)"""
    # TODO: 이진탐색으로 빠르게 카테고리별 개수 구하기
    # 힌트: 전체를 순회하지 말고 이진탐색 활용
    #!! 클라우드 피셜 출제오류 선형탐색으로 하고 넘어가기 
    count = 0
    for book in books:
        if book[2] == category:  # 카테고리 비교
            count += 1
    return count





# 테스트
print("\n--- 테스트 ---")
print("1. 도서번호로 찾기:")
result = find_book_by_id(library_books, 1015)
print(f"도서번호 1015: {result}")

print("\n2. 도서번호 범위:")
result = find_books_in_id_range(library_books, 1010, 1025)
print(f"1010-1025 범위: {result}")

print("\n3. 카테고리별 개수:")
result = count_books_by_category(library_books, "컴퓨터과학")
print(f"컴퓨터과학 책 개수: {result}")

print("\n" + "="*50)

# 문제 4: 게임 레벨 시스템
print("📝 문제 4: 게임 레벨 시스템")
print("경험치에 따른 레벨을 이진탐색으로 빠르게 찾으세요")

# 레벨별 필요 경험치 (정렬되어 있음)
level_exp = [
    (1, 0),      # 1레벨: 0 경험치
    (2, 100),    # 2레벨: 100 경험치  
    (3, 250),    # 3레벨: 250 경험치
    (4, 450),    # 4레벨: 450 경험치
    (5, 700),    # 5레벨: 700 경험치
    (6, 1000),   # 6레벨: 1000 경험치
    (7, 1350),   # 7레벨: 1350 경험치
    (8, 1750),   # 8레벨: 1750 경험치
    (9, 2200),   # 9레벨: 2200 경험치
    (10, 2700)   # 10레벨: 2700 경험치
]

print("레벨 시스템:")
for level, exp in level_exp:
    print(f"  레벨 {level}: {exp} 경험치")

def find_level_by_exp(level_data, current_exp):
    """현재 경험치로 레벨 찾기"""
    # TODO: 현재 경험치에 해당하는 최고 레벨 찾기
    # 힌트: current_exp보다 작거나 같은 가장 큰 경험치 찾기
    pass

def exp_needed_for_next_level(level_data, current_exp):
    """다음 레벨까지 필요한 경험치"""
    # TODO: 다음 레벨까지 얼마나 더 필요한지 계산
    pass

# 테스트
print("\n--- 테스트 ---")
test_exps = [150, 500, 1200, 3000]

for exp in test_exps:
    level_info = find_level_by_exp(level_exp, exp)
    needed = exp_needed_for_next_level(level_exp, exp)
    print(f"경험치 {exp}: 현재 레벨 {level_info}, 다음 레벨까지 {needed} 필요")

print("\n" + "="*50)

# 문제 5: 성능 비교 시스템 (종합 문제)
print("📝 문제 5: 선형탐색 vs 이진탐색 성능 비교")
print("두 탐색의 속도 차이를 직접 측정해보세요")

import time
import random

def linear_search(arr, target):
    """비교용 선형탐색"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

class SearchPerformanceTester:
    def __init__(self):
        self.test_sizes = [1000, 5000, 10000, 50000]
        print("🚀 탐색 성능 테스터 시작!")
    
    def generate_sorted_data(self, size):
        """정렬된 테스트 데이터 생성"""
        # TODO: 정렬된 데이터 생성
        # 힌트: list(range(0, size * 2, 2)) 같은 방식
        pass
    
    def measure_search_time(self, search_func, data, target, iterations=1000):
        """탐색 함수의 실행 시간 측정"""
        # TODO: 여러 번 실행해서 평균 시간 계산
        # 힌트: time.time() 사용
        pass
    
    def compare_searches(self):
        """선형탐색과 이진탐색 비교"""
        print("\n📊 성능 비교 결과:")
        print("데이터 크기 | 선형탐색 | 이진탐색 | 속도 향상")
        print("-" * 50)
        
        for size in self.test_sizes:
            data = self.generate_sorted_data(size)
            target = random.choice(data)
            
            # TODO: 각각의 실행 시간 측정
            linear_time = self.measure_search_time(linear_search, data, target)
            binary_time = self.measure_search_time(binary_search, data, target)
            
            # TODO: 결과 출력
            if binary_time > 0:
                speedup = linear_time / binary_time
                print(f"{size:8}개 | {linear_time:7.3f}ms | {binary_time:7.3f}ms | {speedup:6.1f}x")
            else:
                print(f"{size:8}개 | {linear_time:7.3f}ms | 측정불가    | 매우빠름")

# 테스트
tester = SearchPerformanceTester()
# tester.compare_searches()  # 구현 완료 후 주석 해제

print("\n" + "="*50)

# 문제 6: 실전 응용 - 온라인 상점 (도전!)
print("📝 문제 6: 온라인 상점 가격 검색 (도전 문제)")
print("가격으로 정렬된 상품에서 다양한 검색 기능을 구현하세요")

# 가격순으로 정렬된 상품들
products = [
    ("키보드", 25000, "전자제품"),
    ("마우스", 35000, "전자제품"),
    ("헤드폰", 45000, "전자제품"),
    ("모니터", 150000, "전자제품"),
    ("책상", 180000, "가구"),
    ("의자", 220000, "가구"),
    ("노트북", 800000, "전자제품")
]

print("상품 목록 (가격순):")
for name, price, category in products:
    print(f"  {name}: {price:,}원 ({category})")

def find_product_by_price(products, target_price):
    """정확한 가격으로 상품 찾기"""
    # TODO: 가격으로 이진탐색
    pass

def find_products_under_budget(products, max_budget):
    """예산 이하의 모든 상품 찾기"""
    # TODO: max_budget 이하인 모든 상품 반환
    pass

def find_cheapest_in_category(products, category):
    """특정 카테고리에서 가장 저렴한 상품"""
    # TODO: 해당 카테고리에서 가장 저렴한 상품 찾기
    pass

def find_price_range_products(products, min_price, max_price):
    """가격 범위 내 상품들 찾기"""
    # TODO: min_price 이상 max_price 이하 상품들 반환
    pass

# 테스트
print("\n--- 테스트 ---")
print("1. 정확한 가격으로 찾기:")
result = find_product_by_price(products, 45000)
print(f"45,000원 상품: {result}")

print("\n2. 예산 이하 상품들:")
result = find_products_under_budget(products, 100000)
print(f"10만원 이하: {result}")

print("\n3. 카테고리별 최저가:")
result = find_cheapest_in_category(products, "전자제품")
print(f"전자제품 최저가: {result}")

print("\n4. 가격 범위:")
result = find_price_range_products(products, 40000, 200000)
print(f"4-20만원 범위: {result}")

print("\n" + "="*50)

print("🎯 실습 완료 후 체크리스트:")
checklist = [
    "✅ 문제 1: 기본 이진탐색이 올바르게 작동하나요?",
    "✅ 문제 2: 학생 점수로 검색이 잘 되나요?", 
    "✅ 문제 3: 도서번호 검색과 범위 검색이 가능한가요?",
    "✅ 문제 4: 게임 레벨 시스템이 정확히 작동하나요?",
    "✅ 문제 5: 성능 비교에서 이진탐색이 빠른가요?",
    "✅ 문제 6: 온라인 상점의 모든 검색 기능이 작동하나요?"
]

for item in checklist:
    print(item)

print("\n💡 핵심 패턴:")
print("while left <= right:")
print("    mid = (left + right) // 2")
print("    if arr[mid] == target:")
print("        return mid")
print("    elif arr[mid] < target:")
print("        left = mid + 1")
print("    else:")
print("        right = mid - 1")

print("\n🚀 막히는 부분이 있으면 언제든 질문하세요!")
print("📚 다음 단계: 탐색 프로젝트 또는 트리 자료구조!")