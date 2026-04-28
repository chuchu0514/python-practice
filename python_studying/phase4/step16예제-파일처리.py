# 📝 파일에 글 쓰기 - 기초

# 1. 가장 간단한 방법
print("=== 파일에 글 쓰기 ===")

# 파일을 만들고 글을 써보자!
file = open('my_first_file.txt', 'w', encoding='utf-8')
file.write("안녕하세요! 저는 진성입니다.")
file.write("\n파이썬으로 파일을 만들었어요!")
file.close()  # 꼭 닫아줘야 해요!

print("✅ my_first_file.txt 파일이 만들어졌어요!")
print("폴더를 확인해보세요!")                                                                                                                

# 2. 더 안전한 방법 (with 사용)
print("\n=== 더 안전한 방법 ===")

with open('safe_file.txt', 'w', encoding='utf-8') as file:
    file.write("이 방법이 더 안전해요!\n")
    file.write("자동으로 파일이 닫혀요.")

print("✅ safe_file.txt 파일도 만들어졌어요!")

# 3. 여러 줄 한번에 쓰기
with open('multiple_lines.txt', 'w', encoding='utf-8') as file:
    lines = [
        "첫 번째 줄\n",
        "두 번째 줄\n", 
        "세 번째 줄\n"
    ]
    file.writelines(lines)

print("✅ multiple_lines.txt 파일도 완성!")