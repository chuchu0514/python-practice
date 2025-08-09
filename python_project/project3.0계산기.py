from module import math_utils

record = []

def show_menu():
    print("\n=== 계산기 ===")
    print("0. 종료")
    print("1. 덧셈")
    print("2. 뺄셈") 
    print("3. 곱셈")
    print("4. 나눗셈")
    print("5. 거듭제곱") 
    print("6. 저장기록")
    

def get_numbers():
    a = float(input("첫 번째 숫자: "))
    b = float(input("두 번째 숫자: "))
    return a, b

def main():
    """메인 프로그램"""
    while True:
        show_menu()
        choice = input("메뉴 선택: ")
        if choice == '0':
            exit()
        
        elif choice == '1':
            a, b = get_numbers()
            result = math_utils.add(a, b)
            print(f"결과: {a} + {b} = {result}")
            record.append([a, b, result]) 
        
        elif choice == '2':
            a, b = get_numbers()
            result = math_utils.subtract(a, b)
            print(f"결과: {a} - {b} = {result}")
            record.append([a, b, result])

        
        elif choice == '3':
            a, b = get_numbers()
            result = math_utils.multiply(a, b)
            print(f"결과: {a} * {b} = {result:.5f}")
            record.append([a, b, result])


        elif choice == '4':
            a, b = get_numbers()
            if b == 0:
                print("0으론 나눌 수 없습니다.")
            else:
                result = math_utils.divide(a, b)
                print(f"결과: {a} / {b} = {result:.5f}")
                record.append([a, b, result])


        elif choice == '5':
            a, b = get_numbers()
            result = math_utils.power(a, b)
            print(f"결과: {a} ^ {b} = {result}")
            record.append([a, b, result])

        elif choice == '6':
            print("\n=== 계산 기록 ===")
            if len(record) == 0:
                print("계산 기록이 비어있습니다")
            else:
                for list in record:
                    print(list)


        else:
            print("잘못 입력하였습니다.")

    

if __name__ == "__main__":
    main()

