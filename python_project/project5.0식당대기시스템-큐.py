import datetime

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

class RestaurantWaitingSystem:
    def __init__(self, restaurant_name="진성이네 맛집"):
        self.restaurant_name = restaurant_name
        # TODO: 테이블별 웨이팅 큐 생성
        # 힌트: 딕셔너리로 {"2인석": Queue(), "4인석": Queue(), "6인석": Queue()}
        self.waiting_queue = {
            "2인석": Queue(),
            "4인석": Queue(),
            "6인석": Queue()    
        }
        
        # TODO: 웨이팅 번호 관리
        # 힌트: self.waiting_number = 1
        self.waiting_number = 1
        # TODO: 오늘 통계 데이터
        # 힌트: 총 접수 고객, 서비스 완료 고객 등
        self.total_customer = 0
        self.served_customer = 0 
        print(f"🍽️ {restaurant_name} 웨이팅 시스템 시작!")
        print("=" * 50)
    
    def get_total_waiting(self):
        return (self.waiting_queue["2인석"].size() + 
                self.waiting_queue["4인석"].size() + 
                self.waiting_queue["6인석"].size())

    def get_table_type_by_people(self, people_count):
        if people_count <= 2:
            return "2인석"
        elif people_count <= 4:
            return "4인석"
        else:
            return "6인석"
    
    def show_menu(self):
        """메인 메뉴 표시"""
        print(f"\n=== {self.restaurant_name} 웨이팅 시스템 ===")
        print("1. 웨이팅 접수")
        print("2. 고객 호출")
        print("3. 대기 현황 확인")
        print("4. 웨이팅 취소")
        print("5. 오늘 통계")
        print("6. 시스템 종료")
        print("=" * 40)
    
    def register_waiting(self):
        """웨이팅 접수"""
        name = input("이름: ")
        phone = input("전화번호: ")
        while True:
            try:
                people = int(input("인원: "))
                if people <= 0:
                    print("최소 1명이어야 합니다.")
                    pass
                else:
                    break
            except ValueError:
                print("숫자만 입력하세요.")

        now = datetime.datetime.now()    

        waiting_status = {
            "번호": self.waiting_number, 
            "이름": name, 
            "인원": people, 
            "연락처": phone, 
            "접수시간": now
        }  
        # TODO: 고객 정보 입력받기
        # - 대표자 이름
        # - 인원수 (2명, 4명, 6명 이상 선택)
        # - 연락처
        
        # TODO: 인원수에 따른 테이블 타입 결정
        # 2명 → "2인석", 3-4명 → "4인석", 5명 이상 → "6인석"

        table_type = self.get_table_type_by_people(people)
        self.waiting_queue[table_type].enqueue(waiting_status)
        self.waiting_number += 1
        self.total_customer += 1


            

        # TODO: 웨이팅 정보 객체 생성
        # 힌트: {"번호": self.waiting_number, "이름": name, "인원": people, "연락처": phone, "접수시간": 현재시간}
        
        # TODO: 해당 테이블 큐에 추가
        
        # TODO: 웨이팅 번호 증가
        
        # TODO: 접수 완료 메시지 + 현재 대기 팀 수 + 예상 대기시간
    
    def call_customer(self):
        """고객 호출 (테이블 준비됨)"""
        # TODO: 어떤 테이블이 비었는지 선택 받기
        # "1. 2인석  2. 4인석  3. 6인석"
        while True:
            choice = input("1. 2인석  2. 4인석  3. 6인석: ")
            if choice == "1":
                if self.waiting_queue["2인석"].is_empty():
                    print("대기 중인 손님이 없습니다.")
                    return
                next_customer = self.waiting_queue["2인석"].dequeue()
                print(f"{next_customer['이름']}님 주문 도와드리겠습니다.")
                self.served_customer += 1
                break
            elif choice == "2":
                if self.waiting_queue["4인석"].is_empty():
                    print("대기 중인 손님이 없습니다.")
                    return
                next_customer = self.waiting_queue["4인석"].dequeue()
                print(f"{next_customer['이름']}님 주문 도와드리겠습니다.")
                self.served_customer += 1
                break

            elif choice == "3":
                if self.waiting_queue["6인석"].is_empty():
                    print("대기 중인 손님이 없습니다.")
                    return
                next_customer = self.waiting_queue["6인석"].dequeue()
                print(f"{next_customer['이름']}님 주문 도와드리겠습니다.")
                self.served_customer += 1
                break

            else: 
                print("유효한 숫자를 입력해주세요.")
        # TODO: 해당 테이블 큐에서 다음 고객 호출
        
        # TODO: 큐가 비어있으면 "대기 고객 없음" 메시지
        
        # TODO: 호출 성공시 고객 정보 표시 + "📞 문자 발송" 시뮬레이션
       
    def show_waiting_status(self):
        """대기 현황 확인"""
        # TODO: 테이블별 대기 현황 표시
        # 예시:
        # 🪑 2인석: 3팀 대기 (예상 대기시간: 45분)
        #   1. 김철수님 (2명) - 15분 전 접수
        #   2. 이영희님 (2명) - 10분 전 접수  
        #   3. 박민수님 (2명) - 5분 전 접수
        for table_type, queue in self.waiting_queue.items():
            if queue.size() > 0:
                print(f"🪑 {table_type}: {queue.size()}팀 대기")
                for customer in queue.items:
                    print(f"  {customer['번호']}. {customer['이름']}님 ({customer['인원']}명)")
            else:
                print(f"🪑 {table_type}: 대기 없음")
    
        print(f"\n📊 총 대기: {self.get_total_waiting()}팀")
        # TODO: 전체 대기 팀 수와 예상 대기시간
    
    def cancel_waiting(self):
        """웨이팅 취소"""
        # TODO: 취소할 웨이팅 번호 입력받기
        self.show_waiting_status()
        choice = input("취소할 웨이팅 번호를 입력해주세요: ")
        target_number = int(choice)

        # 모든 테이블에서 찾기
        for table_type, queue in self.waiting_queue.items():
            for customer in queue.items:
                if customer["번호"] == target_number:
                    name = customer["이름"]
                    temp_queue = Queue()
                    for customer in self.waiting_queue[table_type].items:
                        temp_queue.enqueue(customer)
                    temp2_queue = Queue()
                    count = int(choice) - self.served_customer 
                    for i in range(count):
                        delete = temp_queue.dequeue()
                        if i == count - 1:
                            continue
                        temp2_queue.enqueue(delete)
                    while not temp_queue.is_empty():
                        delete = temp_queue.dequeue()
                        temp2_queue.enqueue(delete)
                    self.waiting_queue[table_type] = temp2_queue
                    if name:  # name이 정의됐는지 체크
                        print(f"{name}님 취소 완료")
                    else:
                        print("취소 완료")
                    return
        print("번호가 존재하지 않습니다.")

        # TODO: 모든 테이블 큐에서 해당 번호 찾아서 제거
        # 힌트: 큐에서 특정 항목 제거는 까다로움. 임시 큐 활용 필요
        
        # TODO: 취소 완료/실패 메시지

    
    def show_daily_statistics(self):
        """오늘 통계"""
        # TODO: 오늘 접수된 총 고객 수
        
        # TODO: 서비스 완료된 고객 수
        
        # TODO: 현재 대기 중인 고객 수
        
        # TODO: 테이블별 이용 현황
        
        # TODO: 평균 대기시간 (선택사항)
        pass
    
    def calculate_estimated_waiting_time(self, table_type):
        """예상 대기시간 계산"""
        # TODO: 테이블별 평균 식사시간 가정
        # 2인석: 60분, 4인석: 90분, 6인석: 120분
        
        # TODO: 앞에 대기하는 팀 수 * 평균 식사시간
        
        # TODO: 분 단위로 반환
        pass
    


def main():
    """메인 실행 함수"""
    system = RestaurantWaitingSystem("진성이네 삼겹살집")
    
    while True:
        system.show_menu()
        choice = input("메뉴를 선택하세요: ")
        
        if choice == '1':
            system.register_waiting()
        elif choice == '2':
            system.call_customer()
        elif choice == '3':
            system.show_waiting_status()
        elif choice == '4':
            system.cancel_waiting()
        elif choice == '5':
            system.show_daily_statistics()
        elif choice == '6':
            print("🍽️ 오늘도 수고하셨습니다!")
            break
        else:
            print("❌ 올바른 메뉴를 선택해주세요!")
        
        input("\n계속하려면 Enter를 누르세요...")

if __name__ == "__main__":
    main()