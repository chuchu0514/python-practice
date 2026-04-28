from module import game_utils

def play_flipcoin_game():
    while True:
        result = game_utils.flip_coin()  # 결과 받기
        print(f"🪙 결과: {result}")      # 결과 출력 추가!
        while True:
            answer = input("다시 던지시겠습니까?:(y/n)")
            if answer == 'y':
                break
            elif answer == 'n':
                return
            else: 
                print("y와 n 중 하나를 입력해주십시오.")

def validate_input(user_input, difficult = 3):
    """간단하게 통합"""
    if len(user_input) == difficult and user_input.isdigit() and len(set(user_input)) == difficult and user_input[0] != '0':
        return True
    else: 
        return False
    
def number_choice_baseball(difficult = 3):
   while True:
        if difficult == 3:
            return game_utils.generate_baseball_numbers()
        elif difficult == 4:
            return game_utils.generate_4digit_numbers()
        else:
            print("3 또는 4를 입력하세요.")

def calculate_strike_ball(computer, user, difficult = 3): 
    """간단하게 통합"""
    ball_count = 0
    strike_count = 0

    for i in range(difficult):
        for j in range(difficult):
            if i == j and computer[i] == user[j]:
                strike_count += 1
            elif i != j and computer[i] == user[j]:
                ball_count += 1

    return strike_count, ball_count

def play_baseball_game():
    while True: 
        while True:
            try:
                difficult = int(input("난이도를 입력하세요 3자리, 4자리(숫자만 입력하세요):"))
                if difficult in [3, 4]:
                    break
                else:
                    print("3 또는 4만 입력하세요.")
            except ValueError:
                print("숫자만 입력하세요.")
          
        print("=== 숫자야구 게임 === 기록을 보고 싶다면 'h' 입력.")
                
        # 컴퓨터 숫자 생성 (이미 완성된 함수 사용)
        computer_numbers = number_choice_baseball(difficult)
        game_over = False
        attempt_count = 0  
        record = []
        while not game_over:
            
            user_input = input(f"{difficult}자리 숫자(0~9)를 입력하세요(첫 자리 0x, 중복불가): ")
            print(f"입력: {user_input}")
            

            if user_input == 'h':
                if not record == []:
                    for entry in record:
                        print(f"시도 {entry[0]}: {entry[1]} -> {entry[2]}S {entry[3]}B")
                else:
                    print("기록이 없습니다.")

            elif validate_input(user_input, difficult):
                attempt_count += 1  # ✅ 시도 횟수 증가
                
                # ✅ 함수 호출하고 결과 받기
                strike, ball = calculate_strike_ball(computer_numbers, user_input, difficult)
                record.append([attempt_count, user_input, strike, ball])
                if strike == difficult:  
                    print(f"축하드립니다! {attempt_count}번만에 정답을 맞췄습니다! 정답: {user_input}")
                    while True:
                        answer = input("재시작하겠습니까? (y/n)")
                        if answer == 'y':
                            game_over = True
                            break
                        elif answer == 'n':
                            return
                        else:
                            print("y와n 중 하나를 입력하세요.")

                    
                else:
                    # ✅ 결과 제대로 출력
                    print(f"시도 {attempt_count}: {strike}s {ball}b")
                    
            else:
                print("❌ 잘못된 입력입니다!")
                print(f"💡 중복 없는 {difficult}자리 숫자를 입력하세요 (첫 자리는 0 제외)")
        
def play_roll_dice():
    while True:
        print(f"주사위를 굴려서 나온 값은 {game_utils.roll_dice()}입니다.")
        answer = input("다시 던지시겠습니까? (y/n):")
        if answer == 'y':
            continue
        elif answer == 'n':
            break
        else:
            print("y와 n 중 하나를 입력해주십시오.")

def play_lotto():
    while True:
        print(f"생성된 로또 번호는 {game_utils.generate_lotto()}입니다.")
        answer = input("다시 뽑겠습니까? (y/n):")
        if answer == 'y':
            continue
        elif answer == 'n':
            break
        else:
            print("y와 n 중 하나를 입력해주십시오.")


def main():
    while True:
        print("🎮 === 게임 센터 ===")
        print("1. 동전 던지기")
        print("2. 숫자야구")
        print("3. 주사위 굴리기") 
        print("4. 로또번호") 
        print("5. 종료")
        
        choice = input("게임을 선택하세요: ")
        
        if choice == '1':
            play_flipcoin_game()
        elif choice == '2':
            play_baseball_game()  
        elif choice == '3':
            play_roll_dice()
        elif choice == '4':
            play_lotto()
        elif choice == '5':
            print("게임 센터를 종료합니다!")
            break
        else:
            print("올바른 번호를 선택하세요!")

if __name__ == "__main__":
    main()
    print("게임이 끝났습니다. 감사합니다!")