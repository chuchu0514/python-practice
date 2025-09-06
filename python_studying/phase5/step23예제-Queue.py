# 📚 큐(Queue) 자료구조 완전 가이드

print("=== 📚 큐란 무엇인가? ===")
print("큐 = 줄서기!")
print("- First In First Out (FIFO)")
print("- 먼저 들어간 것이 먼저 나옴")
print("- 뒤에서 넣고, 앞에서 빼기")

print("\n💡 실생활 예시:")
print("🏪 카페 줄서기: 먼저 온 사람이 먼저 주문")
print("🖨️ 프린터: 먼저 인쇄 요청한 문서부터 출력")
print("🏥 병원 대기: 먼저 접수한 환자부터 진료")

print("\n" + "="*40)

# 1. 가장 간단한 큐 - 리스트로 만들기
print("1. 가장 간단한 큐 만들기")

queue = []  # 빈 큐

print(f"초기 큐: {queue}")

# 큐에 데이터 추가 (enqueue) - 뒤에서 넣기
queue.append("첫 번째 손님")
print(f"첫 번째 손님 도착: {queue}")

queue.append("두 번째 손님")
print(f"두 번째 손님 도착: {queue}")

queue.append("세 번째 손님")
print(f"세 번째 손님 도착: {queue}")

print(f"현재 줄서기 상태: {queue}")
print(f"맨 앞 손님: {queue[0]}")  # 첫 번째 원소 = 맨 앞

# 큐에서 데이터 제거 (dequeue) - 앞에서 빼기
served = queue.pop(0)  # 맨 앞에서 제거!
print(f"{served} 서비스 완료: {queue}")

served = queue.pop(0)
print(f"{served} 서비스 완료: {queue}")

served = queue.pop(0)
print(f"{served} 서비스 완료: {queue}")

print(f"모든 손님 서비스 완료: {queue}")

print("\n" + "="*40)

# 2. 스택 vs 큐 비교
print("2. 📊 스택 vs 큐 비교")

print("\n🥞 스택 (LIFO):")
stack = []
stack.append("접시1")
stack.append("접시2") 
stack.append("접시3")
print(f"스택에 쌓기: {stack}")
print(f"스택에서 빼기: {stack.pop()}")  # 접시3 (마지막 것)
print(f"남은 접시: {stack}")

print("\n🚶 큐 (FIFO):")
queue = []
queue.append("손님1")
queue.append("손님2")
queue.append("손님3") 
print(f"줄서기: {queue}")
print(f"서비스 완료: {queue.pop(0)}")  # 손님1 (첫 번째 것)
print(f"남은 줄: {queue}")

print("\n💡 핵심 차이:")
print("  스택: 마지막 → 먼저 나감 (LIFO)")
print("  큐:   첫 번째 → 먼저 나감 (FIFO)")

print("\n" + "="*40)

# 3. 제대로 된 큐 클래스 만들기
print("3. 큐 클래스 만들기")

class Queue:
    def __init__(self):
        """큐 초기화"""
        self.items = []
        print("🚶 새로운 줄서기 큐가 만들어졌습니다!")
    
    def enqueue(self, item):
        """큐에 원소 추가 (뒤에서 넣기)"""
        self.items.append(item)
        print(f"🔽 '{item}' 줄서기 참가: {self.items}")
    
    def dequeue(self):
        """큐에서 원소 제거 (앞에서 빼기)"""
        if self.is_empty():
            print("❌ 줄이 비어있어서 서비스할 사람이 없습니다!")
            return None
        
        item = self.items.pop(0)  # 맨 앞에서 제거
        print(f"🔼 '{item}' 서비스 완료: {self.items}")
        return item
    
    def front(self):
        """맨 앞 원소 확인하기 (제거하지 않음)"""
        if self.is_empty():
            print("❌ 줄이 비어있습니다!")
            return None
        return self.items[0]
    
    def is_empty(self):
        """큐가 비었는지 확인"""
        return len(self.items) == 0
    
    def size(self):
        """큐 크기 확인"""
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

# 큐 테스트해보기
print("\n=== 큐 클래스 테스트 ===")
my_queue = Queue()

print("\n--- 손님들이 줄서기 ---")
my_queue.enqueue("김철수")
my_queue.enqueue("이영희")
my_queue.enqueue("박민수")

print(f"\n다음 서비스 대상: {my_queue.front()}")
print(f"대기 중인 손님 수: {my_queue.size()}")

print("\n줄서기 상태:")
my_queue.show()

print("\n--- 손님 서비스하기 ---")
my_queue.dequeue()
my_queue.show()

my_queue.dequeue()
my_queue.show()

my_queue.dequeue()
my_queue.show()

# 빈 큐에서 서비스 시도
my_queue.dequeue()

print("\n" + "="*40)

# 4. 실생활 예시 - 카페 주문 시스템
print("4. 실생활 예시: 카페 주문 시스템")

