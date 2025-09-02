

def partition(arr, low, high):
    mid = (low + high) // 2
  
    arr[mid], arr[high] = arr[high], arr[mid]
    
   
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

    return arr

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
result = quick_sort(test_data.copy())
print(f"결과: {result}")

print("\n" + "="*60)
