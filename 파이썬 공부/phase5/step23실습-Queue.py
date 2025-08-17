# 🎯 큐 실습 문제

print("=== 📚 큐 실습 문제 ===")
print("큐 클래스를 활용해서 문제를 해결해보세요!")

# 큐 클래스 (이미 완성된 것 사용)
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

print("\n" + "="*50)

# 문제 1: 은행 번호표 시스템
print("📝 문제 1: 은행 번호표 시스템")
print("고객이 번호표를 뽑고, 순서대로 업무를 처리하는 시스템")
print("기능: 번호표 발급, 다음 고객 호출, 대기 인원 확인")

class BankTicketSystem:
    def __init__(self):
        self.queue = Queue()
        self.ticket_number = 1
        print("🏦 은행 번호표 시스템 시작!")
    
    def issue_ticket(self, customer_name):
        """번호표 발급"""
        # TODO: 현재 번호와 고객명으로 표 만들기
        # TODO: 큐에 추가
        # TODO: 번호 증가
        # TODO: 발급 메시지 출력
        pass
    
    def call_next_customer(self):
        """다음 고객 호출"""
        # TODO: 큐가 비어있으면 "대기 고객 없음" 메시지
        # TODO: 큐에서 다음 고객 꺼내기
        # TODO: 호출 메시지 출력
        pass
    
    def show_waiting_list(self):
        """대기 명단 보기"""
        # TODO: 대기 중인 고객 수 출력
        # TODO: 다음 순서 고객 이름 출력 (front() 사용)
        pass

# 테스트
print("\n=== 은행 번호표 시스템 테스트 ===")
bank = BankTicketSystem()

print("\n--- 번호표 발급 ---")
bank.issue_ticket("김철수")
bank.issue_ticket("이영희")
bank.issue_ticket("박민수")
bank.issue_ticket("최진성")

print("\n--- 대기 현황 확인 ---")
bank.show_waiting_list()

print("\n--- 고객 호출 ---")
bank.call_next_customer()  # 1번 김철수
bank.call_next_customer()  # 2번 이영희
bank.show_waiting_list()

bank.call_next_customer()  # 3번 박민수
bank.call_next_customer()  # 4번 최진성
bank.call_next_customer()  # 더 이상 고객 없음

print("\n" + "="*50)

# 문제 2: 메시지 처리 시스템 (채팅)
print("📝 문제 2: 실시간 채팅 메시지 처리 시스템")
print("메시지가 도착한 순서대로 처리하는 시스템")
print("기능: 메시지 수신, 메시지 처리, 대기 중인 메시지 확인")

class ChatMessageProcessor:
    def __init__(self):
        self.message_queue = Queue()
        print("💬 채팅 메시지 처리 시스템 시작!")
    
    def receive_message(self, sender, message):
        """메시지 수신"""
        # TODO: "sender: message" 형태로 큐에 추가
        # TODO: 수신 메시지 출력
        pass
    
    def process_message(self):
        """메시지 처리 (화면에 표시)"""
        # TODO: 큐가 비어있으면 "처리할 메시지 없음"
        # TODO: 큐에서 메시지 꺼내서 처리
        # TODO: 처리 완료 메시지 출력
        pass
    
    def show_pending_messages(self):
        """대기 중인 메시지 확인"""
        # TODO: 대기 중인 메시지 개수 출력
        # TODO: 다음 처리할 메시지 출력 (front() 사용)
        pass

# 테스트
print("\n=== 채팅 메시지 처리 시스템 테스트 ===")
chat = ChatMessageProcessor()

print("\n--- 메시지 수신 ---")
chat.receive_message("진성", "안녕하세요!")
chat.receive_message("철수", "반가워요")
chat.receive_message("영희", "오늘 날씨 좋네요")
chat.receive_message("민수", "점심 뭐 드실 건가요?")

print("\n--- 대기 중인 메시지 ---")
chat.show_pending_messages()

print("\n--- 메시지 처리 ---")
chat.process_message()  # 진성 메시지
chat.process_message()  # 철수 메시지
chat.show_pending_messages()

chat.process_message()  # 영희 메시지
chat.process_message()  # 민수 메시지
chat.process_message()  # 더 이상 메시지 없음

print("\n" + "="*50)

# 문제 3: 웹서버 요청 처리 시스템
print("📝 문제 3: 웹서버 요청 처리 시스템")
print("사용자 요청을 순서대로 처리하는 시스템")
print("기능: 요청 접수, 요청 처리, 서버 상태 확인")

