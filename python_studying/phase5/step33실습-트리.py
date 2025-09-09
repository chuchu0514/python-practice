# 🎯 트리 실습 문제

print("=== 🌳 트리 실습 문제 ===")
print("예제를 보고 직접 구현해보세요!")
print("힌트만 주어지므로 스스로 생각해서 코드 작성하기!")

# 기본 이진 트리 노드 클래스 (완성된 것 사용)
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

print("\n" + "="*60)

# 문제 1: 트리 기본 연산 (🥉 브론즈 4-5 난이도)
print("📝 문제 1: 이진 트리 기본 연산 구현하기")
print("난이도: 🥉 브론즈 4-5")
print("목표: BinaryTree 클래스에 기본 메서드들 추가하기")

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert_root(self, data):
        """루트 노드 삽입 (이미 구현됨)"""
        if self.root is None:
            self.root = BinaryTreeNode(data)
            print(f"루트 노드 '{data}' 삽입됨")
        else:
            print("루트가 이미 존재합니다!")
    
    def count_nodes(self):
        """트리의 총 노드 개수 구하기"""
        # TODO: 재귀를 사용해서 전체 노드 개수 계산
        # 힌트: 루트가 None이면 0, 아니면 1 + 왼쪽 서브트리 노드 수 + 오른쪽 서브트리 노드 수
        return self._count_helper(self.root)
    def _count_helper(self, node):
        """실제 카운팅 담당 (노드를 받아서 처리)"""
        # 여기서 node는 BinaryTreeNode 객체
        # TODO: 이 부분을 네가 구현해봐!
        # 힌트: node가 None이면? 아니면?
        if node is None:
            return 0
        
        count = 1
        left_count = self._count_helper(node.left)
        right_count = self._count_helper(node.right)

        return count + left_count + right_count

    def get_height(self):
        """트리의 높이 구하기"""  
        # TODO: 재귀를 사용해서 트리 높이 계산
        # 힌트: 루트가 None이면 -1, 아니면 max(왼쪽 높이, 오른쪽 높이) + 1
        return self._height_helper(self.root)
    
    def _height_helper(self, node):
        if node is None:
            return -1  # 빈 트리
        
        # 왼쪽 서브트리 높이 구하기
        left_height = self._height_helper(node.left)
        
        # 오른쪽 서브트리 높이 구하기  
        right_height = self._height_helper(node.right)
        
        # 더 높은 쪽을 선택하고 +1
        return max(left_height, right_height) + 1

    def count_leaves(self):
        """잎 노드(leaf) 개수 구하기"""
        # TODO: 자식이 없는 노드들의 개수 계산
        # 힌트: 왼쪽과 오른쪽 자식이 모두 None인 노드가 잎 노드
        return self._count_leaves_helper(self.root)
    
    def _count_leaves_helper(self, node):
        if node is None:
            return 0  # 빈 노드는 잎 0개
        
        # 현재 노드가 잎 노드인가?
        if node.left is None and node.right is None:
            return 1  # 잎 노드 1개!
        
        # 아니면 왼쪽 + 오른쪽 잎 개수
        left_count = self._count_leaves_helper(node.left)
        right_count = self._count_leaves_helper(node.right)
        return left_count + right_count
        


# 테스트용 트리 만들기
tree = BinaryTree()
tree.insert_root(1)
tree.root.left = BinaryTreeNode(2)
tree.root.right = BinaryTreeNode(3)
tree.root.left.left = BinaryTreeNode(4)
tree.root.left.right = BinaryTreeNode(5)

print("테스트할 트리:")
print("    1")
print("   / \\")
print("  2   3") 
print(" / \\")
print("4   5")


print(f"노드 개수: {tree.count_nodes()}")  # 예상 결과: 5
print(f"트리 높이: {tree.get_height()}")   # 예상 결과: 2  
print(f"잎 노드 개수: {tree.count_leaves()}") # 예상 결과: 3 (4, 5, 3)

