class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    

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
