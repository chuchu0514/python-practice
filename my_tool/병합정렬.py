def merge(left, right):
    """두 정렬된 배열을 병합"""
    result = []
    i = j = 0
    
    print(f"    병합 시작: {left} + {right}")
    
    # 두 배열을 비교하면서 작은 것부터 결과에 추가
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            print(f"      {left[i]} 선택 (왼쪽)")
            i += 1
        else:
            result.append(right[j])
            print(f"      {right[j]} 선택 (오른쪽)")
            j += 1
    
    # 남은 원소들 추가
    while i < len(left):
        result.append(left[i])
        print(f"      {left[i]} 추가 (왼쪽 남은 것)")
        i += 1
    
    while j < len(right):
        result.append(right[j])
        print(f"      {right[j]} 추가 (오른쪽 남은 것)")
        j += 1
    
    print(f"    병합 완료: {result}")
    return result

def merge_sort(arr):
    """병합 정렬 구현"""
    print(f"분할: {arr}")
    
    # 기저 사례: 원소가 1개 이하면 이미 정렬됨
    if len(arr) <= 1:
        print(f"  → 기저 사례 (정렬 완료): {arr}")
        return arr
    
    # 배열을 반으로 나누기
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    print(f"  → 왼쪽: {left}, 오른쪽: {right}")
    
    # 재귀적으로 왼쪽과 오른쪽을 정렬
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # 정렬된 두 배열을 병합
    result = merge(left_sorted, right_sorted)
    
    return result



def merge_sort_simple(arr):
    """간단한 병합 정렬 (출력 없는 버전)"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort_simple(arr[:mid])
    right = merge_sort_simple(arr[mid:])
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
