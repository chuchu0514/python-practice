# 📚 Phase 5 고급 문법 완전 가이드

print("=== 🚀 Phase 5 고급 문법 마스터 ===")
print("리스트 컴프리헨션, enumerate/zip, *args/**kwargs, 람다 함수")
print("=" * 60)

# ================================================================
# 1. 리스트 컴프리헨션 (List Comprehension)
# ================================================================

print("\n📋 1. 리스트 컴프리헨션")
print("-" * 40)

# 기본 문법: [표현식 for 변수 in 반복가능객체]
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(f"제곱수: {squares}")  # [1, 4, 9, 16, 25]

# 조건부 컴프리헨션: [표현식 for 변수 in 반복가능객체 if 조건]
evens = [n for n in numbers if n % 2 == 0]
print(f"짝수만: {evens}")  # [2, 4]

# 조건부 표현식
result = [n**2 if n % 2 == 0 else n**3 for n in numbers]
print(f"짝수는 제곱, 홀수는 세제곱: {result}")  # [1, 4, 27, 16, 125]

# 문자열 처리
words = ["apple", "banana", "cherry", "date"]
lengths = [len(word) for word in words]
print(f"문자열 길이들: {lengths}")  # [5, 6, 6, 4]

long_words = [word.upper() for word in words if len(word) > 5]
print(f"긴 단어들 대문자: {long_words}")  # ['BANANA', 'CHERRY']

# 중첩 컴프리헨션 (2차원 리스트)
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"구구단 매트릭스: {matrix}")  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# 2차원 리스트 평탄화
flattened = [num for row in matrix for num in row]
print(f"평탄화된 리스트: {flattened}")  # [1, 2, 3, 2, 4, 6, 3, 6, 9]

# Set와 Dictionary 컴프리헨션
unique_squares = {n**2 for n in [1, 2, 2, 3, 3, 4]}
print(f"중복 제거된 제곱수: {unique_squares}")  # {1, 4, 9, 16}

word_lengths = {word: len(word) for word in words}
print(f"단어-길이 딕셔너리: {word_lengths}")

print("\n" + "="*60)

# ================================================================
# 2. enumerate와 zip
# ================================================================

print("\n🔢 2. enumerate와 zip")
print("-" * 40)

# enumerate - 인덱스와 값 동시 접근
print("📌 enumerate 예제:")
fruits = ["apple", "banana", "cherry"]

print("기존 방식:")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

print("enumerate 사용:")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

print("시작 인덱스 지정:")
for i, fruit in enumerate(fruits, 1):
    print(f"  {i}등: {fruit}")

# enumerate와 컴프리헨션
indexed_fruits = [(i, fruit) for i, fruit in enumerate(fruits)]
print(f"인덱스-과일 튜플: {indexed_fruits}")

print("\n📌 zip 예제:")
# zip - 여러 리스트 동시 순회
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Seoul", "Busan", "Incheon"]

print("여러 리스트 동시 순회:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}세, {city}")

# 길이가 다른 리스트
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(f"길이 다른 리스트 zip: {zipped}")  # 짧은 것 기준

# 딕셔너리 생성
keys = ["name", "age", "city"]
values = ["Alice", 25, "Seoul"]
person = dict(zip(keys, values))
print(f"zip으로 딕셔너리 생성: {person}")

# zip 언팩킹 (역연산)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(f"zip 언팩킹 - 숫자: {numbers}, 문자: {letters}")

# enumerate + zip 조합
print("\nenumerate + zip 조합:")
scores1 = [85, 92, 78, 96]
scores2 = [90, 87, 93, 89]

for i, (score1, score2) in enumerate(zip(scores1, scores2)):
    diff = abs(score1 - score2)
    print(f"  {i+1}번째 시험 점수차: {diff}점")

print("\n" + "="*60)

# ================================================================
# 3. *args와 **kwargs
# ================================================================

print("\n🔧 3. *args와 **kwargs")
print("-" * 40)

print("📌 *args (가변 위치 인수):")

def add_all(*args):
    """모든 인수를 더하는 함수"""
    return sum(args)

print(f"add_all(1, 2, 3): {add_all(1, 2, 3)}")
print(f"add_all(1, 2, 3, 4, 5): {add_all(1, 2, 3, 4, 5)}")

