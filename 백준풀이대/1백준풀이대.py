

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result




def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    result = merge(left_sorted, right_sorted)
    return result






def merge_sort_simple(arr):
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

    if i < len(left):
        result.extend(left[i:])
    elif j <len(right):
        result.extend(right[j:])

    return result





# 테스트해보기
print("\n=== ⚡ 병합 정렬 테스트 ===")
test_data = [38, 27, 43, 3, 9, 82, 10]
print(f"정렬 전: {test_data}")
result = merge_sort(test_data)

result = merge_sort_simple(test_data)
print(f"\n🎉 최종 결과: {result}")

print("\n" + "="*60)