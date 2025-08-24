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

class StockTradingSystem:

    def __init__(self, stock_name= "이더리움"):
        # TODO: 매수 주문 힙 (높은 가격 우선)
        # TODO: 매도 주문 힙 (낮은 가격 우선) 
        # TODO: 주문 번호 관리
        self.stock_name = stock_name 
        self.buy_heap = MinHeap()
        self.sell_heap = MinHeap()
        self.order_id = 1
        print(f"📈 {stock_name} 거래 시스템 시작!")
        
    def place_buy_order(self, price, quantity, trader_name): 
        # TODO: 매수 주문 접수
        self.buy_heap.insert((-price, quantity, trader_name, self.order_id))
        print(f"주문 번호{self.order_id}. {self.stock_name}을 {price}원에 {quantity}개 매수 주문.")
        self.order_id += 1

    def place_sell_order(self, price, quantity, trader_name):  
        # TODO: 매도 주문 접수
        self.sell_heap.insert((price, quantity, trader_name, self.order_id))
        print(f"주문 번호{self.order_id}. {self.stock_name}을 {price}원에 {quantity}개 매도 주문.")
        self.order_id += 1
        
    def show_order_book(self):
        # TODO: 현재 호가창 보기 (매수/매도 상위 5개씩)
        print(f"=== {self.stock_name} 호가창 ===")
        print("매수 상위 5개 목록")
        buy_temp = []
        if self.buy_heap.size() == 0:
            print("매수 주문 없음.")
        else:
            for i in range(min(5, self.buy_heap.size())):
                order = self.buy_heap.extract_min()
                buy_temp.append(order)
                print(f"주문 번호{order[3]}. {-order[0]} {order[1]}개 매수 주문.")
            for order in buy_temp:
                self.buy_heap.insert(order)
        print("매도 상위 5개 목록")
        sell_temp = []
        if self.sell_heap.size() == 0:
            print("매도 주문 없음.")
        else:   
            for i in range(min(5, self.sell_heap.size())):
                order = self.sell_heap.extract_min()
                sell_temp.append(order)
                print(f"주문 번호{order[3]}. {order[0]} {order[1]}개 매도 주문.")
            for order in sell_temp:
                self.sell_heap.insert(order)

        
    def cancel_order(self, order_id, order_type):
        if order_type == "매수":
            temp = MinHeap()
            found = False
            
            while not self.buy_heap.is_empty():
                order = self.buy_heap.extract_min()
                _, _, _, id = order
                if id != order_id:
                    temp.insert(order)
                else:
                    found = True
            
            self.buy_heap = temp
            
            if found:
                print("주문 취소 완료!")
            else:
                print("해당 주문을 찾을 수 없습니다.")
        elif order_type == "매도":
            temp = MinHeap()
            found = False
            
            while not self.sell_heap.is_empty():
                order = self.sell_heap.extract_min()
                _, _, _, id = order
                if id != order_id:
                    temp.insert(order)
                else:
                    found = True
            
            self.sell_heap = temp
            
            if found:
                print("주문 취소 완료!")
            else:
                print("해당 주문을 찾을 수 없습니다.")


def main():
    eth = StockTradingSystem("이더리움")

    while True:
        print("1. 매수 주문  2. 매도 주문  3. 호가창  4. 주문취소 5. 종료")
        choice = input("선택: ")
        
        if choice == '1':
            price = int(input("매수 가격: "))
            quantity = int(input("수량: "))
            name = input("이름: ")
            eth.place_buy_order(price, quantity, name)
        elif choice == '2':
            price = int(input("매도 가격: "))
            quantity = int(input("수량: "))
            name = input("이름: ")
            eth.place_sell_order(price, quantity, name)
        elif choice == '3':
            eth.show_order_book()
        elif choice == '4':
            order_id = int(input("주문 번호:"))
            order_type =(input('"매수", "매도" 중 택일'))
            eth.cancel_order(order_id, order_type)
        elif choice == '5':
            break
        else:
            print("올바른 수를 입력하세요.")
        

if __name__ == "__main__":
    main()
    print("종료합니다.")