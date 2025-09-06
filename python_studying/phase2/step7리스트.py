# 리스트
# 문제1
my_list=[10,20,30,40,50]

print(my_list[2])

# 문제2
fruits= []

fruits.append("apple")
fruits.append("banana")
fruits.append("orange")

# 문제3
grades = [85,92,78,96,88]
grades.append(95)
grades.remove(85)
print(grades)


# 📋 Phase 2-1: 리스트(List) 완전 가이드

print("=== 📋 리스트(List) 완전 가이드 ===")

# 1. 리스트 만들기
print("1. 리스트 만들기")
numbers = [1, 2, 3, 4, 5]
fruits = ["사과", "바나나", "포도"]
mixed = [1, "안녕", 3.14, True]
empty_list = []

print(f"숫자 리스트: {numbers}")
print(f"과일 리스트: {fruits}")
print(f"섞인 리스트: {mixed}")
print(f"빈 리스트: {empty_list}")

print("\n" + "="*40)

# 2. 리스트 접근하기 (인덱싱)
print("2. 리스트 요소 접근하기")
colors = ["빨강", "파랑", "노랑", "초록"]

print(f"첫 번째 색깔: {colors[0]}")
print(f"두 번째 색깔: {colors[1]}")
print(f"마지막 색깔: {colors[-1]}")
print(f"뒤에서 두 번째: {colors[-2]}")

print("\n" + "="*40)

# 3. 리스트 슬라이싱
print("3. 리스트 슬라이싱")
scores = [85, 92, 78, 96, 88, 91, 83]

print(f"전체 점수: {scores}")
print(f"처음 3개: {scores[:3]}")
print(f"2번째부터 5번째까지: {scores[1:5]}")
print(f"마지막 2개: {scores[-2:]}")
print(f"전체 복사: {scores[:]}")

print("\n" + "="*40)

# 4. 리스트 요소 추가하기
print("4. 리스트 요소 추가하기")
animals = ["고양이", "강아지"]
print(f"초기 동물: {animals}")

# append - 맨 뒤에 추가
animals.append("햄스터")
print(f"append 후: {animals}")

# insert - 특정 위치에 추가
animals.insert(1, "토끼")
print(f"insert 후: {animals}")

# extend - 여러 개 추가
animals.extend(["금붕어", "앵무새"])
print(f"extend 후: {animals}")

print("\n" + "="*40)

# 5. 리스트 요소 제거하기
print("5. 리스트 요소 제거하기")
numbers = [10, 20, 30, 40, 50]
print(f"초기 숫자: {numbers}")

# remove - 값으로 제거
numbers.remove(30)
print(f"30 제거 후: {numbers}")

# pop - 인덱스로 제거 (기본값: 마지막)
removed = numbers.pop()
print(f"마지막 제거 후: {numbers}, 제거된 값: {removed}")

removed = numbers.pop(0)
print(f"첫 번째 제거 후: {numbers}, 제거된 값: {removed}")

# del - 인덱스로 제거
del numbers[0]
print(f"del로 제거 후: {numbers}")

print("\n" + "="*40)

# 6. 리스트 수정하기
print("6. 리스트 수정하기")
grades = [85, 90, 78, 92]
print(f"원래 성적: {grades}")

grades[2] = 88  # 인덱스 2번을 88로 변경
print(f"수정된 성적: {grades}")

grades[1:3] = [95, 85]  # 여러 개 한번에 수정
print(f"여러 개 수정: {grades}")

print("\n" + "="*40)

# 7. 리스트 유용한 메소드들
print("7. 리스트 유용한 메소드들")
data = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"원본 데이터: {data}")

print(f"길이: {len(data)}")
print(f"최댓값: {max(data)}")
print(f"최솟값: {min(data)}")
print(f"합계: {sum(data)}")

# 정렬
sorted_data = sorted(data)  # 원본 그대로, 새로운 리스트 반환
print(f"정렬된 복사본: {sorted_data}")
print(f"원본 유지: {data}")

data.sort()  # 원본 자체를 정렬
print(f"원본을 정렬: {data}")

# 뒤집기
data.reverse()
print(f"뒤집기: {data}")

# 개수 세기
numbers = [1, 2, 3, 2, 2, 4, 5]
print(f"리스트: {numbers}")
print(f"2의 개수: {numbers.count(2)}")

# 찾기
print(f"3의 위치: {numbers.index(3)}")

print("\n" + "="*40)

# 8. 리스트 반복문
print("8. 리스트와 반복문")
subjects = ["수학", "영어", "과학", "국어"]

print("방법 1: 요소 직접 사용")
for subject in subjects:
    print(f"- {subject}")

print("\n방법 2: 인덱스 사용")
for i in range(len(subjects)):
    print(f"{i+1}. {subjects[i]}")

print("\n방법 3: enumerate 사용")
for index, subject in enumerate(subjects):
    print(f"{index+1}번째: {subject}")

print("\n" + "="*40)

# 9. 리스트 컴프리헨션 (간단한 것만)
print("9. 리스트 컴프리헨션")

# 기본 형태
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print(f"원본: {numbers}")
print(f"제곱: {squares}")

# 조건 추가
even_squares = [x * x for x in numbers if x % 2 == 0]
print(f"짝수의 제곱: {even_squares}")

print("\n" + "="*40)

# 10. 실전 예제
print("10. 실전 예제: 학생 성적 관리")

students = ["김철수", "이영희", "박민수", "최지영"]
scores = [85, 92, 78, 96]

# 성적과 함께 출력
print("학생별 성적:")
for i in range(len(students)):
    print(f"{students[i]}: {scores[i]}점")

# 평균 계산
average = sum(scores) / len(scores)
print(f"\n평균 점수: {average:.1f}점")

# 90점 이상 학생 찾기
high_scorers = []
for i in range(len(students)):
    if scores[i] >= 90:
        high_scorers.append(students[i])

print(f"90점 이상 학생: {high_scorers}")

print("\n" + "="*40)
print("✅ 리스트 완전 정복!")