# 🎯 BST 실습 문제

print("=== 🌳 BST 실습 문제 ===")
print("BST 클래스를 완성하고 고급 기능들을 구현해보세요!")

# 🎯 BST 실습 난이도 (1-10점)
# 문제 1: 기본 연산 → 4점 (재귀 패턴 익히기)
# 문제 2: 최솟값/최댓값 → 3점 (단순 탐색)
# 문제 3: 삭제 연산 → 8점 (3케이스, 가장 복잡!)
# 문제 4: BST 검증 → 6점 (범위 체크 사고력)
# 문제 5: 범위 검색 → 7점 (최적화 고려)
# 문제 6: 고급 기능 → 5점 (응용이지만 패턴 있음)
# 추천 순서: 1 → 2 → 4 → 6 → 5 → 3
# (삭제는 마지막에!)
 
# BST 노드 클래스 (완성된 것 사용)
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 문제 1: BST 기본 연산 완성하기 (4점)
print("📝 문제 1: BST 기본 클래스 완성하기")
print("난이도: 4점")
print("목표: BST의 핵심 연산들을 직접 구현")

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """BST에 데이터 삽입"""
        if self.root is None:
            self.root = BSTNode(data)
        else:
            return self._insert_helper(self.root, data)
            
    
    def _insert_helper(self, node, data):
        """삽입을 도와주는 재귀 함수"""
        # TODO: 현재 노드와 비교해서 왼쪽/오른쪽에 삽입
        # 힌트: 
        # - data < node.data면 왼쪽으로
        # - data > node.data면 오른쪽으로  
        # - 자식이 None이면 새 노드 생성, 아니면 재귀 호출
        # - data == node.data면 중복이므로 무시
        if data < node.data:
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self._insert_helper(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self._insert_helper(node.right, data)

    def search(self, data):
        """BST에서 데이터 검색"""
        # TODO: 재귀 또는 반복문으로 데이터 찾기
        # 힌트: 현재 노드와 비교해서 왼쪽/오른쪽으로 이동

        result = self._search_helper(self.root, data)
        return result

    def _search_helper(self, node, data):
        """검색을 도와주는 재귀 함수"""
        # TODO: 재귀로 데이터 찾기
        # 힌트: node가 None이면 False, data 찾으면 True, 작으면 왼쪽, 크면 오른쪽
        if node is None:
            return False
        
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_helper(node.left, data)
        else:
            return self._search_helper(node.right, data)
    
    def inorder_traversal(self):
        """중위 순회 (정렬된 결과)"""
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _inorder_helper(self, node, result):
        """중위 순회 도우미"""
        # TODO: 왼쪽 → 현재 → 오른쪽 순서로 방문
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append(node.data)
            self._inorder_helper(node.right, result)

# 기본 연산 테스트
print("\n=== 문제 1 테스트 ===")
bst = BST()
test_data = [5, 3, 8, 2, 4, 7, 9, 1]

print("삽입 테스트:")
for data in test_data:
    bst.insert(data)
    print(f"  {data} 삽입")

print(f"\n중위 순회 결과: {bst.inorder_traversal()}")
print("예상 결과: [1, 2, 3, 4, 5, 7, 8, 9] (정렬됨)")

print("\n검색 테스트:")
for target in [1, 5, 6, 9, 10]:
    result = bst.search(target)
    print(f"  {target}: {'찾음' if result else '없음'}")

print("\n" + "="*60)

# 문제 2: 최솟값/최댓값 찾기 (3점)
print("📝 문제 2: 최솟값/최댓값 찾기")
print("난이도: 3점")
print("목표: BST의 특성을 이용해서 효율적으로 최솟값/최댓값 찾기")

class BSTAdvanced(BST):
    def find_min(self):
        """최솟값 찾기 (가장 왼쪽 노드)"""
        # TODO: 가장 왼쪽 노드의 값 반환
        # 힌트: 왼쪽 자식이 없을 때까지 계속 이동
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data
        
    
    def find_max(self):
        """최댓값 찾기 (가장 오른쪽 노드)"""
        # TODO: 가장 오른쪽 노드의 값 반환
        # 힌트: 오른쪽 자식이 없을 때까지 계속 이동
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data
        
    
    def find_kth_smallest(self, k):
        """k번째로 작은 값 찾기"""
        # TODO: 중위 순회를 이용해서 k번째 원소 찾기
        # 힌트: 중위 순회 결과에서 k-1 인덱스 (0부터 시작)
        result = self.inorder_traversal()
        return result[k-1]
    
    def find_successor(self, data):
        """특정 값의 successor(다음으로 큰 값) 찾기"""
        # TODO: 어려운 문제! 도전 과제
        # 힌트: 중위 순회에서 data 다음에 오는 값
        result = self.inorder_traversal()
        left = 0
        right = len(result) - 1
        while left <= right:
            mid = (left + right) // 2
            if result[mid] == data:
                if mid + 1 < len(result):
                    return result[mid + 1]
                else:
                    return None
            elif result[mid] > data:
                right = mid - 1
            else:
                left = mid + 1
        return None

# 테스트
print("\n=== 문제 2 테스트 ===")
bst_adv = BSTAdvanced()
for data in [5, 3, 8, 2, 4, 7, 9, 1, 6]:
    bst_adv.insert(data)

print(f"최솟값: {bst_adv.find_min()}")  # 1
print(f"최댓값: {bst_adv.find_max()}")  # 9
print(f"정렬 : {bst_adv.inorder_traversal()}")
print(f"3번째로 작은 값: {bst_adv.find_kth_smallest(3)}")  # 3
print(f"5의 successor: {bst_adv.find_successor(5)}")  # 6

print("\n" + "="*60)

# 문제 3: BST 삭제 연산 (8점)
print("📝 문제 3: BST 삭제 연산 구현하기")
print("난이도: 8점")
print("목표: BST에서 노드를 삭제하는 복잡한 알고리즘 구현")
print("케이스 1: 잎 노드 삭제")
print("케이스 2: 자식이 1개인 노드 삭제")
print("케이스 3: 자식이 2개인 노드 삭제 (가장 복잡!)")

class BSTWithDelete(BSTAdvanced):
    def delete(self, data):
        """BST에서 데이터 삭제"""
        self.root = self._delete_helper(self.root, data)
    
    def _delete_helper(self, node, data):
        """삭제를 도와주는 재귀 함수"""
        # TODO: 3가지 케이스를 모두 처리해야 함!
        
        # 1단계: 삭제할 노드 찾기
        # 2단계: 3가지 케이스 처리
        # 케이스 1: 잎 노드 (자식 0개)
        # 케이스 2: 자식이 1개
        # 케이스 3: 자식이 2개 (successor 찾아서 교체)
        pass
    
    def _find_min_node(self, node):
        """서브트리에서 최솟값 노드 찾기"""
        # TODO: 가장 왼쪽 노드 반환
        pass

# 삭제 테스트
print("\n=== 문제 3 테스트 ===")
bst_del = BSTWithDelete()
for data in [5, 3, 8, 2, 4, 7, 9, 1, 6]:
    bst_del.insert(data)

print(f"삭제 전: {bst_del.inorder_traversal()}")

# 케이스 1: 잎 노드 삭제
bst_del.delete(1)
print(f"1 삭제 후: {bst_del.inorder_traversal()}")

# 케이스 2: 자식 1개 노드 삭제  
bst_del.delete(2)
print(f"2 삭제 후: {bst_del.inorder_traversal()}")

# 케이스 3: 자식 2개 노드 삭제
bst_del.delete(5)
print(f"5 삭제 후: {bst_del.inorder_traversal()}")

print("\n" + "="*60)

# 문제 4: BST 검증하기 (6점)
print("📝 문제 4: BST 검증 함수")
print("난이도: 6점")
print("목표: 주어진 트리가 올바른 BST인지 검증")
print("함정 주의: 바로 옆 자식만 비교하면 안됨!")

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """BST가 올바른지 검증"""
    # TODO: 재귀로 BST 규칙 검증
    # 힌트: 각 노드는 min_val < node.data < max_val 범위에 있어야 함
    # 왼쪽 서브트리: max_val을 현재 노드 값으로 제한
    # 오른쪽 서브트리: min_val을 현재 노드 값으로 제한
    if root is None:
        return True
    if not (min_val < root.data < max_val):
        return False
    
    # 🔥 핵심: 범위를 제대로 전달!
    left_valid = is_valid_bst(root.left, min_val, root.data)      # 왼쪽: max를 현재값으로 제한
    right_valid = is_valid_bst(root.right, root.data, max_val)   # 오른쪽: min을 현재값으로 제한
    
    return left_valid and right_valid

def is_valid_bst_simple(root):
    """중위 순회를 이용한 간단한 검증"""
    # TODO: 중위 순회 결과가 정렬되어 있는지 확인
    # 힌트: 중위 순회 결과를 sorted()와 비교
    if root is None:
        return True
    def _inorder_help(node, result):
        if node is None:
            return 
        _inorder_help(node.left, result)
        result.append(node.data)
        _inorder_help(node.right, result)
    result = []
    _inorder_help(root, result)
    return result == sorted(result)

# 테스트용 트리들 생성
print("\n=== 문제 4 테스트 ===")

# 올바른 BST
correct_bst = BSTNode(5)
correct_bst.left = BSTNode(3)
correct_bst.right = BSTNode(8)
correct_bst.left.left = BSTNode(2)
correct_bst.left.right = BSTNode(4)

# 잘못된 BST (함정!)
wrong_bst = BSTNode(5)
wrong_bst.left = BSTNode(3)
wrong_bst.right = BSTNode(8)
wrong_bst.left.left = BSTNode(2)
wrong_bst.left.right = BSTNode(6)  # 잘못됨! 5보다 크면 안됨

print(f"올바른 BST 검증: {is_valid_bst(correct_bst)}")  # True
print(f"올바른 BST 검증 (간단): {is_valid_bst_simple(correct_bst)}")  # True

print(f"잘못된 BST 검증: {is_valid_bst(wrong_bst)}")  # False  
print(f"잘못된 BST 검증 (간단): {is_valid_bst_simple(wrong_bst)}")  # False

print("\n" + "="*60)

# 문제 5: 범위 검색 (7점)
print("📝 문제 5: 범위 검색 구현하기")
print("난이도: 7점")
print("목표: 특정 범위에 속하는 모든 값 찾기")

class BSTRangeSearch(BSTWithDelete):
    def range_search(self, min_val, max_val):
        """min_val 이상 max_val 이하인 모든 값 반환"""
        # TODO: 범위에 속하는 값들을 효율적으로 찾기
        # 힌트: 중위 순회를 사용하되, 범위 밖 서브트리는 탐색하지 않도록 최적화
        result = []
        self._range_search_helper(self.root, min_val, max_val, result)
        return result
    
    def _range_search_helper(self, node, min_val, max_val, result):
        """범위 검색 도우미 함수"""
        # TODO: 최적화된 범위 검색 구현
        # 힌트: 
        # - 현재 노드가 범위에 속하면 결과에 추가
        # - 왼쪽 서브트리 탐색 (현재 노드가 min_val보다 크면)
        # - 오른쪽 서브트리 탐색 (현재 노드가 max_val보다 작으면)
        pass
    
    def count_in_range(self, min_val, max_val):
        """범위에 속하는 노드 개수 반환"""
        # TODO: 범위에 속하는 노드 개수만 세기
        pass
    
    def sum_in_range(self, min_val, max_val):
        """범위에 속하는 값들의 합 반환"""
        # TODO: 범위에 속하는 값들의 합 계산
        pass

# 범위 검색 테스트
print("\n=== 문제 5 테스트 ===")
bst_range = BSTRangeSearch()
for data in [5, 3, 8, 2, 4, 7, 9, 1, 6]:
    bst_range.insert(data)

print(f"전체 데이터: {bst_range.inorder_traversal()}")
print(f"3~7 범위: {bst_range.range_search(3, 7)}")  # [3, 4, 5, 6, 7]
print(f"1~5 범위: {bst_range.range_search(1, 5)}")  # [1, 2, 3, 4, 5]
print(f"6~10 범위: {bst_range.range_search(6, 10)}")  # [6, 7, 8, 9]

print(f"3~7 범위 개수: {bst_range.count_in_range(3, 7)}")  # 5
print(f"3~7 범위 합: {bst_range.sum_in_range(3, 7)}")  # 25

print("\n" + "="*60)

# 문제 6: BST 고급 기능 (5점)
print("📝 문제 6: BST 고급 기능들")
print("난이도: 5점")
print("목표: BST의 고급 기능들을 구현해보기")

class BSTMaster(BSTRangeSearch):
    def height(self):
        """BST 높이 계산"""
        # TODO: 트리의 높이 반환
        if self.root is None:
            return -1
        return self._height_helper(self.root)
    
    def _height_helper(self, node):
        # TODO: 재귀로 높이 계산
        if node is None:
            return -1
        left = self._height_helper(node.left)
        right = self._height_helper(node.right)
        height = max(left, right)
        return height + 1
    
    def is_balanced(self):
        """BST가 균형잡혀있는지 확인 (높이 차이 ≤ 1)"""
        # TODO: 모든 노드에서 왼쪽과 오른쪽 서브트리의 높이 차이가 1 이하인지 확인
        if self.root is None:
            return True
        def check_tree(node):
            if node is None:
                return True
            left = self._height_helper(node.left)
            right = self._height_helper(node.right)
            if abs(left - right) > 1:
                return False
            left_result = check_tree(node.left)
            right_result = check_tree(node.right)
            return left_result and right_result
        return check_tree(self.root)

            
    def get_level_order(self):
        """레벨 순서 순회 (BFS)"""
        # TODO: 큐를 사용해서 레벨별로 순회
        from collections import deque
        pass
    
    def mirror(self):
        """BST를 좌우 반전 (주의: BST 특성 깨짐!)"""
        # TODO: 모든 노드의 왼쪽과 오른쪽 자식을 바꾸기
        pass
    
    def lowest_common_ancestor(self, val1, val2):
        """두 값의 최소 공통 조상 찾기"""
        # TODO: BST 특성을 이용해서 효율적으로 LCA 찾기
        pass

# 고급 기능 테스트
print("\n=== 문제 6 테스트 ===")
bst_master = BSTMaster()
for data in [4, 2, 6, 1, 3, 5, 7]:
    bst_master.insert(data)

print(f"트리 데이터: {bst_master.inorder_traversal()}")
print(f"트리 높이: {bst_master.height()}")
print(f"균형 여부: {bst_master.is_balanced()}")
print(f"레벨 순서: {bst_master.get_level_order()}")
print(f"LCA(1, 3): {bst_master.lowest_common_ancestor(1, 3)}")  # 2
print(f"LCA(1, 7): {bst_master.lowest_common_ancestor(1, 7)}")  # 4

print("\n반전 전 중위 순회:", bst_master.inorder_traversal())
bst_master.mirror()
print("반전 후 중위 순회:", bst_master.inorder_traversal())
print("(주의: 반전 후에는 더 이상 올바른 BST가 아님!)")

print("\n" + "="*60)

# 종합 테스트
print("🎯 BST 실습 완료 후 체크리스트:")

checklist = [
    "□ 문제 1: BST 기본 연산 (삽입, 검색, 순회)",
    "□ 문제 2: 최솟값/최댓값/k번째 값 찾기",
    "□ 문제 3: 삭제 연산 (3가지 케이스)",
    "□ 문제 4: BST 검증 (올바른 BST인지 확인)",
    "□ 문제 5: 범위 검색 (특정 범위의 값들)",
    "□ 문제 6: 고급 기능 (높이, 균형, LCA 등)"
]

for item in checklist:
    print(f"  {item}")

print("\n💡 BST 마스터 포인트:")
tips = [
    "🎯 BST 규칙: 왼쪽 < 부모 < 오른쪽 (항상 기억!)",
    "🔥 삭제가 가장 복잡: 3가지 케이스 모두 이해",
    "⚡ 검색/삽입/삭제 모두 평균 O(log n)",
    "📊 중위 순회 = 정렬된 결과 (BST의 특별한 성질)",
    "⚖️ 균형이 중요: 한쪽으로 기울면 성능 저하",
    "🔍 범위 검색: BST의 강력한 응용",
    "🧠 재귀 사고: BST 알고리즘은 대부분 재귀"
]

for tip in tips:
    print(f"  {tip}")

print("\n🚀 다음 단계 예고:")
next_steps = [
    "🌟 균형 BST: AVL 트리, Red-Black 트리",
    "📊 그래프 알고리즘: DFS, BFS 본격 학습",
    "🎮 프로젝트: BST를 활용한 실전 응용",
    "⚡ 해시 테이블: 또 다른 검색 자료구조"
]

for step in next_steps:
    print(f"  {step}")

print("\n✨ BST 실습 준비 완료!")
print("🏆 이제 직접 구현해서 BST 전문가가 되어보세요!")

print("\n🎯 BST 실습 완료!")
print("다음은 그래프 알고리즘이 기다리고 있습니다! 🚀")