# 📚 정렬 알고리즘 완전 가이드

print("=== 📚 정렬 알고리즘이란 무엇인가? ===")
print("정렬 = 문제 해결의 시작점!")
print("- 프로그래밍의 가장 기본적인 사고 과정")
print("- 모든 알고리즘의 기초")

print("\n💡 실생활 예시:")
print("🏪 쇼핑몰: 가격순, 인기순 상품 정렬")
print("📱 연락처: 이름 가나다순 정렬")  
print("🎮 게임: 점수 랭킹 정렬")
print("📈 주식: 수익률순 정렬")
print("🔍 검색엔진: 관련도순 정렬")

print("\n🌟 구글에서 쓰는 곳:")
print("- 검색 결과 랭킹: 수십억 개 웹페이지 정렬")
print("- YouTube 추천: 조회수, 좋아요순 정렬")
print("- Gmail: 시간순 메일 정렬")
print("- Google Maps: 거리순 장소 정렬")

print("\n" + "="*50)

# 1️⃣ 버블 정렬 (Bubble Sort)
print("1️⃣ 버블 정렬 (Bubble Sort)")
print("🫧 개념: '거품이 물 위로 올라오듯이' 큰 값들이 뒤로 밀려나는 정렬")

print("\n🎯 작동 원리:")
print("[64, 34, 25, 12, 22, 11, 90]")
print(" ↑   ↑  비교해서 큰 것을 오른쪽으로!")
print("")
print("1라운드: [34, 25, 12, 22, 11, 64, 90]  # 64가 뒤로!")
print("2라운드: [25, 12, 22, 11, 34, 64, 90]  # 34가 뒤로!")
print("3라운드: [12, 22, 11, 25, 34, 64, 90]  # 25가 뒤로!")
print("...")

def bubble_sort(arr):
    """버블 정렬 구현"""
    n = len(arr)
    print(f"🫧 버블 정렬 시작! 배열 크기: {n}")
    print(f"정렬 전: {arr}")
    
    # 전체 라운드 (n-1번)
    for i in range(n - 1):
        print(f"\n--- {i+1}라운드 시작 ---")
        swapped = False  # 최적화: 교환 발생했는지 체크
        
        # 각 라운드에서 비교 (n-i-1번)
        for j in range(n - i - 1):
            print(f"비교: {arr[j]} vs {arr[j+1]}", end=" ")
            
            # 왼쪽이 더 크면 교환
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"→ 교환! {arr}")
            else:
                print(f"→ 그대로 {arr}")
        
        print(f"{i+1}라운드 완료: {arr}")
        print(f"→ 가장 큰 값 {arr[n-i-1]}이 {n-i}번째 자리에 확정!")
        
        # 최적화: 교환이 없으면 이미 정렬됨
        if not swapped:
            print("💡 더 이상 교환할 것이 없습니다. 정렬 완료!")
            break
    
    print(f"\n🎉 최종 결과: {arr}")
    return arr

def bubble_sort_simple(arr):
    """간단한 버블 정렬 (실무용)"""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 테스트해보기
print("\n=== 🫧 버블 정렬 테스트 ===")
test_data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(test_data.copy())

print("\n" + "="*50)

# 다양한 케이스 테스트
test_cases = [
    [5, 2, 8, 1, 9],
    [1, 2, 3, 4, 5],  # 이미 정렬된 경우
    [5, 4, 3, 2, 1],  # 역순 정렬
    [3, 3, 3, 3],     # 중복값
    [42]              # 단일 원소
]

print("📊 다양한 테스트 케이스:")
for i, case in enumerate(test_cases, 1):
    print(f"\n테스트 케이스 {i}: {case}")
    result = bubble_sort_simple(case.copy())
    print(f"결과: {result}")

print("\n" + "="*50)

print("🎯 버블 정렬 특징:")
print("✅ 장점: 구현 간단, 이해하기 쉬움")
print("❌ 단점: 느림 (O(n²)), 큰 데이터에 부적합")
print("🎪 용도: 학습용, 작은 데이터셋")
print("🚀 개선점: 최적화(이미 정렬된 경우 조기 종료)")

print("\n⏰ 시간 복잡도:")
print("- 최악의 경우: O(n²) - 역순으로 정렬된 경우")
print("- 최선의 경우: O(n) - 이미 정렬된 경우 (최적화 버전)")
print("- 평균: O(n²)")

print("\n🔄 알고리즘 사고 과정:")
print("1. 문제 정의: 배열을 오름차순으로 정렬하자")
print("2. 해결 전략: 옆끼리 비교해서 큰 것을 뒤로 보내자")
print("3. 반복 구조: 이 과정을 계속 반복하자")
print("4. 최적화: 불필요한 작업은 줄이자")

print("\n🎮 실습 과제:")
print("1. 왜 n-1 라운드만 하면 될까요?")
print("2. 각 라운드에서 비교 횟수가 줄어드는 이유는?")
print("3. 최적화가 왜 중요할까요?")

print("\n💡 다음에 배울 것: 선택 정렬!")
print("선택 정렬은 '가장 작은 것을 찾아서 앞으로' 방식이에요!")

print("\n✅ 버블 정렬 기초 완전 마스터!")