def print_info(name, *hobbies):
    """이름과 여러 취미를 출력"""
    print(f"  이름: {name}")
    if hobbies:
        print(f"  취미: {', '.join(hobbies)}")

print_info("진성", "코딩", "게임", "독서")

# 리스트 언팩킹
numbers = [1, 2, 3, 4, 5]
print(f"리스트 언팩킹: add_all(*{numbers}) = {add_all(*numbers)}")

print("\n📌 **kwargs (가변 키워드 인수):")

def print_person(**kwargs):
    """사람 정보를 출력"""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("키워드 인수로 호출:")
print_person(name="Alice", age=25, city="Seoul", job="개발자")

# def print_person(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_person(**{"name": "Alice", "age": 25, "city": "Seoul"})  # ✅ 가능

# def print_person(kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# data = {"name": "Alice", "age": 25, "city": "Seoul"}
# print_person(data)  # ✅ 가능


# 딕셔너리 언팩킹
person_info = {"name": "Bob", "age": 30, "hobby": "음악"}
print("\n딕셔너리 언팩킹:")
print_person(**person_info)

print("\n📌 *args + **kwargs 조합:")

def flexible_function(*args, **kwargs):
    """유연한 함수 - 모든 종류의 인수 받기"""
    print(f"  위치 인수: {args}")
    print(f"  키워드 인수: {kwargs}")
    return len(args) + len(kwargs)

result = flexible_function(1, 2, 3, name="Alice", age=25)
print(f"  총 인수 개수: {result}")
# *는 튜플 **는 딕셔너리 

# 함수 래퍼 만들기
def timer_decorator(func):
    """함수 실행 시간을 측정하는 데코레이터"""
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  함수 '{func.__name__}' 실행시간: {end-start:.6f}초")
        return result
    return wrapper

@timer_decorator
def slow_function(n):
    """시간이 걸리는 함수 시뮬레이션"""
    total = sum(i**2 for i in range(n))
    return total

print(f"\n데코레이터 테스트:")
result = slow_function(10000)
print(f"결과: {result}")

print("\n" + "="*60)

# ================================================================
# 4. 람다 함수 심화
# ================================================================

print("\n🔥 4. 람다 함수 심화")
print("-" * 40)

print("📌 기본 람다 함수:")
# 기본 람다
square = lambda x: x ** 2
add = lambda x, y: x + y
max_lambda = lambda x, y: x if x > y else y

print(f"square(5): {square(5)}")
print(f"add(3, 7): {add(3, 7)}")
print(f"max_lambda(10, 5): {max_lambda(10, 5)}")

print("\n📌 map()과 람다:")
numbers = [1, 2, 3, 4, 5]

# 제곱 계산
squares = list(map(lambda x: x**2, numbers))
print(f"제곱들: {squares}")

# 문자열 처리
words = ["apple", "banana", "cherry"]
lengths = list(map(lambda word: len(word), words))
print(f"문자열 길이들: {lengths}")

# 두 리스트 연산
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"두 리스트 합: {sums}")

print("\n📌 filter()와 람다:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 짝수만 필터링
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"짝수들: {evens}")

# 5보다 큰 수
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"5보다 큰 수들: {greater_than_5}")

# 문자열 필터링
words = ["apple", "banana", "cherry", "date", "elderberry"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(f"긴 단어들: {long_words}")

print("\n📌 sorted()와 람다:")
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 90},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 95}
]

# 성적순 정렬
by_grade = sorted(students, key=lambda student: student["grade"])
print("성적순 정렬:")
for student in by_grade:
    print(f"  {student['name']}: {student['grade']}")

# 이름순 정렬 (역순)
by_name = sorted(students, key=lambda student: student["name"], reverse=True)
print("이름 역순:")
for student in by_name:
    print(f"  {student['name']}")

# 복잡한 정렬 (이름 길이 → 성적 순)
complex_sort = sorted(students, key=lambda s: (len(s["name"]), s["grade"]))
print("이름길이 → 성적 순:")
for student in complex_sort:
    print(f"  {student['name']} ({len(student['name'])}글자): {student['grade']}")

print("\n📌 고급 람다 활용:")
# 연산 딕셔너리
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else "Error: Division by zero"
}

