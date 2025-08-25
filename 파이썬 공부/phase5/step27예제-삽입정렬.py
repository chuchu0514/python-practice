# 📚 삽입 정렬 (Insertion Sort) 완전 가이드

print("=== 3️⃣ 삽입 정렬 (Insertion Sort) ===")
print("🃏 개념: '카드 게임하듯이 하나씩 끼워넣기!' 가장 직관적인 정렬")

print("\n🎯 실생활 예시:")
print("🃏 포커 게임에서 카드 정렬하는 방법")
print("📚 책장에서 책 하나씩 올바른 위치에 끼워넣기")
print("👥 키 순으로 줄 서기 (한 명씩 적절한 위치로)")

print("\n🎯 작동 원리:")
print("[5, 2, 4, 6, 1, 3]")
print("1단계: [5] | 2,4,6,1,3  →  2를 5 앞에 삽입")
print("      [2, 5] | 4,6,1,3")
print("2단계: [2, 5] | 4,6,1,3  →  4를 2와 5 사이에 삽입") 
print("      [2, 4, 5] | 6,1,3")
print("3단계: [2, 4, 5] | 6,1,3  →  6을 맨 뒤에 삽입")
print("      [2, 4, 5, 6] | 1,3")
print("4단계: [2, 4, 5, 6] | 1,3  →  1을 맨 앞에 삽입")
print("      [1, 2, 4, 5, 6] | 3")
print("5단계: [1, 2, 4, 5, 6] | 3  →  3을 2와 4 사이에 삽입")
print("      [1, 2, 3, 4, 5, 6] → 완성!")

print("\n🔄 3가지 정렬 방식 비교:")
print("🫧 버블: 옆끼리 비교하면서 큰 것을 뒤로 밀기")
print("👆 선택: 최솟값을 찾아서 앞자리에 직접 배치")
print("🃏 삽입: 하나씩 가져와서 정렬된 부분에 끼워넣기")

def insertion_sort(arr):
    """삽입 정렬 구현"""
    n = len(arr)
    print(f"🃏 삽입 정렬 시작! 배열 크기: {n}")
    print(f"정렬 전: {arr}")
    
    # 두 번째 원소부터 시작 (첫 번째는 이미 정렬된 것으로 간주)
    for i in range(1, n):
        key = arr[i]  # 삽입할 값
        print(f"\n--- {i}단계: {key}를 삽입 ---")
        print(f"정렬된 부분: {arr[:i]} | 현재 삽입할 값: {key} | 남은 부분: {arr[i+1:]}")
        
        # key를 정렬된 부분에서 적절한 위치에 삽입
        j = i - 1
        
        print(f"  {key}가 들어갈 자리를 찾아보자...")
        
        # key보다 큰 값들을 오른쪽으로 이동
        while j >= 0 and arr[j] > key:
            print(f"    {arr[j]} > {key} → {arr[j]}를 오른쪽으로 이동")
            arr[j + 1] = arr[j]
            j -= 1
            print(f"    현재 상태: {arr}")
        
        # key를 올바른 위치에 삽입
        arr[j + 1] = key
        print(f"  {key}를 {j+1}번 위치에 삽입!")
        print(f"{i}단계 완료: {arr}")
        print(f"→ 정렬된 부분이 {i+1}개로 확장됨!")
    
    print(f"\n🎉 최종 결과: {arr}")
    return arr

def insertion_sort_simple(arr):
    """간단한 삽입 정렬 (실무용)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 테스트해보기
print("\n=== 🃏 삽입 정렬 테스트 ===")
test_data = [5, 2, 4, 6, 1, 3]
insertion_sort(test_data.copy())

print("\n" + "="*50)

# 다양한 케이스 테스트
test_cases = [
    [3, 1, 4, 1, 5, 9],
    [1, 2, 3, 4, 5],     # 이미 정렬된 경우
    [5, 4, 3, 2, 1],     # 역순 정렬
    [2, 2, 2, 2],        # 중복값
    [7]                  # 단일 원소
]

print("📊 다양한 테스트 케이스:")
for i, case in enumerate(test_cases, 1):
    print(f"\n테스트 케이스 {i}: {case}")
    result = insertion_sort_simple(case.copy())
    print(f"결과: {result}")

print("\n" + "="*50)

print("🎯 삽입 정렬 특징:")
print("✅ 장점:")
print("  - 직관적이고 이해하기 쉬움 (실생활과 동일)")
print("  - 이미 정렬된 데이터에서 매우 빠름 O(n)")
print("  - 안정 정렬 (같은 값의 순서 유지)")
print("  - 온라인 알고리즘 (데이터가 실시간으로 들어와도 처리 가능)")
print("  - 작은 데이터셋에서 효율적")

print("❌ 단점:")
print("  - 큰 데이터에서 느림 (평균 O(n²))")
print("  - 최악의 경우 매우 느림 (역순 정렬시)")

print("\n⏰ 시간복잡도:")
print("- 최선: O(n) - 이미 정렬된 경우 (각 원소마다 1번씩만 비교)")
print("- 평균: O(n²) - 랜덤 데이터")
print("- 최악: O(n²) - 역순으로 정렬된 경우")

print("\n🔍 동작 분석:")
print("외부 루프: n-1번 (1부터 n-1까지)")
print("내부 루프: 평균 i/2번 (최악의 경우 i번)")
print("총 비교 횟수: 평균 (1+2+...+(n-1))/2 ≈ n²/4")

print("\n🆚 3가지 정렬 비교:")
print("구현 난이도: 버블 = 삽입 < 선택")
print("최선 성능: 삽입 O(n) > 버블 O(n) > 선택 O(n²)")
print("평균 성능: 삽입 ≈ 버블 ≈ 선택 (모두 O(n²))")
print("교환 횟수: 선택 < 삽입 < 버블")
print("실용성: 삽입 > 선택 > 버블")

print("\n💡 실무에서 삽입 정렬이 쓰이는 경우:")
print("- 작은 배열 (< 50개) 정렬")
print("- 거의 정렬된 데이터 처리")
print("- 다른 고급 정렬의 하위 루틴 (퀵정렬 + 삽입정렬 조합)")
print("- 실시간 데이터 스트림 정렬")

print("\n🎮 실습 과제:")
print("1. 왜 삽입 정렬이 이미 정렬된 데이터에서 O(n)일까요?")
print("2. 삽입 정렬이 '안정 정렬'인 이유는 무엇일까요?")
print("3. 어떤 상황에서 삽입 정렬을 선택하는 것이 좋을까요?")

print("\n💡 다음에 배울 것: 병합 정렬!")
print("드디어 O(n log n) 고성능 정렬의 세계로! 분할정복의 마법을 경험해보세요!")

print("\n✅ 삽입 정렬 완전 마스터!")