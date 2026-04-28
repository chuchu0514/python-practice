# 🚨 에러가 발생하는 상황들

print("=== 문제 상황 1: 존재하지 않는 파일 읽기 ===")

# 이 코드를 실행하면 FileNotFoundError 발생!
try:
    with open('존재하지않는파일.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("❌ 파일을 찾을 수 없습니다!")

print("\n" + "="*40)

print("=== 문제 상황 2: 입력 개수가 맞지 않을 때 ===")

# 사용자가 "추진성 25"만 입력하면? (취미 누락)
print("이름, 나이만 입력해보세요 (취미 빼고):")
try:
    user_input = input("입력: ").split()
    if len(user_input) != 3:
        print(f"❌ 3개를 입력해야 하는데 {len(user_input)}개만 입력했어요!")
    else:
        name, age, hobby = user_input
        print(f"✅ 이름: {name}, 나이: {age}, 취미: {hobby}")
except ValueError as e:
    print(f"❌ 입력 에러: {e}")

print("\n" + "="*40)

print("=== 해결책: try-except 사용! ===")
print("예외처리를 사용하면 프로그램이 죽지 않아요!")