print("연산 딕셔너리:")
print(f"  3 + 5 = {operations['add'](3, 5)}")
print(f"  10 * 4 = {operations['multiply'](10, 4)}")
print(f"  8 / 0 = {operations['divide'](8, 0)}")

# 클로저 (람다를 반환하는 함수)
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"\n클로저 예제:")
print(f"  double(5) = {double(5)}")
print(f"  triple(4) = {triple(4)}")

print("\n" + "="*60)

# ================================================================
# 5. 실전 종합 예제: 학생 성적 관리 시스템
# ================================================================

print("\n🎯 5. 실전 종합 예제: 학생 성적 관리 시스템")
print("-" * 50)

# 학생 데이터
students_data = [
    {"name": "Alice", "scores": [85, 92, 78, 96], "class": "A"},
    {"name": "Bob", "scores": [90, 87, 93, 89], "class": "A"},
    {"name": "Charlie", "scores": [78, 85, 82, 79], "class": "B"},
    {"name": "Diana", "scores": [95, 98, 94, 97], "class": "A"},
    {"name": "Eve", "scores": [88, 91, 87, 90], "class": "B"},
    {"name": "Frank", "scores": [72, 75, 78, 74], "class": "B"}
]

subjects = ["수학", "영어", "과학", "사회"]

print("📊 원본 데이터:")
for student in students_data:
    print(f"  {student['name']} ({student['class']}반): {student['scores']}")

# 1. 각 학생의 평균 계산 (map + 람다)
print(f"\n📈 1. 학생별 평균 계산:")
students_with_avg = list(map(lambda student: {
    **student,
    "average": sum(student["scores"]) / len(student["scores"])
}, students_data))

for student in students_with_avg:
    print(f"  {student['name']}: {student['average']:.1f}점")

# 2. 우수학생 필터링 (filter + 람다)
print(f"\n🏆 2. 우수학생 (평균 90점 이상):")
high_achievers = list(filter(lambda s: s["average"] >= 90, students_with_avg))
high_achiever_names = [s["name"] for s in high_achievers]
print(f"  총 {len(high_achievers)}명: {', '.join(high_achiever_names)}")

# 3. 성적순 정렬 (sorted + 람다)
print(f"\n📋 3. 전체 성적 순위:")
sorted_students = sorted(students_with_avg, key=lambda s: s["average"], reverse=True)
for rank, student in enumerate(sorted_students, 1):
    grade = "A" if student["average"] >= 90 else "B" if student["average"] >= 80 else "C"
    print(f"  {rank}등: {student['name']} ({student['average']:.1f}점, {grade}등급)")

# 4. 반별 통계 (리스트 컴프리헨션 + 고급 기법)
print(f"\n🏫 4. 반별 통계:")
classes = list(set(s["class"] for s in students_data))  # 중복 제거

class_stats = {
    class_name: {
        "students": [s for s in students_with_avg if s["class"] == class_name],
        "count": len([s for s in students_with_avg if s["class"] == class_name]),
        "average": sum(s["average"] for s in students_with_avg if s["class"] == class_name) / 
                  len([s for s in students_with_avg if s["class"] == class_name])
    }
    for class_name in classes
}

for class_name, stats in class_stats.items():
    print(f"  {class_name}반: 학생수 {stats['count']}명, 평균 {stats['average']:.1f}점")
    students_names = [s["name"] for s in stats["students"]]
    print(f"    학생들: {', '.join(students_names)}")

# 5. 과목별 통계 (zip + enumerate)
print(f"\n📚 5. 과목별 통계:")
all_scores_by_subject = list(zip(*[student["scores"] for student in students_data]))

for i, (subject, scores) in enumerate(zip(subjects, all_scores_by_subject)):
    avg_score = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    print(f"  {subject}: 평균 {avg_score:.1f}점 (최고 {max_score}, 최저 {min_score})")

# 6. 개인별 상세 리포트 생성 함수 (*args, **kwargs 활용)
def generate_student_report(student_data, *additional_info, **options):
    """학생 개인 리포트 생성"""
    show_details = options.get('show_details', True)
    show_rank = options.get('show_rank', False)
    
    print(f"\n📄 {student_data['name']} 학생 리포트")
    print(f"  반: {student_data['class']}반")
    print(f"  평균 점수: {student_data['average']:.1f}점")
    
    if show_details:
        for i, (subject, score) in enumerate(zip(subjects, student_data['scores'])):
            print(f"  {subject}: {score}점")
    
    if additional_info:
        print(f"  추가 정보: {', '.join(additional_info)}")
    
    if show_rank:
        rank = sorted_students.index(student_data) + 1
        total = len(sorted_students)
        print(f"  전체 순위: {rank}/{total}등")

