# 1. 이 일반 함수를 람다로 바꾸기
def triple(x):
    return x * 3

triple = lambda x : x * 3

print(f"{triple(3)}")

# 2. 리스트에서 홀수만 걸러내기 (filter 사용)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odds = list(filter(lambda x : x % 2 == 1, numbers))
print(f"홀수들: {odds}")


# 3. 리스트의 모든 문자열을 대문자로 (map 사용)  
words = ["hello", "world", "python"]
uppercase_words = list(map(lambda word: word.upper(), words))
print(f"대문자: {uppercase_words}")

# upper() - 대문자로
# lower() - 소문자로
# strip() - 앞뒤 공백 제거
# replace() - 문자 바꾸기
# split() - 나누기