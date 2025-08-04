# === 성적 누적 관리 ===
# 1. 성적 추가
# 2. 성적 목록 보기
# 3. 종료

# - 성적을 입력받아서 'scores.txt'에 누적 저장
# - 날짜와 시간도 함께 기록
# - 잘못된 입력에 대한 예외처리
# - 파일이 없어도 안전하게 동작

import datetime

def time_record():
    
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return time

def show_menu():
    print("\n=== 성적 누적 관리 ===")
    print("1. 성적 추가")
    print("2. 성적 목록 보기") 
    print("3. 종료")
    choice = input("선택: ")
    return choice



while True:
    choice = show_menu()
    if choice == '1':
        while True:
            try:            
                grade = int(input("성적을 입력하세요: "))            
                if 0 <= grade <= 100:
                    break
                else:
                    print("❌ 0-100 사이의 점수를 입력하세요!")
            except ValueError as e:
                print(f"잘못된 입력 값입니다 오류{e}")    
        current_time = time_record()
      
        with open('scores.txt', 'a', encoding='utf-8') as file:
            file.write(f"{current_time} - 성적: {grade}\n")

    elif choice == '2':
        try:
            with open('scores.txt', 'r', encoding='utf-8') as file:
                content = file.read()
                print(content)

        except FileNotFoundError as e:
            print(f"파일이 존재하지 않습니다 오류: {e}")
    elif choice == '3':
        print("종료합니다.")
        break
    else: 
        print("잘못된 값을 입력하였습니다.")