print("\n" + "="*60)

# 문제 2: 트리 순회 구현 (🥉 브론즈 2-3 난이도)
print("📝 문제 2: 트리 순회 직접 구현하기")
print("난이도: 🥉 브론즈 2-3")
print("목표: 전위/중위/후위 순회를 깔끔하게 구현")

class TreeTraversal:
    def __init__(self, root):
        self.root = root
    
    def preorder(self, node, result=None):
        """전위 순회: Root → Left → Right"""
        # TODO: 전위 순회 구현
        # 힌트: 1. 현재 노드 방문 2. 왼쪽 재귀 3. 오른쪽 재귀
        # 주의: result 리스트 초기화 문제 해결하기
        if result is None:
            result = []
        if node is None:
            return result

        result.append(node.data)

        if node.left:
            self.preorder(node.left, result)

        if node.right:
            self.preorder(node.right, result)

        return result
    
    def inorder(self, node, result=None):
        """중위 순회: Left → Root → Right"""
        # TODO: 중위 순회 구현  
        # 힌트: 1. 왼쪽 재귀 2. 현재 노드 방문 3. 오른쪽 재귀
        if result is None:
            result = []
        if node is None:
            return result


        if node.left:
            self.inorder(node.left, result)

        result.append(node.data)

        if node.right:
            self.inorder(node.right, result)

        return result
    
    def postorder(self, node, result=None):
        """후위 순회: Left → Right → Root"""
        # TODO: 후위 순회 구현
        # 힌트: 1. 왼쪽 재귀 2. 오른쪽 재귀 3. 현재 노드 방문
        if result is None:
            result = []
        if node is None:
            return result

        
        if node.left:
            self.postorder(node.left, result)

        if node.right:
            self.postorder(node.right, result)
        
        result.append(node.data)

        return result
    
    def get_all_traversals(self):
        """모든 순회 결과를 딕셔너리로 반환"""
        return {
            "전위": self.preorder(self.root, []),
            "중위": self.inorder(self.root, []),
            "후위": self.postorder(self.root, [])
        }

# 테스트
traversal = TreeTraversal(tree.root)
results = traversal.get_all_traversals()
for name, result in results.items():
    print(f"{name} 순회: {result}")

# 예상 결과:
# 전위: [1, 2, 4, 5, 3]
# 중위: [4, 2, 5, 1, 3]  
# 후위: [4, 5, 2, 3, 1]

print("\n" + "="*60)

# 문제 3: 특정 값 찾기 (🥈 실버 5 난이도)
print("📝 문제 3: 트리에서 특정 값 찾기")
print("난이도: 🥈 실버 5")
print("목표: 트리에서 특정 데이터를 가진 노드 찾기")

def find_node(root, target):
    """트리에서 target 값을 가진 노드 찾기"""
    # TODO: 트리를 순회하면서 target과 같은 데이터를 가진 노드 찾기
    # 힌트: 전위/중위/후위 중 아무거나 사용 가능
    # 반환값: 찾으면 노드 객체, 못 찾으면 None  
    if root is None:
        return None
    if root.data == target:
        return root
    left = find_node(root.left, target)
    if left:
        return left
    
    right = find_node(root.right, target)
    return right


def find_parent(root, target):
    """특정 값의 부모 노드 찾기"""
    # TODO: target의 부모 노드를 찾아서 반환
    # 힌트: 현재 노드의 자식이 target인지 확인
    # 어려운 문제! 차근차근 생각해보기
    if root is None:
        return None

    if root.left and root.left.data == target:
        return root  # 내가 부모!
    if root.right and root.right.data == target:
        return root  # 내가 부모!
    
    left_result = find_parent(root.left, target)
    if left_result:
        return left_result
    
    # 오른쪽에서 찾기
    right_result = find_parent(root.right, target)
    return right_result




