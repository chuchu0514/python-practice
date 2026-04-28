# 📚 Phase 2-3: 딕셔너리(Dictionary) 완전 가이드

print("=== 📚 딕셔너리(Dictionary) 완전 가이드 ===")

# 1. 딕셔너리 만들기
print("1. 딕셔너리 만들기")
student = {"name": "김철수", "age": 20, "major": "컴퓨터공학"}
scores = {"수학": 85, "영어": 92, "과학": 78}
mixed = {"숫자": 123, "리스트": [1, 2, 3], "불린": True}
empty_dict = {}

print(f"학생 정보: {student}")
print(f"점수: {scores}")
print(f"섞인 딕셔너리: {mixed}")
print(f"빈 딕셔너리: {empty_dict}")

print("\n💡 딕셔너리 = key: value 쌍으로 구성!")

print("\n" + "="*40)

# 2. 딕셔너리 접근하기
print("2. 딕셔너리 값 접근하기")
person = {"이름": "진성", "나이": 25, "직업": "학생", "취미": "코딩"}

# 방법 1: 대괄호 사용
print(f"이름: {person['이름']}")
print(f"나이: {person['나이']}")

# 방법 2: get() 메소드 (안전함)
print(f"직업: {person.get('직업')}")
print(f"주소: {person.get('주소', '정보 없음')}")  # 기본값 설정

# 차이점 보기
print("\n대괄호 vs get() 차이:")
try:
    print(person['주소'])  # 키가 없으면 에러!
except KeyError:
    print("❌ KeyError 발생!")

print(f"get으로: {person.get('주소', '없음')}")  # 에러 안 남

print("\n" + "="*40)

# 3. 딕셔너리 수정하기
print("3. 딕셔너리 수정하기")
inventory = {"사과": 10, "바나나": 5, "포도": 8}
print(f"초기 재고: {inventory}")

# 값 수정
inventory["사과"] = 15
print(f"사과 수정 후: {inventory}")

# 새 항목 추가
inventory["딸기"] = 12
print(f"딸기 추가 후: {inventory}")

# update로 여러 개 한번에
inventory.update({"오렌지": 7, "키위": 3})
print(f"여러 개 추가: {inventory}")

print("\n" + "="*40)

# 4. 딕셔너리 삭제하기
print("4. 딕셔너리 요소 삭제하기")
menu = {"햄버거": 5000, "피자": 8000, "치킨": 12000, "콜라": 1500}
print(f"초기 메뉴: {menu}")

# del로 삭제
del menu["콜라"]
print(f"콜라 삭제 후: {menu}")

# pop으로 삭제 (값 반환)
removed_price = menu.pop("피자")
print(f"피자 삭제 후: {menu}")
print(f"삭제된 피자 가격: {removed_price}")

# popitem으로 마지막 항목 삭제
removed_item = menu.popitem()
print(f"마지막 항목 삭제: {menu}")
print(f"삭제된 항목: {removed_item}")

print("\n" + "="*40)

# 5. 딕셔너리 유용한 메소드들
print("5. 딕셔너리 유용한 메소드들")
grades = {"철수": 85, "영희": 92, "민수": 78, "지영": 96}
print(f"성적표: {grades}")

# keys() - 모든 키
print(f"학생들: {list(grades.keys())}")

# values() - 모든 값
print(f"점수들: {list(grades.values())}")

# items() - 키-값 쌍
print(f"키-값 쌍: {list(grades.items())}")

# 길이
print(f"학생 수: {len(grades)}")

# 키 존재 확인
print(f"철수 있나? {'철수' in grades}")
print(f"미영 있나? {'미영' in grades}")

print("\n" + "="*40)

# 6. 딕셔너리와 반복문
print("6. 딕셔너리와 반복문")
scores = {"수학": 85, "영어": 92, "과학": 78, "국어": 88}

print("방법 1: 키만 반복")
for subject in scores:
    print(f"{subject}: {scores[subject]}점")

print("\n방법 2: keys() 사용")
for subject in scores.keys():
    print(f"{subject} 과목")

print("\n방법 3: values() 사용")
for score in scores.values():
    print(f"{score}점")

print("\n방법 4: items() 사용 (가장 많이 사용!)")
for subject, score in scores.items():
    print(f"{subject}: {score}점")

print("\n" + "="*40)

