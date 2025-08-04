#연습1

name, age, hobby = input("입력하세요: ").split()

with open('introduce_myself.txt', 'w', encoding='utf-8') as file:
    lines = [
        f"안녕하세요 제 이름은 {name}이고 나이는{age}, 취미는{hobby}예요.\n",
        "잘 부탁드립니다.\n"
    ]
    file.writelines(lines)

#연습2
file = open('introduce_myself.txt', 'r', encoding='utf-8')
content = file.read()
print(content)
file.close()