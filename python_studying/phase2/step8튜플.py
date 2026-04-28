# 📦 Phase 2-2: 튜플(Tuple) 완전 가이드

print("=== 📦 튜플(Tuple) 완전 가이드 ===")

# 1. 튜플 만들기
print("1. 튜플 만들기")
coordinates = (3, 4)
colors = ("빨강", "파랑", "노랑")
mixed = (1, "안녕", 3.14, True)
empty_tuple = ()
single_tuple = (42,)  # 쉼표 필수!

print(f"좌표: {coordinates}")
print(f"색깔들: {colors}")
print(f"섞인 튜플: {mixed}")
print(f"빈 튜플: {empty_tuple}")
print(f"요소 하나인 튜플: {single_tuple}")

print("\n💡 주의: 요소가 하나일 때는 쉼표(,) 필수!")

print("\n" + "="*40)

# 2. 튜플 vs 리스트 차이점
print("2. 튜플 vs 리스트 핵심 차이")

# 리스트 - 변경 가능
my_list = [1, 2, 3]
print(f"리스트 원본: {my_list}")
my_list[0] = 10
my_list.append(4)
print(f"리스트 변경 후: {my_list}")

# 튜플 - 변경 불가능
my_tuple = (1, 2, 3)
print(f"튜플 원본: {my_tuple}")
print("튜플은 변경 불가능! (immutable)")

# my_tuple[0] = 10  # ❌ 에러!
# my_tuple.append(4)  # ❌ 에러!

print("\n" + "="*40)

# 3. 튜플 접근하기 (리스트와 동일)
print("3. 튜플 요소 접근하기")
fruits = ("사과", "바나나", "포도", "딸기")

print(f"첫 번째 과일: {fruits[0]}")
print(f"마지막 과일: {fruits[-1]}")
print(f"처음 2개: {fruits[:2]}")
print(f"마지막 2개: {fruits[-2:]}")

print("\n" + "="*40)

# 4. 튜플 언패킹 (중요!)
print("4. 튜플 언패킹 (매우 유용!)")

# 기본 언패킹
point = (10, 20)
x, y = point
print(f"좌표 {point} → x={x}, y={y}")

# 여러 개 한번에
student_info = ("김철수", 20, "컴퓨터공학")
name, age, major = student_info
print(f"이름: {name}, 나이: {age}, 전공: {major}")

# 변수 교환 (튜플의 강력한 기능!)
a = 10
b = 20
print(f"교환 전: a={a}, b={b}")

a, b = b, a  # 한 줄로 교환!
print(f"교환 후: a={a}, b={b}")

print("\n" + "="*40)

# 5. 튜플 메소드들 (적지만 유용)
print("5. 튜플 메소드들")
numbers = (1, 2, 3, 2, 2, 4, 5)
print(f"튜플: {numbers}")

print(f"길이: {len(numbers)}")
print(f"2의 개수: {numbers.count(2)}")
print(f"3의 위치: {numbers.index(3)}")
print(f"최댓값: {max(numbers)}")
print(f"최솟값: {min(numbers)}")
print(f"합계: {sum(numbers)}")

print("\n" + "="*40)

# 6. 튜플과 반복문
print("6. 튜플과 반복문")
subjects = ("수학", "영어", "과학", "국어")

print("방법 1: 요소 직접 사용")
for subject in subjects:
    print(f"- {subject}")

print("\n방법 2: enumerate 사용")
for index, subject in enumerate(subjects):
    print(f"{index+1}. {subject}")

print("\n" + "="*40)

# 7. 함수에서 튜플 활용
print("7. 함수에서 튜플 활용")

def get_name_age():
    """이름과 나이를 함께 반환"""
    return "진성", 25  # 튜플로 반환

def calculate_stats(numbers):
    """평균, 최대, 최소값을 튜플로 반환"""
    return sum(numbers)/len(numbers), max(numbers), min(numbers)

# 함수 사용
name, age = get_name_age()
print(f"반환값 받기: 이름={name}, 나이={age}")

scores = [85, 92, 78, 96, 88]
avg, maximum, minimum = calculate_stats(scores)
print(f"통계: 평균={avg:.1f}, 최대={maximum}, 최소={minimum}")

print("\n" + "="*40)

# 8. 튜플을 언제 사용할까?
print("8. 튜플 사용 시기")

print("✅ 좋은 튜플 사용 예시:")

# 좌표
position = (100, 200)
print(f"위치: {position}")

# RGB 색상
color = (255, 128, 0)
print(f"주황색 RGB: {color}")

# 날짜
date = (2024, 8, 4)
print(f"날짜: {date}")

# 설정값들 (변경되면 안 되는 것들)
config = ("localhost", 8080, "utf-8")
host, port, encoding = config
print(f"서버 설정: {host}:{port}, {encoding}")

print("\n❌ 리스트가 더 나은 경우:")
print("- 요소를 추가/제거해야 할 때")
print("- 요소를 정렬해야 할 때") 
print("- 요소를 자주 수정해야 할 때")

print("\n" + "="*40)

# 9. 실전 예제: 학생 정보 관리
print("9. 실전 예제: 학생 정보 관리")

# 학생 정보를 튜플로 저장 (변경되지 않는 기본 정보)
students = [
    ("김철수", 20, "컴퓨터공학", "서울"),
    ("이영희", 19, "수학", "부산"),
    ("박민수", 21, "물리학", "대구"),
    ("최지영", 20, "화학", "광주")
]

print("학생 명단:")
for student in students:
    name, age, major, city = student  # 언패킹
    print(f"- {name} ({age}세, {major}, {city})")

# 특정 조건 찾기
print("\n20세 학생들:")
for name, age, major, city in students:
    if age == 20:
        print(f"- {name} ({major})")

print("\n" + "="*40)

# 10. 튜플과 딕셔너리 조합
print("10. 튜플과 딕셔너리 조합")

# 딕셔너리의 items()는 튜플을 반환
scores = {"수학": 85, "영어": 92, "과학": 78}

print("과목별 점수:")
for subject, score in scores.items():  # (key, value) 튜플로 반환
    print(f"{subject}: {score}점")

# 여러 딕셔너리를 튜플로 묶기
student1 = {"name": "철수", "score": 85}
student2 = {"name": "영희", "score": 92}
all_students = (student1, student2)  # 튜플로 묶기

print(f"\n모든 학생: {all_students}")

print("\n" + "="*40)
print("✅ 튜플 완전 정복!")
print("🎯 핵심: 변경 불가능한 순서가 있는 데이터!")