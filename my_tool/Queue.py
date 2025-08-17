class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def front(self):
        if self.is_empty():
            return None
        return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def show(self):
        """큐 상태 예쁘게 보여주기"""
        if self.is_empty():
            print("🚶 빈 줄")
            return
        
        print("🚶 현재 줄서기 상태:")
        for i, item in enumerate(self.items):
            if i == 0:
                print(f"   [{item}] ← 맨 앞 (다음 서비스)")
            else:
                print(f"   [{item}]")
        print("   ^^^^^^^ 줄 끝")