def get_path_to_node(root, target, path=None):
    """루트에서 특정 노드까지의 경로 찾기"""
    # TODO: 루트부터 target까지의 경로를 리스트로 반환
    # 힌트: 백트래킹 알고리즘 사용
    # 매우 어려운 문제! 도전 과제
    if path is None:
        path = []
    if root is None:
        return None

    path.append(root.data)

    if root.data == target:
        return True
    
    left = get_path_to_node(root.left, target, path)
    if left:
        return True
    
    right = get_path_to_node(root.right, target, path)
    if right:
        return True
    
    path.pop()
    return None
# root가 None이면?
# root.data가 target과 같으면?
# 1. 현재 노드를 path에 추가
# 2. 왼쪽 자식에서 재귀 탐색
# 3. 찾았으면 True 반환
# 4. 못 찾았으면 오른쪽 자식에서 재귀 탐색  
# 5. 양쪽 다 실패하면 path에서 현재 노드 제거하고 False 반환
# 테스트
found = find_node(tree.root, 4)
if found:
    print(f"노드 4를 찾았습니다: {found.data}")

parent = find_parent(tree.root, 4)  
if parent:
    print(f"노드 4의 부모: {parent.data}")

path = []
if get_path_to_node(tree.root, 4, path):
    print(f"정답은:{path}")
print("\n" + "="*60)



# 문제 4: 트리 비교하기 (🥈 실버 4 난이도)
print("📝 문제 4: 두 트리가 같은지 비교하기")
print("난이도: 🥈 실버 4")
print("목표: 두 이진 트리가 구조와 값이 모두 같은지 확인")

def are_trees_equal(root1, root2):
    """두 트리가 완전히 같은지 비교"""
    # TODO: 두 트리의 구조와 모든 노드의 값이 같은지 확인
    # 힌트: 
    # 1. 둘 다 None이면 같음
    # 2. 하나만 None이면 다름  
    # 3. 둘 다 존재하면 값 비교 + 왼쪽 서브트리 비교 + 오른쪽 서브트리 비교
    if root1 == None and root2 == None:
        return True
    if (root1 is None) != (root2 is None):
        return False
    
    if root1.data != root2.data:
        return False
    
    left = are_trees_equal(root1.left, root2.left)
    if left == False:
        return False
    right = are_trees_equal(root1.right, root2.right)
    if right == False:
        return False
    
    return True

def is_subtree(main_tree, sub_tree):
    """sub_tree가 main_tree의 서브트리인지 확인"""
    # TODO: 더 어려운 도전 문제!
    # 힌트: main_tree의 모든 노드에 대해 sub_tree와 같은지 확인

    if sub_tree is None:
        return True
    if main_tree is None:
        return False
    
    if main_tree.data == sub_tree.data:
        result = are_trees_equal(main_tree, sub_tree)
        if result:
            return True

    left = is_subtree(main_tree.left, sub_tree)
    right = is_subtree(main_tree.right, sub_tree)
    if left or right :
        return True
    
    return False

    

# 테스트용 트리 2 만들기
tree2 = BinaryTree()
tree2.insert_root(1)
tree2.root.left = BinaryTreeNode(2)
tree2.root.right = BinaryTreeNode(3)
tree2.root.left.left = BinaryTreeNode(4)
tree2.root.left.right = BinaryTreeNode(5)

print(f"두 트리가 같나요? {are_trees_equal(tree.root, tree2.root)}")

# 기존 tree 사용 (이미 있는 것)
print("=== is_subtree 간단 테스트 ===")

# 테스트 1: 빈 트리
print(f"빈 트리: {is_subtree(tree.root, None)}")  # True

# 테스트 2: 단일 노드들
single_node = BinaryTreeNode(4)
print(f"노드 4: {is_subtree(tree.root, single_node)}")  # True

single_node2 = BinaryTreeNode(99)
print(f"노드 99: {is_subtree(tree.root, single_node2)}")  # False

