# 🎯 힙 실습 문제

print("=== 📚 힙 실습 문제 ===")
print("힙 클래스를 활용해서 문제를 해결해보세요!")

# 힙 클래스 (이미 완성된 것 사용 - 예제에서 가져오기)
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def _parent_index(self, index):
        return (index - 1) // 2
    
    def _left_child_index(self, index):
        return 2 * index + 1
    
    def _right_child_index(self, index):
        return 2 * index + 2
    
    def _has_parent(self, index):
        return self._parent_index(index) >= 0
    
    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)
    
    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)
    
    def _parent(self, index):
        return self.heap[self._parent_index(index)]
    
    def _left_child(self, index):
        return self.heap[self._left_child_index(index)]
    
    def _right_child(self, index):
        return self.heap[self._right_child_index(index)]
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def insert(self, item):
        self.heap.append(item)
        self._heapify_up()
    
    def _heapify_up(self):
        index = len(self.heap) - 1
        while (self._has_parent(index) and 
               self._parent(index) > self.heap[index]):
            self._swap(self._parent_index(index), index)
            index = self._parent_index(index)
    
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        
        item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        if len(self.heap) > 0:
            self._heapify_down()
        return item
    
    def _heapify_down(self):
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
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)

print("\n" + "="*50)

# 문제 1: 응급실 환자 관리 시스템
print("📝 문제 1: 응급실 환자 관리 시스템")
print("환자들을 위급도 순서로 진료하는 시스템을 만들어보세요")
print("기능: 환자 접수, 다음 환자 호출, 대기 환자 확인")

class EmergencyRoom:
    def __init__(self):
        # TODO: 우선순위 큐(힙) 생성
        # TODO: 환자 번호 관리
        print("🏥 응급실 시스템 시작!")
    
    def register_patient(self, name, urgency_level):
        """환자 접수 (urgency_level: 1=매우위급, 5=가벼움)"""
        # TODO: (우선순위, 환자번호, 이름) 튜플을 힙에 추가
        # TODO: 환자 번호 증가
        # TODO: 접수 메시지 출력
        pass
    
    def call_next_patient(self):
        """다음 환자 호출"""
        # TODO: 힙이 비어있으면 "대기 환자 없음" 메시지
        # TODO: 가장 위급한 환자를 힙에서 꺼내기
        # TODO: 호출 메시지 출력
        pass
    
    def show_waiting_patients(self):
        """대기 중인 환자 확인"""
        # TODO: 대기 중인 환자 수 출력
        # TODO: 다음 진료 대상 출력 (peek() 사용)
        pass

# 테스트
print("\n=== 응급실 시스템 테스트 ===")
er = EmergencyRoom()

print("\n--- 환자 접수 ---")
er.register_patient("김철수", 3)  # 골절
er.register_patient("이영희", 1)  # 심장마비
er.register_patient("박민수", 5)  # 감기
er.register_patient("최진성", 2)  # 호흡곤란

print("\n--- 대기 현황 ---")
er.show_waiting_patients()

print("\n--- 환자 진료 ---")
er.call_next_patient()  # 이영희 (우선순위 1)
er.call_next_patient()  # 최진성 (우선순위 2)
er.show_waiting_patients()

print("\n" + "="*50)

# 문제 2: 작업 스케줄러
print("📝 문제 2: 작업 스케줄러 시스템")
print("컴퓨터 작업들을 우선순위 순서로 처리하는 시스템")
print("기능: 작업 추가, 작업 실행, 대기열 확인")

class TaskScheduler:
    def __init__(self):
        # TODO: 우선순위 큐 생성
        print("💻 작업 스케줄러 시작!")
    
    def add_task(self, task_name, priority, estimated_time):
        """작업 추가 (priority: 낮을수록 높은 우선순위)"""
        # TODO: (우선순위, 작업명, 예상시간) 튜플을 힙에 추가
        # TODO: 추가 메시지 출력
        pass
    
    def execute_next_task(self):
        """다음 작업 실행"""
        # TODO: 힙이 비어있으면 "실행할 작업 없음"
        # TODO: 가장 높은 우선순위 작업 실행
        # TODO: 실행 메시지 출력
        pass
    
    def show_task_queue(self):
        """작업 대기열 확인"""
        # TODO: 대기 중인 작업 수 출력
        # TODO: 다음 실행 작업 출력
        # TODO: 전체 대기 시간 계산 (모든 작업의 예상시간 합계)
        pass

