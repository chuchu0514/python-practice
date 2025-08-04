# 🤔 repr() 함수 설명

print("=== repr()이 뭔가요? ===")
print("repr = representation (표현)")
print("'개발자가 보기 좋게' 데이터를 표시해주는 함수")

print("\n" + "="*40)

# 1. 일반 print vs repr 비교
text = "안녕하세요\n반갑습니다"

print("1. 일반 print:")
print(text)

print("\n2. repr로 출력:")  
print(repr(text))

print("\n" + "="*40)

# 2. 왜 repr을 쓸까?
print("=== 왜 repr을 쓸까? ===")

# 숨겨진 문자들을 볼 수 있어요!
hidden_text = "보이는 글자\t탭 문자\n줄바꿈"

print("일반 출력:")
print(f"내용: {hidden_text}")

print("\nrepr 출력:")
print(f"내용: {repr(hidden_text)}")

print("\n💡 repr의 장점:")
print("- \\n (줄바꿈), \\t (탭) 같은 특수문자가 보임")
print("- 문자열의 정확한 내용을 확인 가능")
print("- 디버깅할 때 유용!")

print("\n" + "="*40)

# 3. 파일 내용 확인할 때 유용한 예시
print("=== 파일 내용 확인 예시 ===")

# 파일 만들기
with open('test.txt', 'w', encoding='utf-8') as file:
    file.write("첫줄\n두번째줄\n")

# 파일 읽기
with open('test.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print("일반 출력:")
print(f"파일 내용: {content}")

print("repr 출력:")
print(f"파일 내용: {repr(content)}")

print("\n💡 repr로 보면:")
print("- 줄바꿈이 \\n으로 표시됨")
print("- 파일 끝에 줄바꿈이 있는지 확인 가능")

print("\n" + "="*40)

# 4. 지금 당장 알 필요 있나?
print("=== 🤔 지금 당장 알 필요 있나? ===")
print("❌ 지금은 몰라도 됩니다!")
print("✅ 그냥 print() 써도 충분해요")
print("🔧 나중에 디버깅할 때 유용한 도구 정도로만 기억하세요")

print("\n간단 정리:")
print("print(text)     # 사용자가 보기 좋게")
print("print(repr(text)) # 개발자가 보기 좋게 (숨겨진 문자도 표시)")