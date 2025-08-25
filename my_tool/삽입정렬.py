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