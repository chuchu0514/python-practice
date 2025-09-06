# 📚 병합 정렬 (Merge Sort) 완전 가이드

print("=== 4️⃣ 병합 정렬 (Merge Sort) ===")
print("⚡ 개념: '분할정복!' - 나누고, 정복하고, 합치기")
print("🎯 드디어 O(n log n) 고성능 정렬의 세계!")

print("\n💡 분할정복(Divide and Conquer)란?")
print("1️⃣ Divide: 문제를 작은 부분으로 나누기")
print("2️⃣ Conquer: 작은 부분들을 해결하기") 
print("3️⃣ Combine: 해결된 부분들을 합치기")

print("\n🎯 실생활 예시:")
print("📚 도서관 책 정리: 책더미를 반으로 나누고 → 각각 정리하고 → 합치기")
print("🏢 회사 조직: 큰 프로젝트를 팀별로 나누고 → 각 팀이 해결하고 → 통합")
print("🧩 퍼즐 맞추기: 조각들을 그룹으로 나누고 → 각각 맞추고 → 전체 완성")

print("\n🎯 병합 정렬 작동 원리:")
print("[38, 27, 43, 3, 9, 82, 10]")
print("        ↓ 분할")
print("[38, 27, 43] | [3, 9, 82, 10]")
print("      ↓             ↓")
print("[38] [27, 43]  |  [3, 9] [82, 10]")
print(" ↓     ↓           ↓      ↓")
print("[38] [27][43]  |  [3][9] [82][10]")
print("      ↓ 병합             ↓")
print("[38] [27, 43]  |  [3, 9] [10, 82]")
print("      ↓             ↓")
print("[27, 38, 43]   |  [3, 9, 10, 82]")
print("        ↓ 최종 병합")
print("[3, 9, 10, 27, 38, 43, 82]")

print("\n🔄 이전 정렬들과의 차이:")
print("🫧🏃🃏 버블/선택/삽입: 원소끼리 직접 비교하며 이동")
print("⚡ 병합: 배열을 계속 반으로 나누다가 다시 합치면서 정렬")

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

# 테스트해보기
print("\n=== ⚡ 병합 정렬 테스트 ===")
test_data = [38, 27, 43, 3, 9, 82, 10]
print(f"정렬 전: {test_data}")
result = merge_sort(test_data)
print(f"\n🎉 최종 결과: {result}")

print("\n" + "="*60)

# 다양한 케이스 테스트
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

test_cases = [
    [3, 1, 4, 1, 5, 9, 2, 6],
    [1, 2, 3, 4, 5],        # 이미 정렬된 경우
    [5, 4, 3, 2, 1],        # 역순 정렬
    [7, 7, 7, 7],           # 중복값
    [42],                   # 단일 원소
    []                      # 빈 배열
]

print("📊 다양한 테스트 케이스:")
for i, case in enumerate(test_cases, 1):
    print(f"테스트 케이스 {i}: {case}")
    result = merge_sort_simple(case.copy())
    print(f"결과: {result}\n")

print("="*60)

print("🎯 병합 정렬 특징:")
print("✅ 장점:")
print("  - 빠른 성능: 항상 O(n log n) 보장")
print("  - 안정 정렬: 같은 값의 순서 유지")
print("  - 예측 가능: 최선/평균/최악이 모두 같음")
print("  - 큰 데이터에 적합: 성능 저하 없음")

print("❌ 단점:")
print("  - 추가 메모리 필요: O(n) 공간 복잡도")
print("  - 재귀 호출: 스택 오버플로 위험")
print("  - 작은 데이터에서는 오버헤드")

print("\n⏰ 시간복잡도: 항상 O(n log n)")
print("- 최선: O(n log n)")
print("- 평균: O(n log n)") 
print("- 최악: O(n log n)")
print("→ 데이터 상태와 무관하게 항상 같은 성능!")

print("\n🔍 시간복잡도 분석:")
print("분할 깊이: log n (배열을 계속 반으로 나누기)")
print("각 깊이에서 병합 시간: O(n) (모든 원소 한 번씩 처리)")
print("총 시간: O(log n) × O(n) = O(n log n)")

print("\n📊 성능 비교 (n=1000일 때):")
print("버블/선택/삽입: 1,000,000번 연산")
print("병합 정렬: 10,000번 연산 (100배 빠름!)")

print("\n🆚 4가지 정렬 비교:")
comparison_table = """
| 정렬   | 시간복잡도      | 안정성 | 공간복잡도 | 특징 |
|--------|-----------------|--------|------------|------|
| 버블   | O(n²)          | ✅     | O(1)       | 최적화 가능 |
| 선택   | O(n²)          | ❌     | O(1)       | 교환 적음 |
| 삽입   | O(n²)          | ✅     | O(1)       | 거의 정렬시 빠름 |
| 병합   | O(n log n)     | ✅     | O(n)       | 항상 빠름 |
"""
print(comparison_table)

print("💡 재귀(Recursion) 개념:")
print("- 함수가 자기 자신을 호출하는 것")
print("- 기저 사례(Base Case): 재귀를 멈추는 조건")
print("- 병합 정렬의 기저 사례: len(arr) <= 1")

print("\n🎮 실습 과제:")
print("1. 왜 병합 정렬의 시간복잡도가 O(n log n)일까요?")
print("2. 병합 과정에서 안정성은 어떻게 보장될까요?") 
print("3. 공간복잡도 O(n)이 단점인 상황은 언제일까요?")

print("\n💡 다음에 배울 것: 퀵 정렬!")
print("평균적으로 가장 빠른 정렬! 피벗(pivot)의 마법을 경험해보세요!")

print("\n✅ 병합 정렬 완전 마스터!")
print("🎉 축하합니다! 드디어 O(n log n) 고성능 알고리즘을 정복했어요!")