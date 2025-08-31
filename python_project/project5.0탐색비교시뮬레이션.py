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
    """
    테스트용 정렬된 데이터 생성
    
    목표: size 크기의 정렬된 리스트 만들기
    힌트: range() 사용하거나 random.sample() + sort() 사용
    """
    # TODO: size 크기의 정렬된 리스트 생성
    # TODO: 예) [1, 2, 3, 4, 5, ...] 또는 무작위 수들을 정렬
    

def measure_search_time(search_function, data, target):
    """
    탐색 함수의 실행시간 측정
    
    목표: 특정 탐색 함수가 target을 찾는데 걸리는 시간 측정
    힌트: time.time()으로 시작/끝 시간 기록
    """
    # TODO: 시작 시간 기록
    # TODO: search_function 실행
    # TODO: 끝 시간 기록  
    # TODO: 실행시간 계산해서 반환
   

def run_performance_test(data_size):
    
    """
    특정 크기 데이터로 성능 테스트 실행
    
    목표: 선형탐색 vs 이진탐색 성능 비교
    힌트: 같은 데이터, 같은 target으로 두 알고리즘 테스트
    """
    print(f"\n=== 데이터 크기: {data_size}개 ===")
    
    # TODO: 테스트 데이터 생성
    # TODO: 찾을 target 정하기 (데이터 중간쯤 값 추천)
    
    print(f"찾을 값: {target}")
    
    # TODO: 선형탐색 시간 측정
    # TODO: 이진탐색 시간 측정
    
    # TODO: 결과 출력
    print(f"선형탐색: {linear_time:.6f}초")
    print(f"이진탐색: {binary_time:.6f}초") 
    print(f"속도 차이: {linear_time/binary_time:.1f}배")

def show_comparison_table():
   
    """
    여러 데이터 크기로 비교 테스트 실행
    
    목표: 100, 1000, 10000개 데이터로 성능 비교표 만들기
    """
    print("🔍 탐색 알고리즘 성능 비교 시뮬레이터")
    print("=" * 50)
    
    data_sizes = [100, 1000, 10000]  # 테스트할 데이터 크기들
    
    # TODO: 각 크기별로 성능 테스트 실행
    # TODO: for문으로 data_sizes 순회하면서 run_performance_test() 호출
    
    print("\n📊 결론:")
    print("- 데이터 크기가 클수록 이진탐색이 압도적으로 빠름!")
    print("- 선형탐색: O(n), 이진탐색: O(log n)")

def main():
    """메인 실행 함수"""
    # TODO: show_comparison_table() 호출해서 전체 시뮬레이션 실행
    pass

if __name__ == "__main__":
    main()