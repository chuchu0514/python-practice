# 📚 힙(Heap) 자료구조 완전 가이드

print("=== 📚 힙이란 무엇인가? ===")
print("힙 = 응급실 환자 우선순위!")
print("- Priority First Out")
print("- 우선순위가 높은 것이 먼저 나옴")
print("- 완전 이진 트리 구조, 배열로 구현")

print("\n💡 실생활 예시:")
print("🏥 응급실: 위급한 환자부터 치료")
print("🎮 게임: 스킬 쿨타임 관리")
print("💻 운영체제: CPU 프로세스 스케줄링")
print("🗺️ 내비게이션: 최단 경로 찾기")

print("\n" + "="*40)

# 1. 일반 리스트 vs 힙 비교
print("1. 일반 리스트 vs 힙 비교")

print("\n🏥 응급실 상황 - 일반 리스트 방식:")
patients = ["감기환자", "골절환자", "심장마비환자"]
print(f"접수 순서: {patients}")
next_patient = patients.pop(0)  # 첫 번째 환자
print(f"다음 진료: {next_patient}")  # 감기환자 😱
print("문제: 심장마비 환자가 나중에...")

print("\n🏥 응급실 상황 - 힙 방식:")
import heapq
priority_queue = [(5, "감기환자"), (1, "심장마비환자"), (3, "골절환자")]
heapq.heapify(priority_queue)
print(f"우선순위 큐: {priority_queue}")
next_priority, next_patient = heapq.heappop(priority_queue)
print(f"다음 진료: {next_patient} (우선순위: {next_priority})")  # 심장마비환자 ✅
print("해결: 우선순위에 따라 자동 정렬!")

print("\n" + "="*40)

# 2. 힙의 구조 이해하기
print("2. 힙의 구조")

print("\n📊 최소힙 트리 구조:")
print("""
       1
     /   \\
    3     6
   / \\   /
  5   9 8

배열 표현: [1, 3, 6, 5, 9, 8]
인덱스:    [0, 1, 2, 3, 4, 5]
""")

print("🔗 부모-자식 관계 공식:")
print("- 인덱스 i의 부모: (i-1)//2")
print("- 인덱스 i의 왼쪽 자식: 2*i+1")
print("- 인덱스 i의 오른쪽 자식: 2*i+2")

# 실제 확인해보기
heap_array = [1, 3, 6, 5, 9, 8]
for i in range(len(heap_array)):
    parent_idx = (i-1)//2 if i > 0 else "없음"
    left_child_idx = 2*i+1 if 2*i+1 < len(heap_array) else "없음"
    right_child_idx = 2*i+2 if 2*i+2 < len(heap_array) else "없음"
    
    print(f"인덱스 {i} (값: {heap_array[i]})")
    print(f"  부모: {parent_idx}")
    print(f"  왼쪽 자식: {left_child_idx}")
    print(f"  오른쪽 자식: {right_child_idx}")

print("\n" + "="*40)

# 3. 최소힙 클래스 구현
print("3. 최소힙 클래스 만들기")

class MinHeap:
    def __init__(self):
        """힙 초기화"""
        self.heap = []
        print("🏥 새로운 응급실 시스템이 시작됩니다!")
    
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
            print("❌ 응급실이 비어있습니다!")
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
            print("🏥 응급실이 비어있습니다")
            return
        
        print(f"🏥 현재 대기 환자: {self.heap}")
        print(f"   다음 진료 대상: {self.heap[0]} (가장 위급)")

# 힙 테스트
print("\n=== 최소힙 테스트 ===")
emergency_room = MinHeap()

print("\n--- 환자 접수 ---")
emergency_room.insert(5)  # 감기 (우선순위: 5)
emergency_room.insert(3)  # 골절 (우선순위: 3)
emergency_room.insert(8)  # 두통 (우선순위: 8)
emergency_room.insert(1)  # 심장마비 (우선순위: 1)

emergency_room.show()

print("\n--- 환자 진료 ---")
emergency_room.extract_min()  # 1 (심장마비)
emergency_room.extract_min()  # 3 (골절)
emergency_room.show()

emergency_room.extract_min()  # 5 (감기)
emergency_room.extract_min()  # 8 (두통)
emergency_room.extract_min()  # 빈 응급실

print("\n" + "="*40)

# 4. 실생활 예시 - 게임 스킬 시스템
print("4. 실생활 예시: 게임 스킬 쿨타임 시스템")

