# 📚 선택 정렬 (Selection Sort) 완전 가이드

print("=== 2️⃣ 선택 정렬 (Selection Sort) ===")
print("👆 개념: '가장 작은 것을 찾아서 맨 앞으로!' 직관적인 정렬")

print("\n🎯 작동 원리:")
print("[64, 25, 12, 22, 11]")
print("1라운드: 전체에서 가장 작은 11을 찾아 → 맨 앞으로")
print("[11, 25, 12, 22, 64]")
print("2라운드: 나머지에서 가장 작은 12를 찾아 → 두 번째로")  
print("[11, 12, 25, 22, 64]")
print("3라운드: 나머지에서 가장 작은 22를 찾아 → 세 번째로")
print("[11, 12, 22, 25, 64]")
print("4라운드: 나머지에서 가장 작은 25를 찾아 → 네 번째로") 
print("[11, 12, 22, 25, 64] → 완성!")

print("\n🔄 버블 정렬 vs 선택 정렬:")
print("🫧 버블: 옆끼리 비교하면서 큰 것을 뒤로 밀기")
print("👆 선택: 최솟값을 찾아서 앞자리에 직접 배치")

def selection_sort(arr):
    """선택 정렬 구현"""
    n = len(arr)
    print(f"👆 선택 정렬 시작! 배열 크기: {n}")
    print(f"정렬 전: {arr}")
    
    # 전체 라운드 (n-1번)
    for i in range(n - 1):
        print(f"\n--- {i+1}라운드 시작 ---")
        print(f"정렬된 부분: {arr[:i]} | 미정렬 부분: {arr[i:]}")
        
        # 현재 위치를 최솟값 위치로 가정
        min_idx = i
        min_value = arr[i]
        print(f"초기 최솟값 후보: {min_value} (인덱스 {min_idx})")
        
        # i+1부터 끝까지에서 최솟값 찾기
        for j in range(i + 1, n):
            print(f"  비교: {min_value} vs {arr[j]}", end=" ")
            if arr[j] < arr[min_idx]:
                min_idx = j
                min_value = arr[j]
                print(f"→ 새로운 최솟값 발견! {min_value}")
            else:
                print(f"→ {min_value}가 더 작음")
        
        # 최솟값을 현재 위치로 이동
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"교환: {arr[min_idx]} ↔ {arr[i]}")
        else:
            print(f"교환 불필요: {arr[i]}가 이미 제자리")
            
        print(f"{i+1}라운드 완료: {arr}")
        print(f"→ {arr[i]}이 {i+1}번째 자리에 확정!")
    
    print(f"\n🎉 최종 결과: {arr}")
    return arr

def selection_sort_simple(arr):
    """간단한 선택 정렬 (실무용)"""
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 테스트해보기
print("\n=== 👆 선택 정렬 테스트 ===")
test_data = [64, 25, 12, 22, 11]
selection_sort(test_data.copy())

print("\n" + "="*50)

# 다양한 케이스 테스트
test_cases = [
    [3, 1, 4, 1, 5],
    [1, 2, 3, 4, 5],  # 이미 정렬된 경우
    [5, 4, 3, 2, 1],  # 역순 정렬
    [7, 7, 7, 7],     # 중복값
    [42]              # 단일 원소
]

print("📊 다양한 테스트 케이스:")
for i, case in enumerate(test_cases, 1):
    print(f"\n테스트 케이스 {i}: {case}")
    result = selection_sort_simple(case.copy())
    print(f"결과: {result}")

print("\n" + "="*50)

print("🎯 선택 정렬 특징:")
print("✅ 장점:")
print("  - 이해하기 매우 쉬움 (직관적)")
print("  - 교환 횟수가 적음 (최대 n-1번)")
print("  - 메모리 사용량 적음 (제자리 정렬)")
print("❌ 단점:")
print("  - 느림 (항상 O(n²))")
print("  - 안정 정렬이 아님 (같은 값의 순서가 바뀔 수 있음)")

print("\n⏰ 시간복잡도:")
print("- 최선: O(n²) - 이미 정렬되어도 모든 원소를 확인")
print("- 평균: O(n²)")
print("- 최악: O(n²)")
print("→ 버블 정렬과 달리 최적화 불가능!")

print("\n🔍 동작 분석:")
print("외부 루프: n-1번")
print("내부 루프: 평균 n/2번")
print("총 비교 횟수: (n-1) × (n/2) ≈ n²/2")
print("교환 횟수: 최대 n-1번 (버블 정렬보다 적음!)")

print("\n🆚 버블 vs 선택 정렬 비교:")
comparison_data = [5, 2, 8, 1, 9]
print(f"테스트 데이터: {comparison_data}")

print("\n버블 정렬 교환 과정:")
bubble_data = comparison_data.copy()
exchanges = 0
n = len(bubble_data)
for i in range(n-1):
    for j in range(n-i-1):
        if bubble_data[j] > bubble_data[j+1]:
            bubble_data[j], bubble_data[j+1] = bubble_data[j+1], bubble_data[j]
            exchanges += 1
print(f"버블 정렬 교환 횟수: {exchanges}")

print("\n선택 정렬 교환 과정:")
selection_data = comparison_data.copy()
exchanges = 0
n = len(selection_data)
for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if selection_data[j] < selection_data[min_idx]:
            min_idx = j
    if min_idx != i:
        selection_data[i], selection_data[min_idx] = selection_data[min_idx], selection_data[i]
        exchanges += 1
print(f"선택 정렬 교환 횟수: {exchanges}")

print("\n🎮 실습 과제:")
print("1. 왜 선택 정렬은 최적화가 불가능할까요?")
print("2. 교환 횟수가 적다는 것의 장점은 무엇일까요?") 
print("3. 어떤 상황에서 선택 정렬이 버블 정렬보다 유리할까요?")

print("\n💡 다음에 배울 것: 삽입 정렬!")
print("삽입 정렬은 '카드 게임하듯이 하나씩 끼워넣기' 방식이에요!")

print("\n✅ 선택 정렬 완전 마스터!")