# 🎯 함수 하나만 디버깅해보기: calculate_average

def calculate_average(numbers):
    """숫자 리스트의 평균을 계산"""
    total = 0  # 🔴 중단점 1
    count = 0  # 🔴 중단점 2
    if not numbers:
        print("⚠️ 빈 리스트로는 평균을 계산할 수 없습니다")
        return 0
    
    for num in numbers:  # 🔴 중단점 3
        total += num     # 🔴 중단점 4
        count += 1       # 🔴 중단점 5
    
    average = total / count  # 🔴 중단점 6
    return average           # 🔴 중단점 7

# 🧪 간단한 테스트
if __name__ == "__main__":
    print("=== 테스트 1: 정상적인 경우 ===")
    numbers = [10, 20, 30]  # 🔴 중단점 8
    result = calculate_average(numbers)  # 🔴 중단점 9 - F11로 함수 안 들어가기!
    print(f"결과: {result}")  # 🔴 중단점 10
    
    print("\n=== 테스트 2: 빈 리스트 (에러 발생!) ===")
    empty_list = []  # 🔴 중단점 11
    result2 = calculate_average(empty_list)  # 🔴 중단점 12
    print(f"결과: {result2}")

    