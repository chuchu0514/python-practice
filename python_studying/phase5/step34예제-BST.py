# 🌳 BST(Binary Search Tree) 완전 가이드

print("=== 🔍 BST란 무엇인가? ===")
print("BST = Binary Search Tree = 이진 탐색 트리")
print("📐 규칙: 왼쪽 < 부모 < 오른쪽")
print("🎯 목적: 검색, 삽입, 삭제를 빠르게! (O(log n))")
print("💡 핵심: 항상 정렬된 상태를 유지!")

print("\n" + "="*50)

# 1. BST와 일반 트리의 차이점
print("1. 일반 트리 vs BST 비교")

print("\n일반 트리 (아무 규칙 없음):")
print("      5")
print("     / \\")
print("    3   8")
print("   / \\ / \\")
print("  9  1 4  2")
print("→ 값 7을 찾으려면? 모든 노드 확인 필요! (최악 O(n))")

print("\nBST (왼쪽 < 부모 < 오른쪽):")
print("      5")
print("     / \\")
print("    3   8")
print("   / \\ / \\")
print("  1  4 7  9")
print("→ 값 7을 찾으려면? 5 → 8 → 7 (3번만!) (평균 O(log n))")

print("\n" + "="*50)

# 2. BST 노드 클래스
print("2. BST 노드 클래스 정의")

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

print("BST 노드 클래스:")
print("- data: 저장할 값")
print("- left: 왼쪽 자식 (현재 노드보다 작은 값들)")
print("- right: 오른쪽 자식 (현재 노드보다 큰 값들)")

print("\n" + "="*50)

# 3. BST 클래스와 기본 연산
print("3. BST 클래스 구현")

class BST:
    def __init__(self):
        self.root = None
        print("🌳 새로운 BST가 생성되었습니다!")
    
    def insert(self, data):
        """BST에 데이터 삽입"""
        print(f"\n🔼 {data} 삽입 시작...")
        if self.root is None:
            self.root = BSTNode(data)
            print(f"   루트 노드로 {data} 설정!")
        else:
            self._insert_recursive(self.root, data)
        print(f"✅ {data} 삽입 완료!")
    
    def _insert_recursive(self, node, data):
        """재귀적으로 적절한 위치에 삽입"""
        if data < node.data:
            print(f"   {data} < {node.data}, 왼쪽으로 이동")
            if node.left is None:
                node.left = BSTNode(data)
                print(f"   왼쪽 자식으로 {data} 삽입!")
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            print(f"   {data} > {node.data}, 오른쪽으로 이동")
            if node.right is None:
                node.right = BSTNode(data)
                print(f"   오른쪽 자식으로 {data} 삽입!")
            else:
                self._insert_recursive(node.right, data)
        else:
            print(f"   {data}는 이미 존재합니다! (중복 불허)")
    
    def search(self, data):
        """BST에서 데이터 검색"""
        print(f"\n🔍 {data} 검색 시작...")
        result = self._search_recursive(self.root, data)
        if result:
            print(f"✅ {data}를 찾았습니다!")
        else:
            print(f"❌ {data}를 찾지 못했습니다!")
        return result
    
    def _search_recursive(self, node, data):
        """재귀적으로 데이터 검색"""
        if node is None:
            print(f"   끝에 도달, {data} 없음")
            return False
        
        print(f"   현재 노드: {node.data}")
        
        if data == node.data:
            print(f"   찾았다! {data}")
            return True
        elif data < node.data:
            print(f"   {data} < {node.data}, 왼쪽으로 이동")
            return self._search_recursive(node.left, data)
        else:
            print(f"   {data} > {node.data}, 오른쪽으로 이동")
            return self._search_recursive(node.right, data)
    
    def inorder_traversal(self):
        """중위 순회 (정렬된 결과!)"""
        print("\n📋 중위 순회 (왼쪽 → 루트 → 오른쪽):")
        result = []
        self._inorder_recursive(self.root, result)
        print(f"   결과: {result}")
        print("   → BST의 중위 순회는 항상 정렬된 순서!")
        return result
    
    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)
    
    def find_min(self):
        """최솟값 찾기 (가장 왼쪽)"""
        if self.root is None:
            return None
        
        current = self.root
        print(f"\n🔽 최솟값 찾기: {current.data}에서 시작")
        
        while current.left is not None:
            current = current.left
            print(f"   왼쪽으로 이동: {current.data}")
        
        print(f"✅ 최솟값: {current.data}")
        return current.data
    
    def find_max(self):
        """최댓값 찾기 (가장 오른쪽)"""
        if self.root is None:
            return None
        
        current = self.root
        print(f"\n🔼 최댓값 찾기: {current.data}에서 시작")
        
        while current.right is not None:
            current = current.right
            print(f"   오른쪽으로 이동: {current.data}")
        
        print(f"✅ 최댓값: {current.data}")
        return current.data
    
    def show_structure(self):
        """BST 구조 시각화"""
        print("\n🌳 현재 BST 구조:")
        if self.root is None:
            print("   (빈 트리)")
        else:
            self._print_tree(self.root, "", True)
    
    def _print_tree(self, node, prefix, is_last):
        """트리 구조를 예쁘게 출력"""
        if node is not None:
            print(prefix + ("└── " if is_last else "├── ") + str(node.data))
            children = []
            if node.left is not None:
                children.append((node.left, False))
            if node.right is not None:
                children.append((node.right, True))
            
            for i, (child, is_child_last) in enumerate(children):
                extension = "    " if is_last else "│   "
                self._print_tree(child, prefix + extension, is_child_last and i == len(children) - 1)

