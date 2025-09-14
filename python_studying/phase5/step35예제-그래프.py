# 📊 그래프(Graph) 자료구조 완전 가이드

print("=== 📊 그래프란 무엇인가? ===")
print("그래프 = 점(정점)과 선(간선)으로 이루어진 자료구조!")
print("- 정점(Vertex/Node): 데이터를 저장하는 지점")
print("- 간선(Edge): 정점들을 연결하는 선")
print("- 실생활 예시: 지도, SNS 친구관계, 웹페이지 링크")

print("\n" + "="*60)

# 1. 그래프의 기본 개념과 용어
print("1. 📚 그래프 기본 용어")

print("\n🔹 그래프 종류:")
print("- 무방향 그래프: A-B (양방향)")
print("- 방향 그래프: A→B (단방향)")
print("- 가중치 그래프: A--5--B (간선에 비용)")

print("\n🔹 그래프 표현:")
print("정점 집합 V = {A, B, C, D}")
print("간선 집합 E = {(A,B), (B,C), (C,D), (A,D)}")

print("\n🔹 용어 정리:")
terms = [
    "차수(Degree): 정점에 연결된 간선의 수",
    "경로(Path): 정점에서 정점으로 가는 간선들의 순서",
    "사이클(Cycle): 시작점과 끝점이 같은 경로",
    "연결성(Connectivity): 모든 정점이 연결되어 있는지"
]

for term in terms:
    print(f"  • {term}")

print("\n" + "="*60)

# 2. 그래프 표현 방법 1: 인접 행렬
print("2. 📈 인접 행렬(Adjacency Matrix) 표현")

print("\n💡 개념: 2차원 배열로 연결 관계 표현")
print("matrix[i][j] = 1이면 정점 i와 j가 연결")
print("matrix[i][j] = 0이면 정점 i와 j가 연결되지 않음")

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

# 인접 행렬 테스트
print("\n=== 인접 행렬 테스트 ===")
graph_matrix = AdjacencyMatrix(5)

# 간선 추가
edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
for u, v in edges:
    graph_matrix.add_edge(u, v)

graph_matrix.display()

print(f"\n정점 0의 인접 정점들: {graph_matrix.get_neighbors(0)}")
print(f"정점 0과 3이 연결되었나? {graph_matrix.is_connected(0, 3)}")
print(f"정점 1과 3이 연결되었나? {graph_matrix.is_connected(1, 3)}")

print("\n" + "="*60)

# 3. 그래프 표현 방법 2: 인접 리스트
print("3. 📝 인접 리스트(Adjacency List) 표현")

print("\n💡 개념: 각 정점마다 연결된 정점들의 리스트 저장")
print("메모리 효율적 - 간선이 적은 희소 그래프에 유리")

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

# 인접 리스트 테스트
print("\n=== 인접 리스트 테스트 ===")
graph_list = AdjacencyList(5)

# 간선 추가
for u, v in edges:
    graph_list.add_edge(u, v)

graph_list.display()

print(f"\n정점 0의 인접 정점들: {graph_list.get_neighbors(0)}")
print(f"정점 0과 3이 연결되었나? {graph_list.is_connected(0, 3)}")
print(f"정점 1과 3이 연결되었나? {graph_list.is_connected(1, 3)}")

print("\n" + "="*60)

# 4. 인접 행렬 vs 인접 리스트 비교
print("4. ⚖️ 인접 행렬 vs 인접 리스트 비교")

comparison = """
┌─────────────────┬─────────────────┬─────────────────┐
│     기준        │   인접 행렬     │   인접 리스트   │
├─────────────────┼─────────────────┼─────────────────┤
│ 공간 복잡도     │     O(V²)       │     O(V+E)      │
│ 간선 추가/삭제  │     O(1)        │     O(V)        │
│ 간선 존재 확인  │     O(1)        │     O(V)        │
│ 모든 인접 정점  │     O(V)        │     O(degree)   │
│ 희소 그래프     │   메모리 낭비   │   메모리 효율   │
│ 조밀한 그래프   │   메모리 효율   │   오히려 비효율 │
└─────────────────┴─────────────────┴─────────────────┘
"""

print(comparison)

print("\n💡 선택 기준:")
selection_guide = [
    "🔹 간선이 많은 조밀한 그래프 → 인접 행렬",
    "🔹 간선이 적은 희소 그래프 → 인접 리스트", 
    "🔹 간선 존재 확인이 빈번 → 인접 행렬",
    "🔹 인접 정점 탐색이 빈번 → 인접 리스트"
]

