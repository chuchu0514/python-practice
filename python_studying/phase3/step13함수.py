"""
--매개변수와 인수
# 함수 정의 부분
def greet(name, age):  # ← name, age는 "매개변수(Parameter)"
    return f"안녕하세요! {name}님, {age}살이시군요!"

# 함수 호출 부분  
message = greet("김철수", 25)  # ← "김철수", 25는 "인수(Argument)"
print(message)

print("\n=== 용어 정리 ===")
print("📝 매개변수(Parameter): 함수를 '정의'할 때 사용하는 변수명")
print("📝 인수(Argument): 함수를 '호출'할 때 실제로 전달하는 값")

--전역, 지역변수
print("\n=== 이름이 같은 경우 ===")
name = "전역 김철수"  # 전역변수

def name_test():
    name = "지역 이영희"  # 지역변수 (전역변수와 이름 같음)
    print(f"함수 안에서 name: {name}")  # 지역변수가 우선!

    
--global

count = 0  # 전역변수

def wrong_way():
    count = count + 1  # ❌ 에러! 지역변수를 만들려 하는데 자기 자신을 참조
    return count

def right_way():
    global count  # 전역변수 count를 사용하겠다고 선언
    count = count + 1  # ✅ 이제 전역변수를 수정 가능
    return count
"""