print("\n" + "="*50)

# 4. BST 실제 사용해보기
print("4. BST 실제 동작 확인")

# BST 생성
bst = BST()

# 데이터 삽입 테스트
print("\n--- 데이터 삽입 테스트 ---")
test_data = [5, 3, 8, 2, 4, 7, 9]
print(f"삽입할 데이터: {test_data}")

for data in test_data:
    bst.insert(data)
    bst.show_structure()

# 검색 테스트
print("\n--- 검색 테스트 ---")
search_targets = [4, 6, 9, 10]
for target in search_targets:
    bst.search(target)

# 순회 결과 확인
bst.inorder_traversal()

# 최솟값/최댓값 찾기
bst.find_min()
bst.find_max()

print("\n" + "="*50)

# 5. BST vs 다른 자료구조 성능 비교
print("5. 성능 비교")

performance_table = """
📊 연산별 시간복잡도 비교:

연산        | 배열(정렬)  | 연결리스트  | BST(평균)  | BST(최악)
------------|-------------|-------------|------------|----------
검색(Search)| O(log n)    | O(n)        | O(log n)   | O(n)
삽입(Insert)| O(n)        | O(n)        | O(log n)   | O(n)
삭제(Delete)| O(n)        | O(n)        | O(log n)   | O(n)
최솟값      | O(1)        | O(n)        | O(log n)   | O(n)
최댓값      | O(1)        | O(n)        | O(log n)   | O(n)

💡 BST의 장점:
✅ 검색이 빠름 (평균 O(log n))
✅ 삽입/삭제가 빠름 (평균 O(log n))
✅ 정렬된 순서로 데이터 접근 가능
✅ 범위 검색이 효율적

⚠️ BST의 단점:
❌ 최악의 경우 O(n) (일직선 트리)
❌ 균형이 깨지면 성능 저하
❌ 추가 메모리 필요 (포인터)
"""

print(performance_table)

print("\n" + "="*50)

# 6. 실생활 활용 예시
print("6. BST 실생활 활용 사례")

print("\n🏪 전화번호부 시스템")
class PhoneBook:
    def __init__(self):
        self.bst = BST()
        print("📞 전화번호부 시스템 시작!")
    
    def add_contact(self, name, phone):
        # 실제로는 name을 키로 하는 BST
        # 간단히 name을 ASCII 값으로 변환
        key = sum(ord(c) for c in name.lower())
        print(f"연락처 추가: {name} ({phone}) → 키: {key}")
        self.bst.insert(key)
    
    def search_contact(self, name):
        key = sum(ord(c) for c in name.lower())
        print(f"연락처 검색: {name} → 키: {key}")
        return self.bst.search(key)

phonebook = PhoneBook()
phonebook.add_contact("김철수", "010-1234-5678")
phonebook.add_contact("이영희", "010-2345-6789")
phonebook.add_contact("박민수", "010-3456-7890")

phonebook.search_contact("이영희")
phonebook.search_contact("최영수")