# 테스트 3: 서브트리 (노드 2와 그 자식들)
subtree = BinaryTreeNode(2)
subtree.left = BinaryTreeNode(4)
subtree.right = BinaryTreeNode(5)
print(f"서브트리 2(4,5): {is_subtree(tree.root, subtree)}")  # True

# 테스트 4: 잘못된 서브트리
wrong_subtree = BinaryTreeNode(2)
wrong_subtree.left = BinaryTreeNode(4)
wrong_subtree.right = BinaryTreeNode(99)  # 5가 아닌 99
print(f"잘못된 서브트리: {is_subtree(tree.root, wrong_subtree)}")  # False

# 테스트 5: 전체 트리
print(f"전체 트리: {is_subtree(tree.root, tree.root)}")  # True

print("\n" + "="*60)


# 문제 5: 레벨별 출력 (🥈 실버 3 난이도)  
print("📝 문제 5: 트리를 레벨별로 출력하기")
print("난이도: 🥈 실버 3")
print("목표: BFS를 사용해서 트리를 레벨별로 출력")
print("예시: 레벨 0: [1], 레벨 1: [2, 3], 레벨 2: [4, 5]")

def print_level_order(root):
    """트리를 레벨 순서대로 출력 (BFS)"""
    # TODO: 큐를 사용한 BFS로 레벨별 순회
    # 힌트: 
    # 1. 큐에 루트 삽입
    # 2. 큐가 빌 때까지: 노드 하나 꺼내서 출력하고 자식들을 큐에 삽입
    # 3. 레벨 구분하는 방법 생각해보기
    if root is None:
        return
    queue = deque([root])    
    level = 0
    
    while queue:
        level_size = len(queue)  # 🔑 현재 레벨 노드 개수!
        
        print(f"레벨 {level}: ", end="")
        
        # 현재 레벨의 모든 노드 처리
        for i in range(level_size):
            node = queue.popleft()
            print(node.data, end=" ")
            
            # 다음 레벨 노드들 추가
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        print()  # 줄바꿈
        level += 1
    
from collections import deque  # 파이썬 큐 사용
    

def get_level_nodes(root, target_level):
    """특정 레벨의 모든 노드 반환"""
    # TODO: 특정 레벨에 있는 모든 노드를 리스트로 반환
    # 힌트: 현재 레벨이 target_level과 같으면 노드 추가, 다르면 재귀
    if root is None:
        return
    queue = deque([root])    
    level = 0
    
    while queue:
        level_size = len(queue)  
        
        if level == target_level:
            result = [] 
            for i in range(level_size):
                node = queue.popleft()
                result.append(node.data)  
            return result  
        
        # 현재 레벨의 모든 노드 처리
        for i in range(level_size):
            node = queue.popleft()

            
            # 다음 레벨 노드들 추가
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        print()  # 줄바꿈
        level += 1
        if level > target_level:
            break
    return []
    

#테스트
print("레벨 순서 출력:")
print_level_order(tree.root)
print(f"레벨 2 노드들: {get_level_nodes(tree.root, 2)}")

print("\n" + "="*60)

print("🎯 실습 완료 후 체크리스트:")
checklist = [
    "✅ 문제 1: 노드 개수, 높이, 잎 개수가 정확한가요?",
    "✅ 문제 2: 3가지 순회가 모두 올바른 순서인가요?",
    "✅ 문제 3: 노드 찾기와 부모 찾기가 동작하나요?",
    "✅ 문제 4: 트리 비교가 정확하게 작동하나요?",
    "✅ 문제 5: 레벨별 출력이 제대로 나오나요?"
]

for item in checklist:
    print(item)

print("\n💡 막히는 부분이 있으면 구체적으로 질문하세요!")
print("🌳 트리는 재귀 사고방식이 핵심입니다!")
print("🔥 다음 단계: BST(Binary Search Tree) 기다려주세요!")