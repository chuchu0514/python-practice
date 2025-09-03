def partition(arr, low, high):
    """배열을 피벗 기준으로 분할"""
    pivot = arr[high]  # 마지막 원소를 피벗으로 선택
    print(f"    분할 작업: {arr[low:high+1]}, 피벗={pivot}")
    
    i = low - 1  # 작은 원소들의 끝 인덱스
    
    for j in range(low, high):
        print(f"      {arr[j]} vs {pivot}: ", end="")
        
        # 현재 원소가 피벗보다 작거나 같으면
        if arr[j] <= pivot:
            original_value = arr[j]
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"{original_value}는 작음 → 교환 {arr}")
        else:
            print(f"{arr[j]}는 큼 → 그대로")
    
    # 피벗을 올바른 위치에 배치
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"    피벗 {pivot}를 최종 위치 {i+1}에 배치: {arr}")
    print(f"    결과: 작은 부분 {arr[low:i+1]} | 피벗 {pivot} | 큰 부분 {arr[i+2:high+1]}")
    
    return i + 1  # 피벗의 최종 위치

def quick_sort(arr, low=0, high=None):
    """퀵 정렬 구현"""
    if high is None:
        high = len(arr) - 1
        print(f"⚡ 퀵 정렬 시작: {arr}")
    
    if low < high:
        print(f"\n정렬 구간: {arr[low:high+1]} (인덱스 {low}~{high})")
        
        # 분할하고 피벗 위치 얻기
        pivot_index = partition(arr, low, high)
        
        print(f"피벗 위치 확정: 인덱스 {pivot_index}")
        print(f"현재 상태: {arr}")
        
        # 피벗 왼쪽 부분 정렬
        print(f"\n왼쪽 부분 정렬: {arr[low:pivot_index]}")
        quick_sort(arr, low, pivot_index - 1)
        
        # 피벗 오른쪽 부분 정렬
        print(f"\n오른쪽 부분 정렬: {arr[pivot_index+1:high+1]}")
        quick_sort(arr, pivot_index + 1, high)
    

# 간단한 퀵 정렬 (출력 없는 버전)
def quick_sort_simple(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort_simple(left) + middle + quick_sort_simple(right)

# 테스트해보기
print("\n=== ⚡ 퀵 정렬 테스트 ===")
test_data = [3, 6, 8, 10, 1, 2, 2]
print(f"정렬 전: {test_data}")
result = quick_sort(test_data)
print(f"결과: {test_data}")

print("\n" + "="*60)