for guide in selection_guide:
    print(f"  {guide}")

print("\n" + "="*60)

# 5. DFS (깊이 우선 탐색) 구현
print("5. 🔍 DFS (Depth-First Search) - 깊이 우선 탐색")

print("\n💡 개념: 한 방향으로 끝까지 탐색한 후 다른 방향 탐색")
print("🔧 구현 방법: 재귀 또는 스택 사용")
print("📊 시간복잡도: O(V + E)")

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

# DFS 테스트
print("\n=== DFS 테스트 ===")
graph_dfs = GraphDFS(6)

# 그래프 생성: 0-1-3-5, 0-2-4
dfs_edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5)]
for u, v in dfs_edges:
    graph_dfs.add_edge(u, v)

graph_dfs.display()

print(f"\n🔍 DFS 시작 (재귀): 0")
result_recursive = graph_dfs.dfs_recursive(0)
print(f"방문 순서: {result_recursive}")

print(f"\n🔍 DFS 시작 (반복): 0") 
result_iterative = graph_dfs.dfs_iterative(0)
print(f"방문 순서: {result_iterative}")

print("\n" + "="*60)

# 6. BFS (너비 우선 탐색) 구현
print("6. 🌐 BFS (Breadth-First Search) - 너비 우선 탐색")

print("\n💡 개념: 시작점에서 가까운 정점부터 차례로 탐색")
print("🔧 구현 방법: 큐 사용")
print("📊 시간복잡도: O(V + E)")
print("🎯 특징: 최단 경로 찾기에 유용")

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

# BFS 테스트
print("\n=== BFS 테스트 ===")
graph_bfs = GraphBFS(6)

# 그래프 생성
bfs_edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (1, 4)]
for u, v in bfs_edges:
    graph_bfs.add_edge(u, v)

graph_bfs.display()

result_bfs = graph_bfs.bfs(0)
print(f"BFS 방문 순서: {result_bfs}")

levels = graph_bfs.bfs_with_levels(0)
print(f"\n레벨별 정점들:")
for level, vertices in levels.items():
    print(f"  레벨 {level}: {vertices}")

path = graph_bfs.shortest_path(0, 5)
print(f"\n0에서 5로의 최단 경로: {path}")
print(f"최단 거리: {len(path) - 1}")

print("\n" + "="*60)

# 7. DFS vs BFS 비교 및 활용
print("7. 🆚 DFS vs BFS 비교")

comparison_table = """
┌─────────────────┬──────────────────┬──────────────────┐
│     특성        │       DFS        │       BFS        │
├─────────────────┼──────────────────┼──────────────────┤
│ 자료구조        │  스택 (재귀)     │       큐         │
│ 메모리 사용량   │     O(h)         │     O(w)         │
│ 완전성          │   무한그래프 X   │       O          │
│ 최적성          │       X          │   가중치없을때   │
│ 시간복잡도      │    O(V + E)      │    O(V + E)      │
└─────────────────┴──────────────────┴──────────────────┘

h = 트리의 최대 깊이, w = 트리의 최대 너비
"""

print(comparison_table)

print("\n🎯 DFS 활용 분야:")
dfs_uses = [
    "🔹 경로 존재 여부 확인",
    "🔹 위상 정렬 (Topological Sort)",
    "🔹 강연결 성분 찾기",
    "🔹 백트래킹 문제 해결",
    "🔹 사이클 검출",
    "🔹 미로 탈출"
]

for use in dfs_uses:
    print(f"  {use}")

print("\n🎯 BFS 활용 분야:")
bfs_uses = [
    "🔹 최단 경로 찾기 (가중치 없을 때)",
    "🔹 레벨별 탐색",
    "🔹 두 정점 간 최단 거리",
    "🔹 연결 성분 찾기", 
    "🔹 이분 그래프 판별",
    "🔹 웹 크롤링"
]

for use in bfs_uses:
    print(f"  {use}")

print("\n" + "="*60)

# 8. 실전 예제: 미로 탈출 (DFS vs BFS)
print("8. 🎮 실전 예제: 미로 탈출")

