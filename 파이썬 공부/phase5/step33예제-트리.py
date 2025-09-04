# 🌳 트리(Tree) 자료구조 완전 가이드

print("=== 🌳 트리란 무엇인가? ===")
print("트리 = 거꾸로 된 나무!")
print("- 뿌리(Root)가 위에, 잎(Leaf)이 아래")
print("- 부모-자식 관계로 연결")
print("- 사이클이 없는 연결 그래프")

print("\n실생활 예시:")
examples = [
    "📁 폴더 구조 (Windows 탐색기)",
    "🏢 회사 조직도 (사장 → 부장 → 과장 → 사원)",
    "🧬 가족 족보 (조상 → 부모 → 자식)",
    "🌐 HTML DOM 구조",
    "🔍 결정 트리 (Decision Tree)"
]

for ex in examples:
    print(f"  {ex}")

print("\n" + "="*50)

# 1. 트리 용어 정리
print("1. 🔤 트리 핵심 용어")

terms = {
    "노드(Node)": "트리의 각 데이터 요소",
    "루트(Root)": "최상위 노드 (부모가 없는 노드)",
    "부모(Parent)": "상위에 연결된 노드",
    "자식(Child)": "하위에 연결된 노드", 
    "잎(Leaf)": "자식이 없는 노드",
    "높이(Height)": "루트부터 가장 깊은 잎까지의 거리",
    "깊이(Depth)": "루트부터 특정 노드까지의 거리",
    "서브트리": "큰 트리의 일부분"
}

for term, desc in terms.items():
    print(f"📌 {term}: {desc}")

print("\n" + "="*50)

# 2. 가장 간단한 트리 노드 클래스
print("2. 🌿 트리 노드 만들기")

class TreeNode:
    def __init__(self, data):
        """트리 노드 초기화"""
        self.data = data           # 데이터 저장
        self.children = []         # 자식 노드들 리스트
        print(f"🌿 노드 '{data}' 생성됨")
    
    def add_child(self, child_node):
        """자식 노드 추가"""
        self.children.append(child_node)
        print(f"   '{self.data}'에게 자식 '{child_node.data}' 추가됨")
    
    def show_tree(self, level=0):
        """트리 구조를 예쁘게 출력 (들여쓰기로 계층 표현)"""
        indent = "  " * level  # 레벨만큼 들여쓰기
        print(f"{indent}├─ {self.data}")
        
        # 모든 자식에 대해 재귀적으로 출력
        for child in self.children:
            child.show_tree(level + 1)
    
    def count_nodes(self):
        """트리의 총 노드 수 계산"""
        count = 1  # 자기 자신
        for child in self.children:
            count += child.count_nodes()  # 재귀!
        return count
    
    def get_height(self):
        """트리의 높이 계산"""
        if not self.children:  # 잎 노드
            return 0
        
        max_child_height = 0
        for child in self.children:
            child_height = child.get_height()
            if child_height > max_child_height:
                max_child_height = child_height
        
        return max_child_height + 1

# 트리 만들기 테스트
print("\n=== 회사 조직도 만들기 ===")
# 사장 노드 (루트)
ceo = TreeNode("사장")

# 부장들 (사장의 자식)
sales_director = TreeNode("영업부장")
tech_director = TreeNode("기술부장")
hr_director = TreeNode("인사부장")

ceo.add_child(sales_director)
ceo.add_child(tech_director)
ceo.add_child(hr_director)

# 과장들 (부장의 자식)
sales_manager = TreeNode("영업과장")
tech_manager1 = TreeNode("개발과장")
tech_manager2 = TreeNode("QA과장")

sales_director.add_child(sales_manager)
tech_director.add_child(tech_manager1)
tech_director.add_child(tech_manager2)

# 사원들 (과장의 자식)
employee1 = TreeNode("김사원")
employee2 = TreeNode("이사원")
employee3 = TreeNode("박사원")

sales_manager.add_child(employee1)
tech_manager1.add_child(employee2)
tech_manager1.add_child(employee3)

print("\n🏢 완성된 조직도:")
ceo.show_tree()

print(f"\n📊 회사 통계:")
print(f"  총 직원 수: {ceo.count_nodes()}명")
print(f"  조직 높이: {ceo.get_height()}단계")

print("\n" + "="*50)

# 3. 이진 트리 (Binary Tree) - 가장 중요!
print("3. 🔱 이진 트리 (Binary Tree)")
print("특징: 각 노드가 최대 2개의 자식만 가짐")
print("      left(왼쪽 자식), right(오른쪽 자식)")

class BinaryTreeNode:
    def __init__(self, data):
        """이진 트리 노드 초기화"""
        self.data = data
        self.left = None      # 왼쪽 자식
        self.right = None     # 오른쪽 자식
        print(f"🔱 이진 노드 '{data}' 생성됨")
    
    def set_left(self, node):
        """왼쪽 자식 설정"""
        self.left = node
        print(f"   '{self.data}'의 왼쪽에 '{node.data}' 연결")
    
    def set_right(self, node):
        """오른쪽 자식 설정"""
        self.right = node
        print(f"   '{self.data}'의 오른쪽에 '{node.data}' 연결")
    
    def show_binary_tree(self, level=0, prefix="Root: "):
        """이진 트리 구조 출력"""
        if self is not None:
            print("  " * level + prefix + str(self.data))
            if self.left is not None or self.right is not None:
                if self.left:
                    self.left.show_binary_tree(level + 1, "L--- ")
                else:
                    print("  " * (level + 1) + "L--- None")
                if self.right:
                    self.right.show_binary_tree(level + 1, "R--- ")
                else:
                    print("  " * (level + 1) + "R--- None")

