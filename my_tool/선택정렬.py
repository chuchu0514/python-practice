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
