import time
import random
def linear_search(arr, target, key=None):
    for i in range(len(arr)):
        compare_value = key(arr[i]) if key else arr[i]
        if compare_value == target:
            return i
    return -1

def binary_search(arr, target, key=None):  
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = key(arr[mid]) if key else arr[mid]
        if mid_value == target:
            return mid
        elif mid_value > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# ===== Level 1: 기본 성능 비교기 =====

def generate_test_data(size):
    
    # 테스트용 정렬된 데이터 생성

    data = list(range(0, size * 2 , 2))
    return data

def measure_search_time(search_function, data, target):
    
    # 탐색 함수의 실행시간 측정

    start_time = time.perf_counter()
    search_function(data, target)
    end_time = time.perf_counter()
    return end_time - start_time
    
   

def run_performance_test(data_size):
    
    # 특정 크기 데이터로 성능 테스트 실행

    print(f"\n=== 데이터 크기: {data_size}개 ===")
    
    data = generate_test_data(data_size)
    target = random.choice(data)

    print(f"찾을 값: {target}")
    linear_time = measure_search_time(linear_search, data, target)
    binary_time = measure_search_time(binary_search, data, target)

    print(f"선형탐색: {linear_time:.8f}초")
    print(f"이진탐색: {binary_time:.8f}초") 
    if binary_time > 0:
        print(f"속도 차이: {linear_time/binary_time:.1f}배")
    else:
        print("이진탐색이 너무 빨라서 측정 불가!")

def show_comparison_table():
   
    """
    여러 데이터 크기로 비교 테스트 실행
    
    목표: 100, 1000, 10000개 데이터로 성능 비교표 만들기
    """
    print("🔍 탐색 알고리즘 성능 비교 시뮬레이터")
    print("=" * 50)
    
    data_sizes = [1000000, 10000000]  
    for size in data_sizes:
        run_performance_test(size)
    
    print("\n📊 결론:")
    print("- 데이터 크기가 클수록 이진탐색이 압도적으로 빠름!")
    print("- 선형탐색: O(n), 이진탐색: O(log n)")

def main():
    """메인 실행 함수"""
    show_comparison_table()
    return

if __name__ == "__main__":
    main()