class MazeSolver:
    def __init__(self, maze):
        """
        미로 초기화
        0: 길, 1: 벽, S: 시작점, E: 끝점
        """
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.start = self.find_position('S')
        self.end = self.find_position('E')
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상
    
    def find_position(self, target):
        """특정 문자의 위치 찾기"""
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == target:
                    return (i, j)
        return None
    
    def is_valid(self, row, col):
        """유효한 위치인지 확인"""
        return (0 <= row < self.rows and 
                0 <= col < self.cols and 
                self.maze[row][col] != '1')
    
    def solve_dfs(self):
        """DFS로 미로 해결"""
        visited = set()
        path = []
        
        def dfs(row, col):
            if (row, col) == self.end:
                path.append((row, col))
                return True
            
            if (row, col) in visited or not self.is_valid(row, col):
                return False
            
            visited.add((row, col))
            path.append((row, col))
            
            # 4방향 탐색
            for dr, dc in self.directions:
                new_row, new_col = row + dr, col + dc
                if dfs(new_row, new_col):
                    return True
            
            path.pop()  # 백트래킹
            return False
        
        if dfs(self.start[0], self.start[1]):
            return path
        return None
    
    def solve_bfs(self):
        """BFS로 미로 해결 (최단 경로)"""
        queue = deque([(self.start[0], self.start[1], [self.start])])
        visited = {self.start}
        
        while queue:
            row, col, path = queue.popleft()
            
            if (row, col) == self.end:
                return path
            
            for dr, dc in self.directions:
                new_row, new_col = row + dr, col + dc
                
                if (new_row, new_col) not in visited and self.is_valid(new_row, new_col):
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, path + [(new_row, new_col)]))
        
        return None
    
    def print_maze(self, path=None):
        """미로와 경로 출력"""
        for i in range(self.rows):
            for j in range(self.cols):
                if path and (i, j) in path and self.maze[i][j] not in ['S', 'E']:
                    print('*', end=' ')  # 경로 표시
                else:
                    print(self.maze[i][j], end=' ')
            print()

# 미로 테스트
print("\n=== 미로 탈출 테스트 ===")
maze = [
    ['S', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '1'],
    ['1', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '0'],
    ['0', '0', '0', 'E', '0']
]

solver = MazeSolver(maze)

print("🗺️ 원본 미로:")
solver.print_maze()

print(f"\n시작점: {solver.start}")
print(f"끝점: {solver.end}")

# DFS 해결
dfs_path = solver.solve_dfs()
if dfs_path:
    print(f"\n🔍 DFS 경로 (길이: {len(dfs_path)}):")
    solver.print_maze(dfs_path)
    print(f"경로: {dfs_path}")

# BFS 해결
bfs_path = solver.solve_bfs()
if bfs_path:
    print(f"\n🌐 BFS 경로 (길이: {len(bfs_path)}):")
    solver.print_maze(bfs_path)
    print(f"경로: {bfs_path}")

if dfs_path and bfs_path:
    print(f"\n📊 비교 결과:")
    print(f"DFS 경로 길이: {len(dfs_path)}")
    print(f"BFS 경로 길이: {len(bfs_path)}")
    print(f"BFS가 {len(dfs_path) - len(bfs_path)}만큼 더 짧음!" if len(bfs_path) < len(dfs_path) else "두 경로의 길이가 같음")

print("\n" + "="*60)

# 9. 그래프 기초 정리
print("9. 📋 그래프 기초 완전 정리")

print("\n🎯 그래프 핵심 포인트:")
key_points = [
    "📊 그래프 = 정점(Vertex) + 간선(Edge)",
    "🏗️ 표현법: 인접행렬(조밀) vs 인접리스트(희소)",
    "🔍 DFS: 깊이 우선, 스택/재귀, 경로탐색",
    "🌐 BFS: 너비 우선, 큐, 최단경로",
    "⏱️ 시간복잡도: 둘 다 O(V + E)",
    "🎮 응용: 미로탈출, SNS, 지도, 웹크롤링"
]

for point in key_points:
    print(f"  {point}")

print("\n🔧 구현 패턴:")
patterns = [
    "인접리스트: [[] for _ in range(V)]",
    "DFS 재귀: visited 체크 → 인접정점 재귀호출",
    "BFS 큐: deque 사용 → 레벨별 탐색",
    "경로 찾기: 경로 정보를 함께 저장",
    "백트래킹: DFS에서 path.pop()"
]

for pattern in patterns:
    print(f"  • {pattern}")

print("\n🚀 다음 단계:")
next_steps = [
    "🌟 가중치 그래프 (다익스트라, 벨만-포드)",
    "🔗 최소신장트리 (크루스칼, 프림)",
    "🔄 위상정렬 (DAG에서의 순서)",
    "🎯 이분그래프 (두 색칠하기)",
    "💫 강연결성분 (SCC)"
]

for step in next_steps:
    print(f"  {step}")

print("\n✨ 그래프 기초 완전 마스터!")
print("🎯 이제 실습 문제로 그래프 정복하러 가봅시다! 🚀")