class SkillCooldownManager:
    def __init__(self):
        self.cooldowns = MinHeap()
        self.current_time = 0
        print("🎮 스킬 쿨타임 시스템 시작!")
    
    def use_skill(self, skill_name, cooldown_time):
        """스킬 사용 (쿨타임 등록)"""
        ready_time = self.current_time + cooldown_time
        self.cooldowns.insert((ready_time, skill_name))
        print(f"⚡ {skill_name} 사용! {cooldown_time}초 후 재사용 가능")
    
    def update_time(self, time):
        """시간 업데이트 및 준비된 스킬 확인"""
        self.current_time = time
        print(f"\n⏰ 현재 시간: {self.current_time}초")
        
        while (not self.cooldowns.is_empty() and 
               self.cooldowns.peek()[0] <= self.current_time):
            ready_time, skill_name = self.cooldowns.extract_min()
            print(f"✅ {skill_name} 재사용 가능!")
    
    def show_cooldowns(self):
        """현재 쿨타임 상태 보기"""
        if self.cooldowns.is_empty():
            print("🎯 모든 스킬 사용 가능!")
        else:
            print("⏳ 쿨타임 중인 스킬들:")
            for ready_time, skill in self.cooldowns.heap:
                remaining = max(0, ready_time - self.current_time)
                print(f"   {skill}: {remaining}초 남음")

# 게임 시뮬레이션
print("\n=== 게임 스킬 시뮬레이션 ===")
game = SkillCooldownManager()

print("\n--- 스킬 사용 ---")
game.use_skill("파이어볼", 5)
game.use_skill("힐링", 3)
game.use_skill("순간이동", 8)
game.use_skill("방패", 2)

game.show_cooldowns()

print("\n--- 시간 경과 ---")
game.update_time(2)  # 2초 후
game.show_cooldowns()

game.update_time(5)  # 5초 후
game.show_cooldowns()

game.update_time(10) # 10초 후
game.show_cooldowns()

print("\n" + "="*40)

# 5. 파이썬 heapq 모듈
print("5. 파이썬 내장 heapq 모듈")

import heapq

print("\n🐍 파이썬의 heapq 사용법:")
numbers = [5, 3, 8, 1, 9, 2]
print(f"원본 리스트: {numbers}")

heapq.heapify(numbers)  # 힙으로 변환
print(f"힙으로 변환: {numbers}")

heapq.heappush(numbers, 0)  # 0 추가
print(f"0 추가 후: {numbers}")

smallest = heapq.heappop(numbers)  # 최솟값 제거
print(f"최솟값 {smallest} 제거 후: {numbers}")

print(f"현재 최솟값: {numbers[0]}")

print("\n💡 heapq 활용 팁:")
tips = [
    "✅ heapq는 최소힙만 지원",
    "✅ 최대힙 필요시 음수로 변환해서 사용",
    "✅ 튜플 사용시 첫 번째 요소로 우선순위 결정",
    "✅ heappush, heappop, heapify 함수가 핵심"
]

for tip in tips:
    print(f"  {tip}")

print("\n" + "="*40)

# 6. 힙의 특징 정리
print("6. 📋 힙의 특징 정리")

features = [
    "✅ 우선순위 기반 처리 (Priority First)",
    "✅ 삽입: O(log n) - 트리 높이만큼",
    "✅ 삭제: O(log n) - 재정렬 필요",
    "✅ 최솟값 확인: O(1) - 루트가 항상 최솟값",
    "✅ 완전 이진 트리 구조",
    "✅ 배열로 효율적 구현 가능"
]

for feature in features:
    print(f"  {feature}")

print(f"\n💡 힙 활용 예시:")
use_cases = [
    "🏥 응급실 환자 우선순위 관리",
    "🎮 게임 이벤트 스케줄링",
    "💻 운영체제 프로세스 스케줄링",
    "🗺️ 다익스트라 최단경로 알고리즘",
    "📊 상위 K개 원소 찾기",
    "⏰ 타이머/알람 시스템",
    "🔄 데이터 스트림에서 중간값 찾기"
]

for use_case in use_cases:
    print(f"  {use_case}")

print(f"\n🎯 언제 힙을 사용할까?")
comparison = [
    "📌 큐: 공정성 중요 (선착순)",
    "📌 스택: 최근 것 우선 (실행취소)",
    "📌 힙: 우선순위 중요 (응급상황)"
]

for item in comparison:
    print(f"  {item}")

print("\n✅ 힙 기초 완전 마스터!")