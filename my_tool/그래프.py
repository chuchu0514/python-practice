#인접행렬
class AdjacencyMatrix:
    def __init__(self, num_vertices):
        """인접 행렬로 그래프 초기화"""
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        print(f"📊 {num_vertices}개 정점의 인접 행렬 생성")
    
    def add_edge(self, u, v, directed=False):
        """간선 추가"""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = 1
            if not directed:  # 무방향 그래프면 양방향 연결
                self.matrix[v][u] = 1
            print(f"간선 추가: {u} - {v}")
        else:
            print("❌ 잘못된 정점 번호!")
    
    def remove_edge(self, u, v, directed=False):
        """간선 제거"""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = 0
            if not directed:
                self.matrix[v][u] = 0
            print(f"간선 제거: {u} - {v}")
    
    def is_connected(self, u, v):
        """두 정점이 연결되었는지 확인"""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            return self.matrix[u][v] == 1
        return False
    
    def get_neighbors(self, vertex):
        """특정 정점의 인접 정점들 반환"""
        if 0 <= vertex < self.num_vertices:
            neighbors = []
            for i in range(self.num_vertices):
                if self.matrix[vertex][i] == 1:
                    neighbors.append(i)
            return neighbors
        return []
    
    def display(self):
        """인접 행렬 출력"""
        print("\n📊 인접 행렬:")
        print("   ", end="")
        for i in range(self.num_vertices):
            print(f"{i:2}", end=" ")
        print()
        
        for i in range(self.num_vertices):
            print(f"{i}: ", end="")
            for j in range(self.num_vertices):
                print(f"{self.matrix[i][j]:2}", end=" ")
            print()

#인접리스트
class AdjacencyList:
    def __init__(self, num_vertices):
        """인접 리스트로 그래프 초기화"""
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
        print(f"📝 {num_vertices}개 정점의 인접 리스트 생성")
    
    def add_edge(self, u, v, directed=False):
        """간선 추가"""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            if v not in self.adj_list[u]:  # 중복 방지
                self.adj_list[u].append(v)
            if not directed and u not in self.adj_list[v]:
                self.adj_list[v].append(u)
            print(f"간선 추가: {u} - {v}")
        else:
            print("❌ 잘못된 정점 번호!")
    
    def remove_edge(self, u, v, directed=False):
        """간선 제거"""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)
            if not directed and u in self.adj_list[v]:
                self.adj_list[v].remove(u)
            print(f"간선 제거: {u} - {v}")
    
    def is_connected(self, u, v):
        """두 정점이 연결되었는지 확인"""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            return v in self.adj_list[u]
        return False
    
    def get_neighbors(self, vertex):
        """특정 정점의 인접 정점들 반환"""
        if 0 <= vertex < self.num_vertices:
            return self.adj_list[vertex].copy()
        return []
    
    def display(self):
        """인접 리스트 출력"""
        print("\n📝 인접 리스트:")
        for i in range(self.num_vertices):
            print(f"{i}: {self.adj_list[i]}")

#DFS
class GraphDFS:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
        self.visited = [False] * num_vertices
    
    def add_edge(self, u, v, directed=False):
        """간선 추가"""
        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].append(u)
    
    def dfs_recursive(self, start_vertex, visited_order=None):
        """재귀를 사용한 DFS"""
        if visited_order is None:
            visited_order = []
            self.visited = [False] * self.num_vertices
        
        # 현재 정점 방문 처리
        self.visited[start_vertex] = True
        visited_order.append(start_vertex)
        print(f"방문: {start_vertex}")
        
        # 인접한 정점들을 재귀적으로 방문
        for neighbor in self.adj_list[start_vertex]:
            if not self.visited[neighbor]:
                self.dfs_recursive(neighbor, visited_order)
        
        return visited_order
    
    def dfs_iterative(self, start_vertex):
        """스택을 사용한 DFS (반복문)"""
        visited = [False] * self.num_vertices
        stack = [start_vertex]
        visited_order = []
        
        print(f"\n🔍 DFS 시작 (스택 사용): {start_vertex}")
        
        while stack:
            vertex = stack.pop()
            
            if not visited[vertex]:
                visited[vertex] = True
                visited_order.append(vertex)
                print(f"방문: {vertex} (스택: {stack})")
                
                # 인접 정점들을 스택에 추가 (역순으로)
                for neighbor in reversed(self.adj_list[vertex]):
                    if not visited[neighbor]:
                        stack.append(neighbor)
        
        return visited_order
    
    def display(self):
        """그래프 출력"""
        print("\n📊 그래프 구조:")
        for i in range(self.num_vertices):
            print(f"{i}: {self.adj_list[i]}")

#BFS

from collections import deque

class GraphBFS:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v, directed=False):
        """간선 추가"""
        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].append(u)
    
    def bfs(self, start_vertex):
        """BFS 탐색"""
        visited = [False] * self.num_vertices
        queue = deque([start_vertex])
        visited[start_vertex] = True
        visited_order = []
        
        print(f"\n🌐 BFS 시작: {start_vertex}")
        
        while queue:
            vertex = queue.popleft()
            visited_order.append(vertex)
            print(f"방문: {vertex} (큐: {list(queue)})")
            
            # 인접한 정점들을 큐에 추가
            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return visited_order
    
    def bfs_with_levels(self, start_vertex):
        """레벨별 BFS (거리 정보 포함)"""
        visited = [False] * self.num_vertices
        queue = deque([(start_vertex, 0)])  # (정점, 거리)
        visited[start_vertex] = True
        levels = {}
        
        print(f"\n🌐 레벨별 BFS 시작: {start_vertex}")
        
        while queue:
            vertex, level = queue.popleft()
            
            if level not in levels:
                levels[level] = []
            levels[level].append(vertex)
            
            print(f"방문: {vertex} (레벨 {level})")
            
            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, level + 1))
        
        return levels
    
    def shortest_path(self, start, end):
        """두 정점 간 최단 경로 찾기"""
        if start == end:
            return [start]
        
        visited = [False] * self.num_vertices
        queue = deque([(start, [start])])  # (현재정점, 경로)
        visited[start] = True
        
        while queue:
            vertex, path = queue.popleft()
            
            for neighbor in self.adj_list[vertex]:
                if neighbor == end:
                    return path + [neighbor]
                
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, path + [neighbor]))
        
        return None  # 경로 없음
    
    def display(self):
        """그래프 출력"""
        print("\n📊 그래프 구조:")
        for i in range(self.num_vertices):
            print(f"{i}: {self.adj_list[i]}")