class CafeOrderSystem:
    def __init__(self):
        self.order_queue = Queue()
        self.order_number = 1
        print("☕ 카페 주문 시스템 시작!")
    
    def take_order(self, customer_name, menu):
        """주문 받기"""
        order = {
            "number": self.order_number,
            "customer": customer_name,
            "menu": menu
        }
        
        self.order_queue.enqueue(f"#{self.order_number} {customer_name}({menu})")
        print(f"📝 주문 접수: #{self.order_number} {customer_name}님의 {menu}")
        self.order_number += 1
    
    def serve_order(self):
        """주문 서비스하기"""
        if self.order_queue.is_empty():
            print("👨‍🍳 서비스할 주문이 없습니다!")
            return
        
        completed_order = self.order_queue.dequeue()
        print(f"✅ 주문 완성: {completed_order}")
    
    def show_waiting_orders(self):
        """대기 중인 주문 보기"""
        print(f"\n📋 대기 중인 주문 ({self.order_queue.size()}개):")
        self.order_queue.show()

# 카페 시뮬레이션
print("\n=== 카페 시뮬레이션 ===")
cafe = CafeOrderSystem()

print("\n--- 주문 접수 ---")
cafe.take_order("진성", "아메리카노")
cafe.take_order("철수", "카페라떼") 
cafe.take_order("영희", "프라푸치노")
cafe.take_order("민수", "에스프레소")

cafe.show_waiting_orders()

print("\n--- 주문 서비스 ---")
cafe.serve_order()  # 진성 아메리카노
cafe.serve_order()  # 철수 카페라떼
cafe.show_waiting_orders()

cafe.serve_order()  # 영희 프라푸치노
cafe.serve_order()  # 민수 에스프레소
cafe.show_waiting_orders()

cafe.serve_order()  # 더 이상 주문 없음

print("\n" + "="*40)

# 5. 실전 문제 - 프린터 대기열
print("5. 실전 문제: 프린터 대기열 시스템")

class PrinterQueue:
    def __init__(self):
        self.print_queue = Queue()
        self.job_id = 1
        print("🖨️ 프린터 대기열 시스템 시작!")
    
    def add_print_job(self, user, document, pages):
        """인쇄 작업 추가"""
        job = f"Job#{self.job_id} {user}({document}, {pages}p)"
        self.print_queue.enqueue(job)
        print(f"📄 인쇄 작업 추가: {job}")
        self.job_id += 1
    
    def process_print_job(self):
        """인쇄 작업 처리"""
        if self.print_queue.is_empty():
            print("🖨️ 인쇄할 작업이 없습니다!")
            return
        
        current_job = self.print_queue.dequeue()
        print(f"🖨️ 인쇄 중: {current_job}")
    
    def show_print_queue(self):
        """대기열 상태 보기"""
        print(f"\n📋 인쇄 대기열 ({self.print_queue.size()}개 작업):")
        self.print_queue.show()

# 프린터 시뮬레이션
print("\n=== 프린터 시뮬레이션 ===")
printer = PrinterQueue()

print("\n--- 인쇄 작업 추가 ---")
printer.add_print_job("진성", "과제보고서", 10)
printer.add_print_job("교수님", "시험문제", 5)
printer.add_print_job("동기", "논문", 50)

printer.show_print_queue()

print("\n--- 인쇄 작업 처리 ---")
printer.process_print_job()  # 진성 과제보고서
printer.process_print_job()  # 교수님 시험문제
printer.show_print_queue()

printer.process_print_job()  # 동기 논문
printer.process_print_job()  # 더 이상 작업 없음

print("\n" + "="*40)

# 6. 큐의 특징 정리
print("6. 📋 큐의 특징 정리")

features = [
    "✅ FIFO (First In, First Out) - 먼저 들어간 게 먼저 나옴",
    "✅ enqueue() - 데이터 추가 (뒤에서)",
    "✅ dequeue() - 데이터 제거 (앞에서)",
    "✅ front() - 맨 앞 데이터 확인 (제거하지 않음)",
    "✅ is_empty() - 비었는지 확인",
    "✅ size() - 크기 확인"
]

for feature in features:
    print(f"  {feature}")

print(f"\n💡 큐 활용 예시:")
use_cases = [
    "☕ 카페/식당 주문 시스템",
    "🖨️ 프린터 작업 대기열",
    "🏥 병원 대기 번호표",
    "🎮 게임 매칭 시스템",
    "🌐 웹서버 요청 처리",
    "🔍 BFS(너비우선탐색) 알고리즘",
    "💬 채팅 메시지 처리",
    "📱 앱 푸시 알림 시스템"
]

for use_case in use_cases:
    print(f"  {use_case}")

print(f"\n🎯 큐 vs 스택 언제 사용?")
comparison = [
    "📌 큐 사용: 순서대로 처리해야 할 때 (공정성 중요)",
    "📌 스택 사용: 가장 최근 것부터 처리할 때 (실행취소 등)",
    "📌 큐 = 줄서기 (먼저 온 사람부터)",
    "📌 스택 = 접시쌓기 (위에 있는 것부터)"
]

for item in comparison:
    print(f"  {item}")

print("\n✅ 큐 기초 완전 마스터!")