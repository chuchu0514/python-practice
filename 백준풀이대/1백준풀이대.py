count = 0  # 전역변수

def test1_read_global():
    """전역변수 읽기만 하기"""
    print(f"전역변수 count 읽기: {count}")  # ✅ 가능

def test2_local_variable():
    """지역변수 새로 만들기"""
    count = 100  # 새로운 지역변수 (전역변수와 이름만 같음)
    count = count + 50  # 지역변수 수정
    print(f"지역변수 count: {count}")

def test3_try_modify():
    """전역변수 수정 시도 (실패)"""
    try:
        count = count + 1  # ❌ 에러 발생
    except UnboundLocalError:
        print("에러! 전역변수를 함수에서 직접 수정할 수 없음")

def test4_global_modify():
    """global로 전역변수 수정"""
    global count
    count = count + 1  # ✅ 성공
    print(f"global로 전역변수 수정: {count}")

print("=== 실험 시작 ===")
print(f"초기 전역변수: {count}")

print("\n1. 전역변수 읽기:")
test1_read_global()

print("\n2. 지역변수 만들기:")
test2_local_variable()
print(f"실험 후 전역변수: {count}")  # 여전히 0

print("\n3. 전역변수 수정 시도:")
test3_try_modify()

print("\n4. global로 전역변수 수정:")
test4_global_modify()
print(f"최종 전역변수: {count}")  # 1로 변경됨

print("\n=== 결론 ===")
print("✅ 함수에서 전역변수 읽기: 가능")
print("❌ 함수에서 전역변수 수정: 불가능 (global 없으면)")
print("✅ 지역변수 만들기: 가능 (전역변수와 별개)")
print("✅ global 키워드로 수정: 가능")