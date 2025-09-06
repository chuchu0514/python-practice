# python# 기존: 텍스트로 저장
# "[2024-08-04 15:30] 성적: 85점"

# # 새로운: JSON으로 구조화 저장
# {
#     "timestamp": "2024-08-04 15:30:00",
#     "score": 85,
#     "subject": "수학",
#     "student": "진성"
# }
# 미션:

# 성적 데이터를 딕셔너리로 구성
# JSON 파일로 저장
# JSON 파일에서 불러와서 예쁘게 출력

import datetime
import json

def time_record():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     

def show_menu():
    print("\n=== 성적 누적 관리 ===")
    print("1. 성적 추가")
    print("2. 성적 목록 보기") 
    print("3. 종료")
    choice = input("선택: ")
    return choice


def main():

    try:
        with open('scores.json', 'r', encoding='utf-8') as file:
            record = json.load(file)  # 기존 딕셔너리 로드
    except FileNotFoundError:
        record = {}  # 파일 없으면 빈 딕셔너리
    except json.JSONDecodeError:
        record = {}  # JSON 오류시 빈 딕셔너리

    while True:
        choice = show_menu()
        if choice == '1':
            while True:
                try:            
                    score = int(input("성적을 입력하세요(0~100): "))            
                    if 0 <= score <= 100:
                        break
                    else:
                        print("❌ 0-100 사이의 점수를 입력하세요!")
                except ValueError as e:
                    print(f"잘못된 입력 값입니다 오류{e}")
            
            subject = input("과목을 입력하세요: ")
            name = input("이름을 입력하세요: ")            
            current_time = time_record()

            record[name] = {
                "timestamp" : current_time,
                "score" : score,
                "subject" : subject,
                "student" : name
            } 
            try:
                with open('scores.json', 'w', encoding='utf-8') as file:
                    json.dump(record, file, ensure_ascii=False, indent=2)
                    print("✅ 성적이 저장되었습니다!")
            except Exception as e:
                print(f"❌ 저장 실패: {e}")

        elif choice == '2':
            try:
                with open('scores.json', 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    if not data:
                        print("📋 저장된 성적이 없습니다.")
                    else:
                        print("\n📊 === 성적 목록 ===")
                        for student_name, score_info in data.items():
                            print(f"👤 {student_name}: {score_info['subject']} {score_info['score']}점")
                            print(f"   📅 {score_info['timestamp']}")
                            print("-" * 30)
            except FileNotFoundError:
                print("파일이 존재하지 않습니다.")
            except json.JSONDecodeError:
                print("❌ JSON 파일이 손상되었습니다.")
        elif choice == '3':
            break
        else: 
            print("잘못된 값을 입력하였습니다.")


if __name__ == "__main__":
    main()
    print("종료합니다.")