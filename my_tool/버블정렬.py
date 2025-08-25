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