# 🎯 Phase 2 총정리: 자료구조 비교 및 선택 가이드

print("=== 🎯 Phase 2 자료구조 총정리 ===")

# 1. 자료구조 한눈에 비교
print("1. 자료구조 특징 비교표")
print("="*60)
print("구조      | 순서 | 중복 | 변경가능 | 인덱싱 | 주요 특징")
print("="*60)
print("리스트    | ✅   | ✅   | ✅      | ✅     | 가장 범용적")
print("튜플      | ✅   | ✅   | ❌      | ✅     | 변경 불가능")
print("딕셔너리  | ❌   | ❌   | ✅      | ❌     | 키-값 쌍")
print("집합      | ❌   | ❌   | ✅      | ❌     | 중복 제거, 빠른 검색")
print("="*60)

print("\n" + "="*50)

# 2. 언제 어떤 자료구조를 쓸까?
print("2. 상황별 자료구조 선택 가이드")

situations = [
    {
        "상황": "학생들의 점수를 순서대로 저장",
        "추천": "리스트",
        "이유": "순서가 중요하고 중복 점수 가능",
        "예시": "[85, 92, 78, 85, 96]"
    },
    {
        "상황": "좌표나 RGB 색상값 저장", 
        "추천": "튜플",
        "이유": "변경되지 않는 고정값",
        "예시": "(255, 128, 0) # 주황색"
    },
    {
        "상황": "학생 이름으로 점수 찾기",
        "추천": "딕셔너리", 
        "이유": "키로 빠른 검색 필요",
        "예시": "{'철수': 85, '영희': 92}"
    },
    {
        "상황": "중복 제거된 고유한 태그들",
        "추천": "집합",
        "이유": "중복 자동 제거, 집합 연산",
        "예시": "{'python', 'coding', 'tutorial'}"
    }
]

for i, situation in enumerate(situations, 1):
    print(f"\n📌 상황 {i}: {situation['상황']}")
    print(f"   추천: {situation['추천']}")
    print(f"   이유: {situation['이유']}")
    print(f"   예시: {situation['예시']}")

print("\n" + "="*50)

# 3. 실전 종합 예제: 학급 관리 시스템 
print("3. 실전 종합 예제: 학급 관리 시스템")

# 모든 자료구조를 활용한 종합 시스템
class ClassRoom:
    def __init__(self, class_name):
        self.class_name = class_name
        # 리스트: 순서가 있는 학생 명단
        self.student_list = []
        # 딕셔너리: 학생별 상세 정보
        self.student_info = {}
        # 집합: 고유한 과목들
        self.subjects = set()
        # 튜플: 변경되지 않는 학급 정보
        self.class_info = (class_name, "2024년", "1학기")
    
    def add_student(self, name, age, subjects_scores):
        """학생 추가"""
        # 리스트에 순서대로 추가
        if name not in self.student_list:
            self.student_list.append(name)
        
        # 딕셔너리에 상세 정보 저장
        self.student_info[name] = {
            "age": age,
            "scores": subjects_scores,
            "average": sum(subjects_scores.values()) / len(subjects_scores)
        }
        
        # 집합에 과목들 추가 (중복 자동 제거)
        self.subjects.update(subjects_scores.keys())
    
    def get_class_summary(self):
        """학급 요약 정보"""
        print(f"\n📚 {self.class_info[0]} ({self.class_info[1]} {self.class_info[2]})")
        print(f"👥 총 학생 수: {len(self.student_list)}")
        print(f"📖 수업 과목: {', '.join(self.subjects)}")
        
        # 전체 평균 계산
        all_averages = [info["average"] for info in self.student_info.values()]
        class_average = sum(all_averages) / len(all_averages)
        print(f"📊 학급 평균: {class_average:.1f}점")

# 학급 생성 및 데이터 입력
my_class = ClassRoom("컴퓨터공학과 1반")

# 학생들 추가
students_data = [
    ("김철수", 20, {"수학": 85, "영어": 90, "과학": 88}),
    ("이영희", 19, {"수학": 95, "영어": 88, "과학": 92}),
    ("박민수", 21, {"수학": 78, "영어": 85, "과학": 80, "체육": 95}),
    ("최지영", 20, {"수학": 92, "영어": 94, "과학": 89})
]

for name, age, scores in students_data:
    my_class.add_student(name, age, scores)

# 결과 확인
my_class.get_class_summary()

