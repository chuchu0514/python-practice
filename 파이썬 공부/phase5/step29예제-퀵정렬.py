# 📚 퀵 정렬 (Quick Sort) 완전 가이드

print("=== 5️⃣ 퀵 정렬 (Quick Sort) ===")
print("⚡ 개념: '피벗 기준으로 좌우 분할!' - 평균적으로 가장 빠른 정렬")
print("🎯 분할정복 + 제자리 정렬의 결합")

print("\n💡 퀵 정렬의 핵심:")
print("1️⃣ 피벗(pivot) 선택: 기준값 하나 정하기")
print("2️⃣ 분할(partition): 피벗보다 작은 것은 왼쪽, 큰 것은 오른쪽")
print("3️⃣ 재귀: 왼쪽과 오른쪽을 각각 퀵 정렬")

print("\n🎯 퀵 정렬 작동 원리:")
print("[3, 6, 8, 10, 1, 2, 1]")
print("피벗=3을 선택 → 3보다 작은 것 | 3 | 3보다 큰 것")
print("[1, 2, 1] | 3 | [6, 8, 10]")
print("        ↓ 재귀            ↓ 재귀")
print("각각 다시 퀵 정렬")

print("\n🔄 병합 정렬 vs 퀵 정렬:")
print("🔀 병합: 반으로 나누고 → 정렬 → 합치기")
print("⚡ 퀵: 피벗 기준으로 나누고 → 정렬 (합치기 불필요)")

def partition(arr, low, high):
    """배열을 피벗 기준으로 분할"""
    pivot = arr[high]  # 마지막 원소를 피벗으로 선택
    print(f"    분할 작업: {arr[low:high+1]}, 피벗={pivot}")
    
    i = low - 1  # 작은 원소들의 끝 인덱스
    
    for j in range(low, high):
        print(f"      {arr[j]} vs {pivot}: ", end="")
        
        # 현재 원소가 피벗보다 작거나 같으면
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"{arr[j]}는 작음 → 교환 {arr}")
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
test_data = [3, 6, 8, 10, 1, 2, 1]
print(f"정렬 전: {test_data}")
quick_sort(test_data.copy())
print(f"\n🎉 최종 결과: {quick_sort_simple(test_data)}")

print("\n" + "="*60)

# 다양한 케이스 테스트
test_cases = [
    [3, 1, 4, 1, 5, 9, 2],
    [1, 2, 3, 4, 5],        # 이미 정렬된 경우
    [5, 4, 3, 2, 1],        # 역순 정렬
    [7, 7, 7, 7],           # 중복값
    [42],                   # 단일 원소
    []                      # 빈 배열
]

print("📊 다양한 테스트 케이스:")
for i, case in enumerate(test_cases, 1):
    print(f"테스트 케이스 {i}: {case}")
    result = quick_sort_simple(case.copy())
    print(f"결과: {result}\n")

print("="*60)

print("🎯 퀵 정렬 특징:")
print("✅ 장점:")
print("  - 평균적으로 가장 빠름: O(n log n)")
print("  - 제자리 정렬: O(log n) 공간복잡도")
print("  - 실무에서 가장 많이 사용")
print("  - 캐시 효율성이 좋음")

print("❌ 단점:")
print("  - 최악의 경우 느림: O(n²)")
print("  - 불안정 정렬: 같은 값의 순서 바뀔 수 있음")
print("  - 피벗 선택에 따라 성능 차이 큼")

print("\n⏰ 시간복잡도:")
print("- 최선: O(n log n) - 피벗이 항상 중간값")
print("- 평균: O(n log n) - 피벗이 적당한 위치")
print("- 최악: O(n²) - 피벗이 항상 최솟값/최댓값 (이미 정렬된 배열)")

print("\n🔍 공간복잡도:")
print("- 평균: O(log n) - 재귀 호출 스택")
print("- 최악: O(n) - 스택 오버플로 위험")

print("\n🆚 5가지 정렬 총정리:")
comparison_table = """
| 정렬   | 평균 시간    | 최악 시간    | 공간     | 안정성 | 특징 |
|--------|-------------|-------------|----------|--------|------|
| 버블   | O(n²)       | O(n²)       | O(1)     | ✅     | 최적화 가능 |
| 선택   | O(n²)       | O(n²)       | O(1)     | ❌     | 교환 적음 |
| 삽입   | O(n²)       | O(n²)       | O(1)     | ✅     | 거의 정렬시 빠름 |
| 병합   | O(n log n)  | O(n log n)  | O(n)     | ✅     | 항상 일정한 성능 |
| 퀵     | O(n log n)  | O(n²)       | O(log n) | ❌     | 평균적으로 가장 빠름 |
"""
print(comparison_table)

print("💡 피벗 선택 방법:")
print("1. 첫 번째 원소: 구현 간단, 성능 불안정")
print("2. 마지막 원소: 일반적인 방법")  
print("3. 중간 원소: 평균적으로 좋음")
print("4. 3개 중위값: 첫째, 중간, 마지막 중 중간값")
print("5. 랜덤 선택: 최악의 경우 확률 낮춤")

print("\n🌟 실무에서 퀵 정렬:")
print("- Python sorted(): Timsort (병합+삽입 하이브리드)")
print("- C++ std::sort: 인트로정렬 (퀵+힙+삽입 하이브리드)")  
print("- Java Arrays.sort(): 듀얼 피벗 퀵정렬")
print("- 대부분 언어에서 퀵정렬을 기반으로 개선된 버전 사용")

print("\n🎮 실습 과제:")
print("1. 왜 퀵 정렬이 이미 정렬된 배열에서 O(n²)가 될까요?")
print("2. 피벗을 랜덤으로 선택하면 어떤 장점이 있을까요?")
print("3. 언제 퀵 정렬 대신 병합 정렬을 선택해야 할까요?")

print("\n💡 다음에 배울 것:")
print("🔍 탐색 알고리즘 - 선형 탐색과 이진 탐색")
print("🌳 트리 자료구조와 이진 탐색 트리")

print("\n✅ 퀵 정렬 완전 마스터!")
print("🎉 5가지 정렬 알고리즘을 모두 정복했습니다!")