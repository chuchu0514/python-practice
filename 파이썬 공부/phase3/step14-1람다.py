# 일반 함수 vs 람다 함수 비교

print("=== 1. 기본 비교 ===")

# 일반 함수 방식
def add_normal(x, y):
    return x + y

# 람다 함수 방식  
add_lambda = lambda x, y: x + y

# 사용법은 똑같음!
print(f"일반 함수: {add_normal(3, 5)}")
print(f"람다 함수: {add_lambda(3, 5)}")

print("\n=== 2. 람다 문법 ===")
print("lambda 매개변수: 반환값")
print("lambda x, y: x + y")

# 다양한 람다 예시
square = lambda x: x * x              # 제곱
greet = lambda name: f"안녕 {name}!"   # 인사
is_even = lambda n: n % 2 == 0        # 짝수 판별
max_of_two = lambda a, b: a if a > b else b  # 더 큰 값

print(f"제곱: {square(4)}")
print(f"인사: {greet('진성')}")
print(f"짝수?: {is_even(10)}")
print(f"더 큰 값: {max_of_two(15, 8)}")

print("\n=== 3. 람다의 특징 ===")
print("✅ 한 줄로 간단한 함수 작성")
print("✅ return 키워드 필요 없음 (자동으로 반환)")
print("✅ 익명 함수 (이름 없이도 사용 가능)")
print("❌ 복잡한 로직은 일반 함수가 better")

print("\n=== 4. 즉석에서 사용 (익명) ===")
# 변수에 저장하지 않고 바로 사용
result = (lambda x, y: x * y)(4, 6)
print(f"즉석 계산: {result}")

# 하지만 이렇게 쓰는 경우는 거의 없음...

# 람다의 진짜 활용처!

print("=== 1. map() 함수와 람다 ===")
# 리스트의 모든 원소에 같은 작업 적용

numbers = [1, 2, 3, 4, 5]

# 일반 함수로 하면...
def square_normal(x):
    return x * x

squared_normal = list(map(square_normal, numbers))

# 람다로 하면 한 줄!
squared_lambda = list(map(lambda x: x * x, numbers))

print(f"원본: {numbers}")
print(f"제곱 (일반): {squared_normal}")
print(f"제곱 (람다): {squared_lambda}")

# 다른 예시들
doubled = list(map(lambda x: x * 2, numbers))
strings = list(map(lambda x: f"숫자{x}", numbers))

print(f"2배: {doubled}")
print(f"문자열: {strings}")

print("\n=== 2. filter() 함수와 람다 ===")
# 조건에 맞는 원소만 걸러내기

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 짝수만 걸러내기
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"짝수만: {evens}")

# 5보다 큰 수만
greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"5보다 큰 수: {greater_than_5}")

print("\n=== 3. sorted() 함수와 람다 ===")
# 정렬 기준을 람다로 지정

students = [
    ("김철수", 85),
    ("이영희", 92),
    ("박민수", 78),
    ("최지영", 96)
]

# print("\n✅ 올바른 설명:")
# print("sorted(students, key=lambda student: student[1])")
# print("       ↑               ↑")
# print("    첫번째 인수        두번째 인수")
# print("    (실제 값)         (실제 함수)")

# 성적 순으로 정렬
by_score = sorted(students, key=lambda student: student[1])
print(f"성적순: {by_score}")

# 이름 순으로 정렬  
by_name = sorted(students, key=lambda student: student[0])
print(f"이름순: {by_name}")

# 문자열 길이로 정렬
words = ["python", "java", "c", "javascript", "go"]
by_length = sorted(words, key=lambda word: len(word))
print(f"길이순: {by_length}")

print("\n=== 4. 실전 예시 ===")
# 온도 데이터 처리
temperatures_celsius = [0, 10, 20, 30, 40]

# 섭씨를 화씨로 변환
fahrenheit = list(map(lambda c: c * 9/5 + 32, temperatures_celsius))
print(f"섭씨: {temperatures_celsius}")
print(f"화씨: {fahrenheit}")

# 따뜻한 날씨만 (20도 이상)
warm_days = list(filter(lambda temp: temp >= 20, temperatures_celsius))
print(f"따뜻한 날: {warm_days}")



# print("=== 패턴 1: map, filter (함수가 첫 번째) ===")
# print("map(함수, 리스트)")
# print("filter(함수, 리스트)")

# # map 사용
# doubled = list(map(lambda x: x * 2, numbers))
# print(f"map 결과: {doubled}")

# # filter 사용  
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(f"filter 결과: {evens}")

# print("\n=== 패턴 2: sorted, max, min (리스트가 첫 번째) ===")
# print("sorted(리스트, key=함수)")
# print("max(리스트, key=함수)")
# print("min(리스트, key=함수)")