print("\n👥 학생 명단 (리스트 - 순서 유지):")
for i, student in enumerate(my_class.student_list, 1):
    print(f"  {i}. {student}")

print("\n📋 학생별 상세 정보 (딕셔너리 - 빠른 검색):")
for name, info in my_class.student_info.items():
    print(f"  {name}: 평균 {info['average']:.1f}점")

print(f"\n📚 전체 과목 (집합 - 중복 제거): {my_class.subjects}")

print(f"\n🏫 학급 기본 정보 (튜플 - 변경 불가): {my_class.class_info}")

print("\n" + "="*50)

# 4. 변환 방법들
print("4. 자료구조 간 변환 방법")

# 기본 데이터
sample_list = [1, 2, 3, 2, 4, 3, 5]
print(f"원본 리스트: {sample_list}")

# 리스트 → 다른 자료구조
list_to_tuple = tuple(sample_list)
list_to_set = set(sample_list)  # 중복 제거됨
list_to_dict = {i: val for i, val in enumerate(sample_list)}

print(f"→ 튜플로: {list_to_tuple}")
print(f"→ 집합으로: {list_to_set}")
print(f"→ 딕셔너리로: {list_to_dict}")

# 다시 리스트로
set_to_list = list(list_to_set)
tuple_to_list = list(list_to_tuple)
dict_keys_to_list = list(list_to_dict.keys())
dict_values_to_list = list(list_to_dict.values())

print(f"\n집합 → 리스트: {set_to_list}")
print(f"튜플 → 리스트: {tuple_to_list}")
print(f"딕셔너리 키 → 리스트: {dict_keys_to_list}")
print(f"딕셔너리 값 → 리스트: {dict_values_to_list}")

print("\n" + "="*50)

# 5. 성능 비교 요약
print("5. 성능 특성 요약")

performance_guide = {
    "검색 속도": {
        "빠름": ["딕셔너리 (키)", "집합"],
        "보통": ["리스트 (작은 크기)", "튜플 (작은 크기)"], 
        "느림": ["리스트 (큰 크기)"]
    },
    "메모리 사용": {
        "적음": ["튜플", "집합"],
        "보통": ["리스트", "딕셔너리"]
    },
    "삽입/삭제": {
        "빠름": ["리스트 (맨 끝)", "집합", "딕셔너리"],
        "느림": ["리스트 (중간)", "튜플 (불가능)"]
    }
}

for category, speeds in performance_guide.items():
    print(f"\n🚀 {category}:")
    for speed_level, structures in speeds.items():
        print(f"  {speed_level}: {', '.join(structures)}")

print("\n" + "="*50)

# 6. 자주 하는 실수들
print("6. 자주 하는 실수와 해결법")

mistakes = [
    {
        "실수": "빈 집합을 {}로 만들기",
        "문제": "{}는 빈 딕셔너리가 됨",
        "해결": "set()을 사용하기"
    },
    {
        "실수": "튜플에 요소 하나만 넣을 때 쉼표 안 쓰기",
        "문제": "(42)는 그냥 괄호, 튜플이 아님",
        "해결": "(42,)처럼 쉼표 반드시 쓰기"
    },
    {
        "실수": "딕셔너리에서 없는 키 접근",
        "문제": "KeyError 발생",
        "해결": "get() 메소드 사용하기"
    },
    {
        "실수": "집합이나 딕셔너리에 인덱싱 시도",
        "문제": "순서가 없어서 불가능",
        "해결": "반복문이나 키/값으로 접근"
    }
]

for i, mistake in enumerate(mistakes, 1):
    print(f"\n❌ 실수 {i}: {mistake['실수']}")
    print(f"   문제: {mistake['문제']}")
    print(f"   ✅ 해결: {mistake['해결']}")

print("\n" + "="*50)

# 7. 마무리
print("7. Phase 2 완주 축하! 🎉")

print("\n🏆 마스터한 내용:")
print("✅ 리스트: 순서가 있는 변경 가능한 데이터")
print("✅ 튜플: 순서가 있는 변경 불가능한 데이터") 
print("✅ 딕셔너리: 키-값 쌍의 빠른 검색 구조")
print("✅ 집합: 중복 없는 고유 요소들의 집합 연산")

print("\n🚀 다음 Phase에서는:")
print("📝 객체지향 프로그래밍 (클래스, 상속)")
print("🔧 함수 심화 (람다, 데코레이터)")
print("📦 모듈과 패키지 만들기")

print("어떤 상황에서든 적절한 자료구조를 선택할 수 있어요!")