# 7. 중첩 딕셔너리
print("7. 중첩 딕셔너리 (딕셔너리 안에 딕셔너리)")
students = {
    "김철수": {
        "나이": 20,
        "전공": "컴퓨터공학",
        "성적": {"수학": 85, "영어": 90}
    },
    "이영희": {
        "나이": 19,
        "전공": "수학",
        "성적": {"수학": 95, "영어": 88}
    }
}

print("학생 정보:")
for name, info in students.items():
    print(f"\n{name}:")
    print(f"  나이: {info['나이']}세")
    print(f"  전공: {info['전공']}")
    print("  성적:")
    for subject, score in info['성적'].items():
        print(f"    {subject}: {score}점")

print("\n" + "="*40)

# 8. 딕셔너리 컴프리헨션
print("8. 딕셔너리 컴프리헨션")

# 기본 형태
numbers = [1, 2, 3, 4, 5]
squares = {x: x**2 for x in numbers}
print(f"제곱 딕셔너리: {squares}")

# 조건 추가
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(f"짝수 제곱: {even_squares}")

# 문자열에서 길이 계산
words = ["python", "java", "javascript", "go"]
word_lengths = {word: len(word) for word in words}
print(f"단어 길이: {word_lengths}")

print("\n" + "="*40)

# 9. 실전 예제 1: 투표 집계
print("9. 실전 예제 1: 투표 집계")
votes = ["사과", "바나나", "사과", "포도", "바나나", "사과", "딸기"]

# 투표 집계
vote_count = {}
for vote in votes:
    if vote in vote_count:
        vote_count[vote] += 1
    else:
        vote_count[vote] = 1

print("투표 결과:")
for fruit, count in vote_count.items():
    print(f"{fruit}: {count}표")

# 더 간단한 방법 (get 사용)
vote_count2 = {}
for vote in votes:
    vote_count2[vote] = vote_count2.get(vote, 0) + 1

print(f"\nget 사용한 결과: {vote_count2}")

print("\n" + "="*40)

# 10. 실전 예제 2: 학생 성적 관리 시스템
print("10. 실전 예제 2: 학생 성적 관리 시스템")

# 학생 데이터베이스
student_db = {}

def add_student(name, subjects_scores):
    """학생 추가"""
    student_db[name] = subjects_scores

def get_average(name):
    """평균 계산"""
    if name in student_db:
        scores = student_db[name].values()
        return sum(scores) / len(scores)
    return None

def get_top_student():
    """최고 평균 학생 찾기"""
    best_student = None
    best_average = 0
    
    for name in student_db:
        avg = get_average(name)
        if avg > best_average:
            best_average = avg
            best_student = name
    
    return best_student, best_average

# 학생 데이터 추가
add_student("김철수", {"수학": 85, "영어": 90, "과학": 88})
add_student("이영희", {"수학": 95, "영어": 88, "과학": 92})
add_student("박민수", {"수학": 78, "영어": 85, "과학": 80})

# 결과 출력
print("학생별 평균:")
for name in student_db:
    avg = get_average(name)
    print(f"{name}: {avg:.1f}점")

top_name, top_avg = get_top_student()
print(f"\n최고 학생: {top_name} ({top_avg:.1f}점)")

print("\n" + "="*40)

# 11. 딕셔너리 활용 팁
print("11. 딕셔너리 활용 팁")

print("✅ 딕셔너리를 언제 사용할까?")
print("- 키-값 쌍으로 데이터를 저장할 때")
print("- 빠른 검색이 필요할 때")
print("- 데이터의 의미가 중요할 때")
print("- 설정값이나 옵션을 저장할 때")

print("\n🎯 실제 사용 예시:")
# 설정 파일
config = {
    "server_host": "localhost",
    "server_port": 8080,
    "debug_mode": True,
    "max_connections": 100
}

# 번역기
translations = {
    "hello": "안녕하세요",
    "goodbye": "안녕히 가세요", 
    "thank you": "감사합니다"
}

# 상품 정보
product = {
    "name": "노트북",
    "price": 1200000,
    "brand": "삼성",
    "specs": {"CPU": "Intel i7", "RAM": "16GB", "Storage": "512GB SSD"}
}

print(f"설정: {config}")
print(f"번역: {translations}")
print(f"상품: {product}")

print("\n" + "="*40)
print("✅ 딕셔너리 완전 정복!")
print("🎯 핵심: 키로 빠르게 찾는")