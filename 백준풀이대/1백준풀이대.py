# 🐛 디버깅 연습용 코드
# 이 코드에는 의도적으로 버그가 있습니다!

def calculate_average(numbers):
    """숫자 리스트의 평균을 계산"""
    total = 0
    count = 0
    average = 0
    for num in numbers:
        total += num
        count += 1
    
    # 🐛 버그: 0으로 나누기 가능성
    if count != 0:
        average = total / count
    return average

def find_max_student(students):
    """학생 중에서 가장 높은 점수를 가진 학생 찾기"""
    max_score = 0
    best_student = ""
    
    for name, score in students.items():
        # 🐛 버그: 음수 점수 처리 안됨
        if score > max_score:
            max_score = score
            best_student = name
    
    return best_student, max_score

def process_grades(grade_data):
    """성적 데이터 처리"""
    result = {}
    
    for subject, grades in grade_data.items():
        if len(grades) > 0:  # 빈 리스트가 아니면
            avg = calculate_average(grades)
            result[subject] = avg
        else:
            print(f"⚠️ {subject} 과목에 성적이 없습니다")
    return result

# 🧪 테스트 데이터
if __name__ == "__main__":
    # 테스트 1: 정상적인 경우
    normal_grades = [85, 92, 78, 96, 88]
    print(f"평균: {calculate_average(normal_grades)}")
    
    # 테스트 2: 빈 리스트 (버그 발생!)
    empty_grades = []
    print(f"빈 리스트 평균: {calculate_average(empty_grades)}")
    
    # 테스트 3: 학생 점수 비교
    students = {
        "진성": 95,
        "철수": 87,
        "민수": -10,  # 음수 점수!,
        "영희": 92,
        
    }
    best, score = find_max_student(students)
    print(f"최고 점수 학생: {best}, 점수: {score}")
    
    # 테스트 4: 복합 데이터 처리
    grade_data = {
        "수학": [85, 90, 78],
        "영어": [92, 88, 95],
        "과학": []  # 빈 리스트!
    }
    
    results = process_grades(grade_data)
    for subject, avg in results.items():
        print(f"{subject} 평균: {avg}")