# 테스트
print("\n=== 작업 스케줄러 테스트 ===")
scheduler = TaskScheduler()

print("\n--- 작업 추가 ---")
scheduler.add_task("이메일 전송", 3, 2)
scheduler.add_task("데이터 백업", 1, 30)  # 높은 우선순위
scheduler.add_task("보고서 작성", 5, 10)
scheduler.add_task("보안 검사", 2, 15)

print("\n--- 대기열 확인 ---")
scheduler.show_task_queue()

print("\n--- 작업 실행 ---")
scheduler.execute_next_task()  # 데이터 백업 (우선순위 1)
scheduler.execute_next_task()  # 보안 검사 (우선순위 2)
scheduler.show_task_queue()

print("\n" + "="*50)

# 문제 3: 상위 K개 원소 찾기
print("📝 문제 3: 상위 K개 점수 찾기")
print("학생들의 점수에서 상위 K명의 점수를 찾는 시스템")

def find_top_k_scores(scores, k):
    """상위 K개 점수 반환"""
    # TODO: 최대힙을 만들어야 하는데, MinHeap밖에 없음
    # 힌트: 점수에 -1을 곱해서 저장하면 최소힙이 최대힙처럼 동작!
    # TODO: 모든 점수를 힙에 추가 (-score로 변환해서)
    # TODO: K번 extract_min 해서 상위 K개 추출
    # TODO: 결과에서 다시 -1을 곱해서 원래 점수로 복원
    pass

# 테스트
print("\n=== 상위 K개 점수 찾기 테스트 ===")
student_scores = [85, 92, 78, 96, 88, 75, 91, 83, 97, 80]
print(f"전체 점수: {student_scores}")

top_3 = find_top_k_scores(student_scores, 3)
print(f"상위 3개 점수: {top_3}")  # [97, 96, 92] 순서로 나와야 함

top_5 = find_top_k_scores(student_scores, 5)
print(f"상위 5개 점수: {top_5}")

print("\n" + "="*50)

# 문제 4: 실시간 중간값 찾기 (도전 문제!)
print("📝 문제 4: 실시간 중간값 추적기 (도전!)")
print("숫자가 하나씩 들어올 때마다 현재까지의 중간값을 구하는 시스템")
print("힌트: 최대힙과 최소힙 두 개를 사용해야 함!")

class MedianTracker:
    def __init__(self):
        # TODO: 작은 절반을 저장하는 최대힙 (음수로 변환)
        # TODO: 큰 절반을 저장하는 최소힙
        print("📊 중간값 추적기 시작!")
    
    def add_number(self, num):
        """숫자 추가"""
        # TODO: 두 힙의 크기를 비슷하게 유지하면서 숫자 추가
        # TODO: 최대힙의 최댓값 ≤ 최소힙의 최솟값 유지
        pass
    
    def get_median(self):
        """현재 중간값 반환"""
        # TODO: 두 힙의 크기가 같으면 두 힙의 루트 평균
        # TODO: 크기가 다르면 큰 힙의 루트
        pass

# 테스트 (도전 문제라서 힌트만 제공)
print("\n=== 중간값 추적기 테스트 ===")
tracker = MedianTracker()

numbers = [5, 15, 1, 3, 8, 7, 9, 2, 6]
for num in numbers:
    tracker.add_number(num)
    print(f"숫자 {num} 추가 → 중간값: {tracker.get_median()}")

print("\n" + "="*50)

print("🎯 실습 완료 후 체크리스트:")
checklist = [
    "✅ 문제 1: 응급실에서 위급도 순서로 환자 호출이 되나요?",
    "✅ 문제 2: 작업이 우선순위 순서로 실행되나요?", 
    "✅ 문제 3: 상위 K개가 올바르게 찾아지나요?",
    "✅ 문제 4: 중간값이 실시간으로 정확히 계산되나요? (도전!)"
]

for item in checklist:
    print(item)

print("\n💡 막히는 부분이 있으면 언제든 질문하세요!")
print("📚 힙의 우선순위 원리를 잘 활용하는 게 핵심입니다!")
print("🔥 다음 단계: 정렬 알고리즘 마스터!")