# 리포트 생성 예제
generate_student_report(
    students_with_avg[0], 
    "수학 특기생", "학급 임원",
    show_rank=True, 
    show_details=True
)

# 7. 고급 분석 (람다 + 컴프리헨션 조합)
print(f"\n🔍 6. 고급 분석:")

# 각 학생의 최고/최저 과목 찾기
student_analysis = [
    {
        "name": student["name"],
        "best_subject": subjects[student["scores"].index(max(student["scores"]))],
        "best_score": max(student["scores"]),
        "worst_subject": subjects[student["scores"].index(min(student["scores"]))],
        "worst_score": min(student["scores"]),
        "score_range": max(student["scores"]) - min(student["scores"])
    }
    for student in students_data
]

print("학생별 최고/최저 과목:")
for analysis in student_analysis:
    print(f"  {analysis['name']}: 최고 {analysis['best_subject']}({analysis['best_score']}점), "
          f"최저 {analysis['worst_subject']}({analysis['worst_score']}점), "
          f"편차 {analysis['score_range']}점")

# 8. 함수형 프로그래밍 스타일 요약
print(f"\n📊 7. 전체 요약 (함수형 스타일):")

# 체이닝 스타일로 전체 분석
summary = {
    "총_학생수": len(students_data),
    "전체_평균": sum(s["average"] for s in students_with_avg) / len(students_with_avg),
    "최고점": max(s["average"] for s in students_with_avg),
    "최저점": min(s["average"] for s in students_with_avg),
    "우수학생_비율": len(high_achievers) / len(students_data) * 100,
    "과목별_최고평균": max(sum(scores)/len(scores) for scores in all_scores_by_subject),
    "가장_어려운_과목": subjects[
        [sum(scores)/len(scores) for scores in all_scores_by_subject]
        .index(min(sum(scores)/len(scores) for scores in all_scores_by_subject))
    ]
}

for key, value in summary.items():
    if isinstance(value, float):
        print(f"  {key.replace('_', ' ')}: {value:.1f}")
    else:
        print(f"  {key.replace('_', ' ')}: {value}")

print("\n" + "="*60)

# ================================================================
# 마무리 및 핵심 포인트
# ================================================================

print("\n🎯 고급 문법 핵심 포인트")
print("-" * 40)

tips = [
    "리스트 컴프리헨션: 간단한 변환/필터링에 사용, 복잡하면 일반 반복문",
    "enumerate: range(len()) 대신 사용하여 인덱스와 값 동시 접근",
    "zip: 여러 리스트 동시 순회, 딕셔너리 생성에 유용",
    "람다: map/filter/sorted의 key 함수로 주로 사용",
    "*args/**kwargs: 유연한 함수 만들 때, 함수 래퍼 구현 시 필수",
    "성능: 리스트 컴프리헨션 > map/filter + 람다",
    "가독성: 너무 복잡한 컴프리헨션보다는 명확한 반복문이 나을 수 있음"
]

for i, tip in enumerate(tips, 1):
    print(f"{i}. {tip}")

print(f"\n💡 실무 꿀팁:")
practical_tips = [
    "데이터 전처리: 리스트 컴프리헨션 + 람다 조합",
    "API 응답 가공: enumerate로 인덱스 추가, zip으로 매핑",
    "설정 함수: **kwargs로 옵션 처리",
    "이터레이터 체이닝: map → filter → sorted 순서로 연결",
    "디버깅: 복잡한 컴프리헨션은 중간 결과 확인"
]

for tip in practical_tips:
    print(f"  • {tip}")

print(f"\n🚀 다음 단계: 트리 자료구조")
print("  이제 고급 문법을 활용해서 트리/그래프를 더 깔끔하게 구현할 수 있습니다!")
print("  특히 트리 순회에서 리스트 컴프리헤션이 매우 유용해요!")

print(f"\n✅ Phase 5 고급 문법 완전 마스터 완료! 🎉")