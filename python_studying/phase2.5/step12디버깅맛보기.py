# 버그가 있는 코드 예시
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)  # 만약 numbers가 빈 리스트라면?
    return average

# print() 디버깅으로 문제 찾기
def calculate_average_debug(numbers):
    print(f"🔍 함수 시작: numbers = {numbers}")  # 입력값 확인
    
    total = 0
    print(f"🔍 초기 total = {total}")
    
    for num in numbers:
        total += num
        print(f"🔍 현재 num = {num}, total = {total}")  # 반복 과정 확인
    
    print(f"🔍 반복 완료: total = {total}, len(numbers) = {len(numbers)}")
    
    if len(numbers) == 0:  # 버그 발견 후 수정!
        print("🔍 빈 리스트 감지!")
        return 0
    
    average = total / len(numbers)
    print(f"🔍 계산된 평균 = {average}")
    return average

# 테스트
print("=== 정상 케이스 ===")
result1 = calculate_average_debug([10, 20, 30])

print("\n=== 문제 케이스 ===")
result2 = calculate_average_debug([])  # 빈 리스트

print(f"\n최종 결과: {result1}, {result2}")