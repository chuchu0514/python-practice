class MinHeap:
    def __init__(self):
        """힙 초기화"""
        self.heap = []
  
    
    def _parent_index(self, index):
        """부모 인덱스 계산"""
        return (index - 1) // 2
    
    def _left_child_index(self, index):
        """왼쪽 자식 인덱스 계산"""
        return 2 * index + 1
    
    def _right_child_index(self, index):
        """오른쪽 자식 인덱스 계산"""
        return 2 * index + 2
    
    def _has_parent(self, index):
        """부모가 있는지 확인"""
        return self._parent_index(index) >= 0
    
    def _has_left_child(self, index):
        """왼쪽 자식이 있는지 확인"""
        return self._left_child_index(index) < len(self.heap)
    
    def _has_right_child(self, index):
        """오른쪽 자식이 있는지 확인"""
        return self._right_child_index(index) < len(self.heap)
    
    def _parent(self, index):
        """부모 값 반환"""
        return self.heap[self._parent_index(index)]
    
    def _left_child(self, index):
        """왼쪽 자식 값 반환"""
        return self.heap[self._left_child_index(index)]
    
    def _right_child(self, index):
        """오른쪽 자식 값 반환"""
        return self.heap[self._right_child_index(index)]
    
    def _swap(self, index1, index2):
        """두 원소 위치 바꾸기"""
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def peek(self):
        """최솟값 확인 (제거하지 않음)"""
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def insert(self, item):
        """힙에 원소 추가"""
        self.heap.append(item)
        self._heapify_up()
        print(f"🔼 '{item}' 추가됨: {self.heap}")
    
    def _heapify_up(self):
        """위로 올라가면서 힙 속성 유지"""
        index = len(self.heap) - 1
        while (self._has_parent(index) and 
               self._parent(index) > self.heap[index]):
            self._swap(self._parent_index(index), index)
            index = self._parent_index(index)
    
    def extract_min(self):
        """최솟값 제거하고 반환"""
        if len(self.heap) == 0:
            print("힙이 비어있습니다!")
            return None
        
        item = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        del self.heap[len(self.heap) - 1]
        self._heapify_down()
        print(f"🔽 '{item}' 처리 완료: {self.heap}")
        return item
    
    def _heapify_down(self):
        """아래로 내려가면서 힙 속성 유지"""
        index = 0
        while self._has_left_child(index):
            smaller_child_index = self._left_child_index(index)
            if (self._has_right_child(index) and 
                self._right_child(index) < self._left_child(index)):
                smaller_child_index = self._right_child_index(index)
            
            if self.heap[index] < self.heap[smaller_child_index]:
                break
            else:
                self._swap(index, smaller_child_index)
            
            index = smaller_child_index
    
    def is_empty(self):
        """힙이 비었는지 확인"""
        return len(self.heap) == 0
    
    def size(self):
        """힙 크기 반환"""
        return len(self.heap)
    
    def show(self):
        """힙 상태 보여주기"""
        if self.is_empty():
            print("비어있습니다")
            return
        
        print(f"   현재 대상: {self.heap}")
        print(f"   다음 대상: {self.heap[0]}")
