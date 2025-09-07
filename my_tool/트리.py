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

#이진트리
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

#트리순회
class BinaryTreeWithTraversal(BinaryTreeNode):
    def __init__(self, data):
        super().__init__(data)
    
    def preorder_traversal(self, visit_list=None):
        """전위 순회: Root → Left → Right"""
        if visit_list is None:  # 처음 호출이면 새 리스트 만들기
            visit_list = []
        
        visit_list.append(self.data)  # 1. 루트 방문
        print(f"방문: {self.data}")
        
        if self.left:                 # 2. 왼쪽 서브트리
            self.left.preorder_traversal(visit_list)
        if self.right:                # 3. 오른쪽 서브트리  
            self.right.preorder_traversal(visit_list)
        
        return visit_list
    
    def inorder_traversal(self, visit_list=None):
        """중위 순회: Left → Root → Right"""
        if visit_list is None:  # 처음 호출이면 새 리스트 만들기
            visit_list = []
        
        if self.left:                 # 1. 왼쪽 서브트리
            self.left.inorder_traversal(visit_list)
        visit_list.append(self.data)  # 2. 루트 방문
        print(f"방문: {self.data}")
        if self.right:                # 3. 오른쪽 서브트리
            self.right.inorder_traversal(visit_list)
        
        return visit_list
    
    def postorder_traversal(self, visit_list=None):
        """후위 순회: Left → Right → Root"""
        if visit_list is None:  # 처음 호출이면 새 리스트 만들기
            visit_list = []
        
        if self.left:                 # 1. 왼쪽 서브트리
            self.left.postorder_traversal(visit_list)
        if self.right:                # 2. 오른쪽 서브트리
            self.right.postorder_traversal(visit_list)
        visit_list.append(self.data)  # 3. 루트 방문
        print(f"방문: {self.data}")
        
        return visit_list

