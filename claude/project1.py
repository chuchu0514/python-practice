# 학생 성적 관리 시스템

student_info = {} # 학생 정보 딕셔너리


while True :
    print("\n=== 학생 성적 관리 시스템 ===") 
    i = int(input("1. 학생 추가 2. 학생 삭제 3. 성적 입력 4. 성적 조회 5. 성적 수정 6. 학생 목록 7. 종료\n숫자를 입력하세요:"))
    if i == 1 :
        name = input("추가할 학생 이름을 입력하세요:")
        if name in student_info:
            print("이미 등록된 학생입니다!")
        else:
            student_info[name] = {}  # 빈 딕셔너리로 시작
            print(f"{name} 학생이 추가되었습니다!")
    elif i == 2 :
        name = input("삭제할 학생 이름을 입력하세요:")
        if name in student_info:
            del student_info[name]
            print(f"{name} 학생이 삭제되었습니다!")
        else:
            print("등록되지 않은 학생입니다!")
    elif i == 3 :
        name = input("성적을 입력할 학생 이름을 입력하세요:")
        if name in student_info:
            grade = int(input("성적을 입력하세요 (0~100):"))
            student_info[name]["grade"] = grade
            if grade < 0 or grade > 100:
                print("잘못된 성적입니다. 0~100 사이의 숫자를 입력하세요.")
            else:
                print(f"{name} 학생의 성적이 입력되었습니다!")
        else:
            print("등록되지 않은 학생입니다!")
    elif i == 4 :
        name = input("조회할 학생 이름을 입력하세요:")
        if name in student_info:
            if "grade" in student_info[name]:
                if student_info[name]["grade"]>=90:
                    print(f"{name} 학생의 성적은 {student_info[name]['grade']}점 입니다! 학점은 A입니다!")
                elif student_info[name]["grade"]>=80:
                    print(f"{name} 학생의 성적은 {student_info[name]['grade']}점 입니다! 학점은 B입니다!")
                elif student_info[name]["grade"]>=70:
                    print(f"{name} 학생의 성적은 {student_info[name]['grade']}점 입니다! 학점은 C입니다!")
                else:
                    print(f"{name} 학생의 성적은 {student_info[name]['grade']}점 입니다! 학점은 F입니다!")
            else: 
                print("성적이 입력되지 않았습니다!")        
        else: 
            print("등록되지 않은 학생입니다!")
    elif i == 5 :
        name = input("수정할 학생의 이름을 입력하세요.:")
        if name in student_info:
            grade = int(input("수정할 성적을 입력하세요:"))
            student_info[name]["grade"] = grade
            print(f"{name} 학생의 성적이 수정되었습니다!")
        else:
            print("등록되지 않은 학생입니다!")
    elif i == 6 :
        print("현재 등록된 학생 목록:")
        for name in student_info:
            print(f"- {name}")
    elif i == 7 :
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 수를 입력하였습니다. 다시 입력해주세요.")
        

        
        
        

 