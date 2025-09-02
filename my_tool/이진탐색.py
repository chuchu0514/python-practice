
def binary_search(arr, target):
    """
    정렬된 배열에서 target을 이진탐색으로 찾기
    
    Args:
        arr: 정렬된 리스트
        target: 찾을 값
        
    Returns:
        int: 찾은 인덱스, 없으면 -1
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid  # 찾았다!
        elif arr[mid] < target:
            left = mid + 1  # 오른쪽 절반에서 찾기
        else:
            right = mid - 1  # 왼쪽 절반에서 찾기
    
    return -1  # 못찾음


def binary_search_recursive(arr, target, left=0, right=None):
    """재귀로 구현한 이진탐색"""
    if right is None:
        right = len(arr) - 1
    
    # 기저 조건: 범위가 잘못되면 못찾음
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)