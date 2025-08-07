
def find_max_student(students):
    max_score = 0  # ← 여기 클릭 (빨간 점)
    best_student = ""
    
    for name, score in students.items():  # ← 여기 클릭
        if score > max_score:  # ← 여기 클릭  
            max_score = score  # ← 여기도 클릭!
            best_student = name
    
    return best_student, max_score  # ← 여기도 클릭


# 모든 점수가 음수인 경우
students = {
    "철수": -10,
    "영희": -5,   # 이게 제일 높음!
    "민수": -20
}

best, score = find_max_student(students)
print(f"결과: '{best}', {score}")  # 결과: '', 0 ← 이상함!
