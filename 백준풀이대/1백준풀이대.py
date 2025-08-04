# 🔄 try-except 흐름 이해하기

print("=== try-except 흐름도 ===")
print("""
🔄 흐름:
1. try: 위험한 코드 실행 시도
2-a. 에러 없음 → else 실행 → finally 실행
2-b. 에러 발생 → except 실행 → finally 실행
3. finally: 항상 실행 (에러 있든 없든)
""")

print("\n" + "="*40)

print("=== 실험 1: 에러가 없는 경우 ===")
try:
    print("🔹 try: 10 + 5 계산 중...")
    result = 10 + 5
    print(f"🔹 try: 계산 성공! 결과 = {result}")
except:
    print("🔹 except: 에러 처리")
else:
    print("🔹 else: 에러가 없었어요!")
finally:
    print("🔹 finally: 항상 실행되는 부분")

print("\n" + "-"*30)

print("=== 실험 2: 에러가 있는 경우 ===")
try:
    print("🔸 try: 10 ÷ 0 계산 중...")
    result = 10 / 0  # 에러 발생!
    print("🔸 try: 이 줄은 실행 안 됨")
except ZeroDivisionError:
    print("🔸 except: 0으로 나누기 에러 처리!")
else:
    print("🔸 else: 이 줄은 실행 안 됨")
finally:
    print("🔸 finally: 항상 실행되는 부분")

print("\n" + "="*40)

print("=== 쉬운 비유로 설명 ===")
print("""
🏠 집에 들어가는 상황으로 비유:

try:
    문을 열어보자 (위험한 시도)
    
except KeyError:
    열쇠가 없다면 → 창문으로 들어가자
    
except LockError:  
    문이 잠겼다면 → 관리사무소에 연락하자
    
else:
    문이 잘 열렸다면 → "안전하게 들어왔어요!"
    
finally:
    어떤 상황이든 → "집에 도착했어요!"
""")

print("\n" + "="*40)

print("=== 실제로 유용한 예시 ===")

def safe_divide(a, b):
    try:
        result = a / b
        print(f"✅ 계산 성공: {a} ÷ {b} = {result}")
        return result
    except ZeroDivisionError:
        print("❌ 0으로 나눌 수 없어요!")
        return None
    except TypeError:
        print("❌ 숫자가 아닌 값이 있어요!")
        return None
    finally:
        print("🔚 계산 시도 완료")

# 테스트
safe_divide(10, 2)   # 정상 케이스
print()
safe_divide(10, 0)   # 에러 케이스
print()  
safe_divide(10, "a") # 다른 에러 케이스