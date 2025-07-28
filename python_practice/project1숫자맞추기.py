import random

best_score = None

while True:
    random_num = random.randint(1, 100)
    count = 0
    while True:
        user_input = int(input("1~100까지의 수를 하나 입력하시오:"))
        if 1 <= user_input <= 100:
            if random_num == user_input:
                count += 1
                if best_score is None or count < best_score:
                    best_score = count
                print(f"축하 드립니다. 정답을 {count}번 만에 맞췄습니다! 최고기록은 {best_score}번 입니다!") 
                while True:
                    user_choice = input("다시 하겠습니까? (y/n):")
                    if user_choice == "y":
                        break
                    elif user_choice == "n":
                        print("게임을 종료합니다.")
                        exit()
                    else: print("다시 입력해주세요.")    
                break
                
            elif random_num > user_input:
                print("입력한 수가 정답보다 더 작습니다.")
                count += 1
            else: 
                print("입력한 수가 정답보다 더 큽니다.")    
                count += 1
        else: print("잘못 입력하셨습니다.")


