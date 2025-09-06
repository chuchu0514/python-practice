#연습1

while True:
    try:
        name, age, hobby = input("이름과 나이 취미를 입력하세요(공백으로 구분):").split()
        break
    except ValueError as e:
        print(f"❌ 입력 에러: {e}")

try:
    with open('introduce_myself.txt', 'w', encoding='utf-8') as file:
        lines = [
            f"안녕하세요 제 이름은 {name}이고 나이는{age}, 취미는{hobby}예요.\n",
            "잘 부탁드립니다.\n"
        ]
        file.writelines(lines)
except FileNotFoundError as e:
    print(f"파일 없음 에러: {e}")


#연습2
try:
    with open('introduce_myself.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("📄 저장된 자기소개:")
        print(content)
except FileNotFoundError:
    print("❌ 파일을 찾을 수 없어요! 먼저 자기소개를 저장해주세요.")
except Exception as e:
    print(f"❌ 파일 읽기 에러: {e}")