print("\n🎮 게임 순위 시스템")
class GameRanking:
    def __init__(self):
        self.bst = BST()
        print("🏆 게임 순위 시스템 시작!")
    
    def add_score(self, score):
        print(f"점수 추가: {score}")
        self.bst.insert(score)
    
    def get_rankings(self):
        print("🥇 현재 순위 (높은 점수부터):")
        scores = self.bst.inorder_traversal()
        scores.reverse()  # 내림차순으로
        for i, score in enumerate(scores, 1):
            print(f"   {i}위: {score}점")

ranking = GameRanking()
ranking.add_score(850)
ranking.add_score(920)
ranking.add_score(780)
ranking.add_score(950)
ranking.add_score(820)
ranking.get_rankings()

print("\n" + "="*50)

# 7. BST 심화 개념 미리보기
print("7. 심화 개념 (다음에 배울 내용)")

advanced_concepts = """
🔥 고급 BST 개념들:

1. 🗑️ 삭제 연산 (복잡!)
   - 잎 노드 삭제: 간단
   - 자식 1개 노드 삭제: 중간
   - 자식 2개 노드 삭제: 복잡! (successor 찾기)

2. ⚖️ 균형 BST
   - AVL 트리: 높이 차이 ≤ 1 유지
   - Red-Black 트리: 색칠 규칙으로 균형
   - 목적: 최악 O(n) 방지

3. 🔍 범위 검색
   - 특정 범위의 모든 값 찾기
   - 예: 80점 이상 90점 이하 학생들

4. 🌳 트리 순회 응용
   - 전위: 트리 복사
   - 중위: 정렬된 출력
   - 후위: 트리 삭제

5. 📊 BST 검증
   - 주어진 트리가 올바른 BST인지 확인
   - 함정: 바로 옆 자식만 비교하면 안됨!
"""

print(advanced_concepts)

print("\n" + "="*50)

# 8. BST 마스터 체크리스트
print("8. 🎯 BST 마스터 체크리스트")

checklist = [
    "✅ BST 규칙 이해: 왼쪽 < 부모 < 오른쪽",
    "✅ 삽입 알고리즘: 재귀적 위치 찾기",
    "✅ 검색 알고리즘: 비교하며 한쪽으로 이동",
    "✅ 중위 순회: 정렬된 결과 얻기",
    "✅ 최솟값/최댓값: 가장 왼쪽/오른쪽",
    "🔲 삭제 알고리즘: 3가지 케이스 처리",
    "🔲 BST 검증: 올바른 BST인지 확인",
    "🔲 범위 검색: 특정 범위의 값들 찾기",
    "🔲 균형 트리: AVL, Red-Black 이해"
]

for item in checklist:
    print(f"  {item}")

print(f"\n💡 다음 실습에서 삭제와 검증을 구현해보세요!")

print("\n" + "="*50)

# 9. 재미있는 BST 퀴즈
print("9. 🧩 BST 퀴즈 (생각해보세요!)")

quiz_questions = """
❓ 퀴즈 1: 다음 순서로 삽입했을 때 BST 모양은?
   삽입 순서: [1, 2, 3, 4, 5]
   힌트: 최악의 경우...

❓ 퀴즈 2: BST에서 중위 순회 결과가 [1, 3, 5, 7, 9]일 때
   전위 순회 결과를 유일하게 결정할 수 있을까?

❓ 퀴즈 3: 1000개 노드가 완전히 균형잡힌 BST에서
   검색에 필요한 최대 비교 횟수는?
   힌트: log₂(1000) = ?

❓ 퀴즈 4: BST에서 두 번째로 작은 값을 찾는 효율적인 방법은?
   힌트: 최솟값 다음...
"""

print(quiz_questions)

print("\n답은 실습에서 확인해보세요! 🚀")

print("\n" + "="*50)

print("🎉 BST 기초 완전 정복!")
print("📚 핵심 요약:")
print("  - BST = 검색이 빠른 정렬된 트리")
print("  - 삽입/검색/삭제 모두 평균 O(log n)")
print("  - 중위 순회 = 정렬된 결과")
print("  - 실무에서 DB 인덱스, 검색 엔진 등에 활용")
print("")
print("🔥 다음 단계: BST 실습 문제 도전!")
print("   삭제 연산, BST 검증, 고급 기능들을 직접 구현해보세요!")