class WebServerRequestHandler:
    def __init__(self, max_capacity=5):
        self.request_queue = Queue()
        self.max_capacity = max_capacity
        self.request_id = 1
        print(f"🌐 웹서버 시작! (최대 대기: {max_capacity}개 요청)")
    
    def handle_request(self, user_ip, request_type):
        """요청 처리"""
        # TODO: 최대 용량 체크 (큐 크기가 max_capacity 이상이면 거부)
        # TODO: 요청 ID, 사용자 IP, 요청 타입으로 요청 객체 생성
        # TODO: 큐에 추가
        # TODO: 요청 ID 증가
        # TODO: 접수 또는 거부 메시지 출력
        pass
    
    def process_request(self):
        """요청 처리"""
        # TODO: 큐가 비어있으면 "처리할 요청 없음"
        # TODO: 큐에서 요청 꺼내서 처리
        # TODO: 처리 완료 메시지 출력
        pass
    
    def show_server_status(self):
        """서버 상태 확인"""
        # TODO: 현재 대기 중인 요청 수 출력
        # TODO: 다음 처리할 요청 정보 출력
        # TODO: 서버 용량 상태 출력 (몇 % 사용 중인지)
        pass

# 테스트
print("\n=== 웹서버 요청 처리 시스템 테스트 ===")
server = WebServerRequestHandler(max_capacity=3)

print("\n--- 요청 접수 ---")
server.handle_request("192.168.1.100", "GET /home")
server.handle_request("192.168.1.101", "POST /login")
server.handle_request("192.168.1.102", "GET /profile")
server.handle_request("192.168.1.103", "GET /search")  # 용량 초과로 거부되어야 함

print("\n--- 서버 상태 확인 ---")
server.show_server_status()

print("\n--- 요청 처리 ---")
server.process_request()  # 첫 번째 요청
server.show_server_status()

server.process_request()  # 두 번째 요청
server.process_request()  # 세 번째 요청
server.process_request()  # 더 이상 요청 없음

print("\n" + "="*50)

# 문제 4: 게임 매칭 시스템
print("📝 문제 4: 온라인 게임 매칭 시스템")
print("플레이어들을 순서대로 매칭시키는 시스템")
print("기능: 매칭 대기, 게임 시작, 대기열 확인")

class GameMatchingSystem:
    def __init__(self, players_per_game=4):
        self.waiting_queue = Queue()
        self.players_per_game = players_per_game
        self.game_id = 1
        print(f"🎮 게임 매칭 시스템 시작! (게임당 {players_per_game}명)")
    
    def join_queue(self, player_name, level):
        """매칭 대기열 참가"""
        # TODO: 플레이어 정보(이름, 레벨) 큐에 추가
        # TODO: 대기열 참가 메시지 출력
        # TODO: 자동으로 매칭 체크 (check_for_match 호출)
        pass
    
    def check_for_match(self):
        """매칭 가능한지 체크하고 게임 시작"""
        # TODO: 대기 중인 플레이어가 게임 정원보다 많거나 같으면
        # TODO: 정원만큼 플레이어를 큐에서 빼서 게임 시작
        # TODO: 게임 ID 증가
        pass
    
    def show_queue_status(self):
        """대기열 상태 확인"""
        # TODO: 현재 대기 중인 플레이어 수 출력
        # TODO: 게임 시작까지 몇 명 더 필요한지 출력
        # TODO: 다음 순서 플레이어 정보 출력
        pass

# 테스트
print("\n=== 게임 매칭 시스템 테스트 ===")
matching = GameMatchingSystem(players_per_game=3)  # 3명이면 게임 시작

print("\n--- 플레이어 대기열 참가 ---")
matching.join_queue("진성", 25)
matching.show_queue_status()

matching.join_queue("철수", 30)
matching.show_queue_status()

matching.join_queue("영희", 28)  # 이때 게임 시작되어야 함
matching.show_queue_status()

matching.join_queue("민수", 35)
matching.join_queue("지영", 22)
matching.join_queue("현우", 40)  # 이때 또 게임 시작
matching.show_queue_status()

print("\n" + "="*50)

print("🎯 실습 완료 후 체크리스트:")
checklist = [
    "✅ 문제 1: 번호표 시스템이 순서대로 잘 동작하나요?",
    "✅ 문제 2: 메시지가 도착 순서대로 처리되나요?", 
    "✅ 문제 3: 서버 용량 제한이 잘 동작하나요?",
    "✅ 문제 4: 정원이 차면 자동으로 게임이 시작되나요?"
]

for item in checklist:
    print(item)

print("\n💡 막히는 부분이 있으면 언제든 질문하세요!")
print("📚 큐의 FIFO 원리를 잘 활용하는 게 핵심입니다!")
print("🔥 다음 단계: 큐 중심 프로젝트 - 병원 대기 시스템!")