# 이진 트리 만들기
print("\n=== 간단한 이진 트리 만들기 ===")
root = BinaryTreeNode("A")
node_b = BinaryTreeNode("B")
node_c = BinaryTreeNode("C")
node_d = BinaryTreeNode("D")
node_e = BinaryTreeNode("E")

# 트리 구조 만들기:
#       A
#      / \
#     B   C
#    / \
#   D   E

root.set_left(node_b)
root.set_right(node_c)
node_b.set_left(node_d)
node_b.set_right(node_e)

print("\n🌳 완성된 이진 트리:")
root.show_binary_tree()

print("\n" + "="*50)

# 4. 트리 순회 (Tree Traversal) - 초중요!
print("4. 🚶‍♂️ 트리 순회 (Tree Traversal)")
print("트리의 모든 노드를 체계적으로 방문하는 방법")

class BinaryTreeWithTraversal(BinaryTreeNode):
    def __init__(self, data):
        super().__init__(data)
    
    def preorder_traversal(self, visit_list=[]):
        """전위 순회: Root → Left → Right"""
        if not hasattr(self, '_visit_list'):
            visit_list = []
            self._visit_list = visit_list
        
        visit_list.append(self.data)  # 1. 루트 방문
        print(f"방문: {self.data}")
        
        if self.left:                 # 2. 왼쪽 서브트리
            self.left.preorder_traversal(visit_list)
        if self.right:                # 3. 오른쪽 서브트리  
            self.right.preorder_traversal(visit_list)
        
        return visit_list
    
    def inorder_traversal(self, visit_list=[]):
        """중위 순회: Left → Root → Right"""
        if not hasattr(self, '_visit_list_in'):
            visit_list = []
            self._visit_list_in = visit_list
        
        if self.left:                 # 1. 왼쪽 서브트리
            self.left.inorder_traversal(visit_list)
        visit_list.append(self.data)  # 2. 루트 방문
        print(f"방문: {self.data}")
        if self.right:                # 3. 오른쪽 서브트리
            self.right.inorder_traversal(visit_list)
        
        return visit_list
    
    def postorder_traversal(self, visit_list=[]):
        """후위 순회: Left → Right → Root"""
        if not hasattr(self, '_visit_list_post'):
            visit_list = []
            self._visit_list_post = visit_list
        
        if self.left:                 # 1. 왼쪽 서브트리
            self.left.postorder_traversal(visit_list)
        if self.right:                # 2. 오른쪽 서브트리
            self.right.postorder_traversal(visit_list)
        visit_list.append(self.data)  # 3. 루트 방문
        print(f"방문: {self.data}")
        
        return visit_list

# 순회 테스트용 트리
print("\n=== 트리 순회 테스트 ===")
root = BinaryTreeWithTraversal("1")
root.left = BinaryTreeWithTraversal("2")
root.right = BinaryTreeWithTraversal("3")
root.left.left = BinaryTreeWithTraversal("4")
root.left.right = BinaryTreeWithTraversal("5")

print("트리 구조:")
print("    1")
print("   / \\")
print("  2   3")
print(" / \\")
print("4   5")

print("\n🔄 전위 순회 (Preorder): Root → Left → Right")
preorder_result = root.preorder_traversal()
print(f"결과: {preorder_result}")

print("\n🔄 중위 순회 (Inorder): Left → Root → Right")
inorder_result = root.inorder_traversal()
print(f"결과: {inorder_result}")

print("\n🔄 후위 순회 (Postorder): Left → Right → Root")
postorder_result = root.postorder_traversal()
print(f"결과: {postorder_result}")

print("\n" + "="*50)

# 5. 트리의 특징과 활용
print("5. 📋 트리의 특징 정리")

features = [
    "✅ 계층적 데이터 표현에 최적",
    "✅ 검색, 삽입, 삭제가 효율적 (BST의 경우)",
    "✅ 재귀적 구조 (서브트리도 트리)",
    "✅ 사이클이 없음 (비순환 그래프)",
    "✅ n개 노드면 n-1개 간선"
]

for feature in features:
    print(f"  {feature}")

print(f"\n💡 트리 활용 분야:")
use_cases = [
    "🔍 검색 트리 (Binary Search Tree)",
    "📁 파일 시스템",
    "🌐 웹사이트 구조 (HTML DOM)",
    "🤖 AI 결정 트리",
    "📊 데이터베이스 인덱스 (B-Tree)",
    "🧮 수식 표현 (Expression Tree)",
    "🎮 게임 AI (Minimax Tree)"
]

for use_case in use_cases:
    print(f"  {use_case}")

print(f"\n🎯 트리 마스터 포인트:")
tips = [
    "📌 재귀 사고방식이 핵심! (큰 문제 → 작은 문제)",
    "📌 순회 방법 3가지는 반드시 암기",
    "📌 BST는 다음 단계의 핵심 내용",
    "📌 실생활 예시로 이해하면 쉬움"
]

for tip in tips:
    print(f"  {tip}")

print("\n🚀 다음 단계: BST(Binary Search Tree) 구현!")
print("✅ 트리 기초 개념 완전 마스터!")