# 🎯 그래프 실습 문제

print("=== 📊 그래프 실습 문제 ===")
print("그래프의 기본 개념부터 고급 응용까지 단계별로 마스터하세요!")

# 🎯 그래프 실습 난이도 (1-10점)
# 문제 1: 그래프 기본 구현 → 4점 (표현 방법 익히기)
# 문제 2: DFS 구현 및 응용 → 5점 (재귀와 백트래킹)
# 문제 3: BFS 구현 및 응용 → 5점 (큐와 최단경로)
# 문제 4: 경로 탐색 문제 → 6점 (실전 문제해결)
# 문제 5: 연결성 및 사이클 → 7점 (그래프 이론)
# 문제 6: 종합 응용 문제 → 8점 (미로, 게임 등)

from collections import deque

print("\n" + "="*60)

# 문제 1: 그래프 기본 구현 (4점)
print("📝 문제 1: 그래프 클래스 완성하기")
print("난이도: 4점")
print("목표: 인접리스트 방식으로 그래프 기본 연산 구현")

class Graph:
    def __init__(self, num_vertices, directed=False):
        """그래프 초기화"""
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_list = [[] for _ in range(num_vertices)]
        print(f"📊 {num_vertices}개 정점의 {'방향' if directed else '무방향'} 그래프 생성")
    
    def add_edge(self, u, v):
        """간선 추가"""
        # TODO: 간선 (u, v) 추가
        # 힌트: 방향 그래프인지 무방향 그래프인지 확인
        # 중복 간선 방지도 고려해보세요
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            if v not in self.adj_list[u]:  # 중복 방지
                self.adj_list[u].append(v)
            if not self.directed:
                if u not in self.adj_list[v]:  # 중복 방지
                    self.adj_list[v].append(u)
        else:
            print(f"❌ 유효하지 않은 정점: {u}, {v}")
            print(f"유효 범위: 0 ~ {self.num_vertices-1}")
        
    def remove_edge(self, u, v):
        """간선 제거"""
        # TODO: 간선 (u, v) 제거
        # 힌트: 리스트에서 remove() 메서드 사용
        # 존재하지 않는 간선 처리도 고려해보세요
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            if v in self.adj_list[u]:  # 중복 방지
                self.adj_list[u].remove(v)
            if not self.directed:
                if u in self.adj_list[v]:  # 중복 방지
                    self.adj_list[v].remove(u)
        else:
            print(f"❌ 유효하지 않은 정점: {u}, {v}")  # ← 수정!
            print(f"유효 범위: 0 ~ {self.num_vertices-1}")

    def get_neighbors(self, vertex):
        """특정 정점의 인접 정점들 반환"""
        # TODO: 정점 vertex의 모든 인접 정점 반환
        # 힌트: 유효한 정점 번호인지 먼저 확인
        if 0 <= vertex < self.num_vertices:
            return self.adj_list[vertex].copy()
        return []
    

    def get_degree(self, vertex):
        """정점의 차수 반환"""
        # TODO: 정점 vertex의 차수(연결된 간선 수) 반환
        # 힌트: 인접 리스트의 길이
        if 0 <= vertex < self.num_vertices:
            return len(self.adj_list[vertex])
        return 0
    
    def is_connected_to(self, u, v):
        """두 정점이 연결되었는지 확인"""
        # TODO: 정점 u와 v가 직접 연결되었는지 확인
        # 힌트: v가 u의 인접 리스트에 있는지 확인
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            return v in self.adj_list[u]  # 이것만으로 충분!
        return False
    
    def count_edges(self):
        """총 간선 수 계산"""
        # TODO: 그래프의 총 간선 수 계산
        # 힌트: 무방향 그래프는 중복 계산 주의 (나누기 2)
        total = 0
        for vertex in range(self.num_vertices):
            total += len(self.adj_list[vertex])  # 각 정점의 차수 합
        
        # 무방향 그래프면 중복 계산이므로 2로 나누기
        if not self.directed:
            return total // 2
        return total

    def display(self):
        """그래프 구조 출력"""
        print("\n📊 그래프 구조:")
        for i in range(self.num_vertices):
            print(f"{i}: {self.adj_list[i]}")

# 테스트
print("\n=== 문제 1 테스트 ===")
g = Graph(5, directed=False)

# 간선 추가 테스트
test_edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
for u, v in test_edges:
    g.add_edge(u, v)

g.display()

print(f"\n정점 0의 인접 정점: {g.get_neighbors(0)}")
print(f"정점 1의 차수: {g.get_degree(1)}")
print(f"0과 3이 연결되었나? {g.is_connected_to(0, 3)}")
print(f"1과 3이 연결되었나? {g.is_connected_to(1, 3)}")
print(f"총 간선 수: {g.count_edges()}")

print("\n" + "="*60)

# 문제 2: DFS 구현 및 응용 (5점)
print("📝 문제 2: DFS 구현 및 응용")
print("난이도: 5점")
print("목표: DFS를 이용한 다양한 문제 해결")

class GraphDFS(Graph):
    def dfs_recursive(self, start):
        """재귀를 이용한 DFS"""
        # TODO: DFS 재귀 구현
        # 힌트: visited 리스트 초기화 → dfs_helper 호출
        # 방문 순서를 리스트로 반환
        visited = [False] * self.num_vertices
        result = []
        self._dfs_helper(start, visited, result)
        # 헬퍼 함수 호출
        return result
    
    def _dfs_helper(self, vertex, visited, result):
        """DFS 재귀 헬퍼 함수"""
        # TODO: DFS 재귀 헬퍼 구현
        # 힌트: 
        # 1. 현재 정점 방문 처리
        # 2. 결과 리스트에 추가
        # 3. 모든 인접 정점에 대해 재귀 호출
        visited[vertex] = True
        result.append(vertex)
        for i in self.adj_list[vertex]:
            if not visited[i]:
                self._dfs_helper(i, visited, result)

    def dfs_iterative(self, start):
        """스택을 이용한 반복적 DFS"""
        # TODO: 스택을 사용한 DFS 구현
        # 힌트: 
        # 1. 스택에 시작 정점 추가
        # 2. 스택이 빌 때까지 반복
        # 3. 스택에서 정점 pop → 방문 처리 → 인접 정점들 push
        visited = [False] * self.num_vertices
        result = []
        stack = []
        stack.append(start)
        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)
                for i in reversed(self.adj_list[vertex]):
                    if not visited[i]:
                        stack.append(i)
        
        return result

    
    def has_path(self, start, end):
        """두 정점 간 경로 존재 여부 확인"""
        # TODO: DFS를 사용해서 start에서 end로 가는 경로가 있는지 확인
        # 힌트: DFS 중간에 end를 만나면 True 반환
        # visited = self.dfs_recursive(start)
        # if end in visited:
        #     return True
        # return False   일케 만들었더니 비효율적이래
        if start == end:
            return True
        visited = [False] * self.num_vertices
        def dfs_search(vertex):
            if vertex == end:
                return True
            visited[vertex] = True
            for i in self.adj_list[vertex]:
                if not visited[i]:
                    if dfs_search(i):
                        return True
            return False
        
        return dfs_search(start)
    
    def find_all_paths(self, start, end):
        """두 정점 간 모든 경로 찾기"""
        # TODO: start에서 end로 가는 모든 경로 찾기
        # 힌트: DFS + 백트래킹 사용
        # 경로를 리스트로 저장하며 탐색
        all_paths = []
        visited = [False] * self.num_vertices
        current_path = []
        # 헬퍼 함수 호출
        self._find_paths_helper(start, end, visited, current_path, all_paths )
        return all_paths
    
    def _find_paths_helper(self, current, end, visited, path, all_paths):
        """모든 경로 찾기 헬퍼 함수"""
        # TODO: 백트래킹을 사용한 모든 경로 찾기
        # 힌트:
        # 1. 현재 정점을 경로에 추가
        # 2. 목표 정점에 도달하면 경로 저장
        # 3. 인접 정점들에 대해 재귀 호출
        # 4. 백트래킹 (현재 정점을 경로에서 제거)
        
        path.append(current)
        visited[current] = True

        if current == end:
            all_paths.append(path.copy())
        else:
            for neighbor in self.adj_list[current]:
                if not visited[neighbor]:
                    self._find_paths_helper(neighbor, end, visited, path, all_paths)
        path.pop()
        visited[current] = False

    
    def count_connected_components(self):
        """연결 성분의 개수 계산"""
        # TODO: DFS를 사용해서 연결 성분 개수 계산
        # 힌트:
        # 1. 모든 정점을 미방문으로 초기화
        # 2. 미방문 정점에서 DFS 시작할 때마다 카운트 증가
        visited = [False] * self.num_vertices
        count = 0
        
        # 모든 정점 확인
        for vertex in range(self.num_vertices):
            if not visited[vertex]:  # 미방문 정점 발견!
                # 새로운 연결 성분 발견! 카운트 증가
                count += 1
                # 이 연결 성분 전체를 방문 처리
                self._dfs_for_component(vertex, visited)
        
        return count

    def _dfs_for_component(self, vertex, visited):
        visited[vertex] = True
        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self._dfs_for_component(neighbor, visited)

# 테스트
print("\n=== 문제 2 테스트 ===")
g_dfs = GraphDFS(6, directed=False)

# 연결된 그래프 (0-1-3, 2-4, 5는 독립)
dfs_edges = [(0, 1), (1, 3), (2, 4)]
for u, v in dfs_edges:
    g_dfs.add_edge(u, v)

g_dfs.display()

print(f"\nDFS 재귀 (시작: 0): {g_dfs.dfs_recursive(0)}")
print(f"DFS 반복 (시작: 0): {g_dfs.dfs_iterative(0)}")
print(f"0에서 3으로 경로 존재? {g_dfs.has_path(0, 3)}")
print(f"0에서 5로 경로 존재? {g_dfs.has_path(0, 5)}")

# 모든 경로 찾기 테스트용 그래프
g_paths = GraphDFS(4, directed=False)
path_edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
for u, v in path_edges:
    g_paths.add_edge(u, v)

print(f"\n경로 찾기 테스트 그래프:")
g_paths.display()
print(f"0에서 3으로 가는 모든 경로: {g_paths.find_all_paths(0, 3)}")
print(f"연결 성분 개수: {g_dfs.count_connected_components()}")

print("\n" + "="*60)

# 문제 3: BFS 구현 및 응용 (5점)
print("📝 문제 3: BFS 구현 및 응용")
print("난이도: 5점")
print("목표: BFS를 이용한 최단경로 및 레벨 탐색")

class GraphBFS(Graph):
    def bfs(self, start):
        """BFS 탐색"""
        # TODO: BFS 구현
        # 힌트:
        # 1. 큐(deque) 초기화, 시작정점 삽입
        # 2. visited 배열 초기화
        # 3. 큐가 빌 때까지 반복:
        #    - 큐에서 정점 pop
        #    - 인접 정점들 중 미방문 정점들 큐에 추가
        queue = deque([start])
        visited = [False] * self.num_vertices
        visited[start] = True
        result = []
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for i in self.adj_list[vertex]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
        return result
    
    def shortest_path(self, start, end):
        """두 정점 간 최단 경로 찾기"""
        # TODO: BFS를 사용한 최단 경로 찾기
        # 힌트:
        # 1. 큐에 (정점, 경로) 쌍으로 저장
        # 2. 목표 정점에 도달하면 경로 반환
        # 3. 각 정점까지의 경로를 같이 저장하며 탐색
        pass
    
    def shortest_distance(self, start, end):
        """두 정점 간 최단 거리 계산"""
        # TODO: BFS를 사용한 최단 거리 계산
        # 힌트: shortest_path의 길이 - 1 또는 직접 거리 계산
        pass
    
    def bfs_levels(self, start):
        """레벨별 BFS (각 레벨의 정점들 그룹화)"""
        # TODO: 시작점에서 각 거리별 정점들을 그룹화
        # 힌트:
        # 1. 큐에 (정점, 레벨) 쌍으로 저장
        # 2. 레벨별로 딕셔너리에 정점들 저장
        # 반환: {0: [start], 1: [level1_nodes], 2: [level2_nodes], ...}
        pass
    
    def is_bipartite(self):
        """이분 그래프 판별"""
        # TODO: BFS를 사용해서 그래프가 이분 그래프인지 확인
        # 힌트:
        # 1. 각 정점을 두 색깔 중 하나로 칠하기
        # 2. 인접한 정점끼리 다른 색이어야 함
        # 3. 색칠이 불가능하면 이분 그래프가 아님
        pass
    
    def find_all_distances(self, start):
        """시작점에서 모든 정점까지의 최단거리"""
        # TODO: 시작점에서 모든 정점까지의 최단거리 계산
        # 힌트: BFS하면서 각 정점의 거리 저장
        # 반환: [거리] 배열, 도달 불가능하면 -1
        pass

# 테스트
print("\n=== 문제 3 테스트 ===")
g_bfs = GraphBFS(6, directed=False)

# 테스트용 그래프 생성
bfs_edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5)]
for u, v in bfs_edges:
    g_bfs.add_edge(u, v)

g_bfs.display()

print(f"\nBFS 탐색 (시작: 0): {g_bfs.bfs(0)}")
print(f"0에서 5로 최단경로: {g_bfs.shortest_path(0, 5)}")
print(f"0에서 5로 최단거리: {g_bfs.shortest_distance(0, 5)}")

levels = g_bfs.bfs_levels(0)
print(f"레벨별 정점들: {levels}")

distances = g_bfs.find_all_distances(0)
print(f"0에서 모든 정점까지 거리: {distances}")

# 이분 그래프 테스트
g_bipartite = GraphBFS(4, directed=False)
bipartite_edges = [(0, 1), (0, 3), (1, 2), (2, 3)]
for u, v in bipartite_edges:
    g_bipartite.add_edge(u, v)

print(f"\n이분 그래프 테스트:")
g_bipartite.display()
print(f"이분 그래프인가? {g_bipartite.is_bipartite()}")

print("\n" + "="*60)

# 문제 4: 경로 탐색 문제 (6점)
print("📝 문제 4: 경로 탐색 종합 문제")
print("난이도: 6점")
print("목표: 다양한 경로 탐색 알고리즘 구현")

class PathFinder(GraphBFS, GraphDFS):
    def has_cycle(self):
        """사이클 존재 여부 확인 (무방향 그래프)"""
        # TODO: DFS를 사용해서 사이클 탐지
        # 힌트:
        # 1. DFS 중에 이미 방문한 정점을 다시 만나면 사이클
        # 2. 단, 바로 이전 정점(부모)은 제외
        # 3. 모든 연결 성분에 대해 확인
        pass
    
    def has_cycle_directed(self):
        """사이클 존재 여부 확인 (방향 그래프)"""
        # TODO: DFS를 사용해서 방향 그래프의 사이클 탐지
        # 힌트:
        # 1. WHITE(0), GRAY(1), BLACK(2) 상태 사용
        # 2. GRAY 상태인 정점을 다시 만나면 사이클
        # 3. 재귀 스택에서 현재 처리 중인 정점들 추적
        pass
    
    def topological_sort(self):
        """위상 정렬 (DAG에서만 가능)"""
        # TODO: DFS를 사용한 위상 정렬
        # 힌트:
        # 1. DFS로 탐색하면서 종료 시간 기록
        # 2. 종료 시간의 역순이 위상 정렬 순서
        # 3. 사이클이 있으면 위상 정렬 불가능
        pass
    
    def find_bridges(self):
        """다리(Bridge) 찾기"""
        # TODO: 타잔 알고리즘을 사용한 다리 찾기
        # 힌트: 제거하면 연결 성분이 증가하는 간선
        # 고급 문제 - 도전 과제!
        pass
    
    def diameter(self):
        """그래프의 지름 (가장 먼 두 정점 간 거리)"""
        # TODO: 모든 정점 쌍에 대해 최단거리 계산 후 최댓값
        # 힌트: 각 정점에서 BFS 실행하여 최대 거리 찾기
        pass
    
    def center_vertices(self):
        """중심 정점들 찾기"""
        # TODO: 각 정점의 편심도(다른 모든 정점까지의 최대 거리) 계산
        # 편심도가 최소인 정점들이 중심
        pass

# 테스트
print("\n=== 문제 4 테스트 ===")

# 사이클 없는 그래프
g_tree = PathFinder(5, directed=False)
tree_edges = [(0, 1), (1, 2), (1, 3), (3, 4)]
for u, v in tree_edges:
    g_tree.add_edge(u, v)

print("트리 구조:")
g_tree.display()
print(f"사이클 있나? {g_tree.has_cycle()}")
print(f"그래프 지름: {g_tree.diameter()}")
print(f"중심 정점들: {g_tree.center_vertices()}")

# 사이클 있는 그래프  
g_cycle = PathFinder(4, directed=False)
cycle_edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
for u, v in cycle_edges:
    g_cycle.add_edge(u, v)

print(f"\n사이클 구조:")
g_cycle.display()
print(f"사이클 있나? {g_cycle.has_cycle()}")

# 방향 그래프 위상 정렬
g_dag = PathFinder(6, directed=True)
dag_edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
for u, v in dag_edges:
    g_dag.add_edge(u, v)

print(f"\nDAG 구조:")
g_dag.display()
print(f"위상 정렬: {g_dag.topological_sort()}")

print("\n" + "="*60)

# 문제 5: 연결성 및 사이클 심화 (7점)
print("📝 문제 5: 연결성 및 사이클 심화")
print("난이도: 7점")  
print("목표: 그래프의 연결성과 구조 분석")

class ConnectivityAnalyzer(PathFinder):
    def find_articulation_points(self):
        """단절점(Articulation Points) 찾기"""
        # TODO: 타잔 알고리즘을 사용한 단절점 찾기
        # 힌트: 제거하면 연결 성분이 증가하는 정점
        # 고급 문제 - 도전 과제!
        pass
    
    def is_connected(self):
        """그래프가 연결되어 있는지 확인"""
        # TODO: DFS 또는 BFS로 모든 정점에 도달 가능한지 확인
        # 힌트: 임의의 정점에서 시작해서 방문 가능한 정점 수 확인
        pass
    
    def find_shortest_cycle(self):
        """가장 짧은 사이클의 길이 찾기"""
        # TODO: 각 간선을 제거하고 BFS로 우회경로 찾기
        # 힌트: 간선 (u,v)를 제거하고 u에서 v로 가는 최단경로 + 1
        pass
    
    def count_triangles(self):
        """삼각형(3-cycle) 개수 세기"""
        # TODO: 모든 정점 3개 조합에 대해 삼각형 형성 여부 확인
        # 힌트: 정점 i, j, k가 모두 서로 연결되어 있으면 삼각형
        pass
    
    def graph_density(self):
        """그래프 밀도 계산"""
        # TODO: 실제 간선 수 / 최대 가능 간선 수
        # 힌트: 무방향 그래프의 최대 간선 수 = n(n-1)/2
        pass
    
    def clustering_coefficient(self, vertex):
        """특정 정점의 군집 계수 계산"""
        # TODO: 이웃들 간의 연결 정도 측정
        # 힌트: 이웃들 사이의 실제 간선 / 가능한 최대 간선
        pass

# 테스트  
print("\n=== 문제 5 테스트 ===")
g_conn = ConnectivityAnalyzer(6, directed=False)

# 복잡한 연결 구조
conn_edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
for u, v in conn_edges:
    g_conn.add_edge(u, v)

g_conn.display()

print(f"\n연결되어 있나? {g_conn.is_connected()}")
print(f"삼각형 개수: {g_conn.count_triangles()}")
print(f"그래프 밀도: {g_conn.graph_density():.3f}")
print(f"정점 1의 군집계수: {g_conn.clustering_coefficient(1):.3f}")
print(f"가장 짧은 사이클 길이: {g_conn.find_shortest_cycle()}")

print("\n" + "="*60)

# 문제 6: 종합 응용 문제 (8점)
print("📝 문제 6: 종합 응용 문제")
print("난이도: 8점")
print("목표: 실전 문제에 그래프 알고리즘 적용")

class MazeGraph:
    """미로를 그래프로 모델링"""
    def __init__(self, maze):
        """
        미로 초기화
        0: 통로, 1: 벽, 'S': 시작점, 'E': 끝점
        """
        # TODO: 미로를 그래프로 변환
        # 힌트: 
        # 1. 각 칸을 정점으로 변환 (2D → 1D 인덱스)
        # 2. 인접한 통로들을 간선으로 연결
        # 3. 시작점과 끝점 위치 저장
        pass
    
    def solve_dfs(self):
        """DFS로 미로 해결"""
        # TODO: DFS를 사용한 미로 탈출
        # 힌트: 경로를 함께 저장하면서 백트래킹
        pass
    
    def solve_bfs(self):
        """BFS로 미로 해결 (최단 경로)"""
        # TODO: BFS를 사용한 최단 경로 찾기
        pass
    
    def count_dead_ends(self):
        """막다른 길 개수 계산"""
        # TODO: 차수가 1인 정점들 중 시작/끝점이 아닌 것들
        pass
    
    def find_all_exits(self):
        """모든 출구 찾기 (경계에 있는 통로)"""
        # TODO: 미로 경계에 있는 모든 통로 찾기
        pass

class SocialNetwork:
    """소셜 네트워크 분석"""
    def __init__(self):
        self.graph = Graph(0, directed=False)
        self.users = {}  # 이름 → ID 매핑
        self.user_names = []  # ID → 이름 매핑
    
    def add_user(self, name):
        """사용자 추가"""
        # TODO: 새 사용자를 그래프에 추가
        pass
    
    def add_friendship(self, user1, user2):
        """친구 관계 추가"""
        # TODO: 두 사용자 간 친구 관계 추가
        pass
    
    def mutual_friends(self, user1, user2):
        """공통 친구 찾기"""
        # TODO: 두 사용자의 공통 친구들 반환
        # 힌트: 두 사용자의 인접 정점들의 교집합
        pass
    
    def friend_recommendation(self, user):
        """친구 추천"""
        # TODO: 친구의 친구들 중 직접 친구가 아닌 사람들
        # 힌트: 거리 2인 정점들 찾기
        pass
    
    def six_degrees_of_separation(self, user1, user2):
        """6도 분리 이론 확인"""
        # TODO: 두 사용자 간 최단 경로의 길이 계산
        # 6보다 작으면 연결되어 있다고 판단
        pass
    
    def most_popular_user(self):
        """가장 인기 있는 사용자 (친구가 가장 많은)"""
        # TODO: 차수가 가장 높은 정점 찾기
        pass
    
    def find_communities(self):
        """커뮤니티 찾기 (연결 성분)"""
        # TODO: DFS를 사용해서 연결된 그룹들 찾기
        pass

# 테스트
print("\n=== 문제 6 테스트 ===")

# 미로 테스트
maze = [
    ['S', '0', '1', '0'],
    ['0', '0', '1', '0'], 
    ['1', '0', '0', '0'],
    ['0', '0', '1', 'E']
]

print("🗺️ 미로 테스트:")
maze_graph = MazeGraph(maze)
for row in maze:
    print('  ' + ' '.join(row))

dfs_path = maze_graph.solve_dfs()
bfs_path = maze_graph.solve_bfs()
print(f"DFS 경로: {dfs_path}")
print(f"BFS 경로: {bfs_path}")
print(f"막다른 길 개수: {maze_graph.count_dead_ends()}")

# 소셜 네트워크 테스트  
print(f"\n👥 소셜 네트워크 테스트:")
social = SocialNetwork()

users = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
for user in users:
    social.add_user(user)

friendships = [('Alice', 'Bob'), ('Bob', 'Charlie'), ('Alice', 'David'), ('Charlie', 'Eve')]
for user1, user2 in friendships:
    social.add_friendship(user1, user2)

print(f"Alice와 Charlie의 공통친구: {social.mutual_friends('Alice', 'Charlie')}")
print(f"Alice에게 추천할 친구: {social.friend_recommendation('Alice')}")
print(f"Alice와 Eve의 분리도: {social.six_degrees_of_separation('Alice', 'Eve')}")
print(f"가장 인기있는 사용자: {social.most_popular_user()}")

print("\n" + "="*60)

# 종합 테스트 및 정리
print("🎯 그래프 실습 완료 후 체크리스트:")

checklist = [
    "□ 문제 1: 그래프 기본 구현 (인접리스트, 간선 추가/삭제)",
    "□ 문제 2: DFS 구현 (재귀, 반복, 경로찾기, 연결성분)",  
    "□ 문제 3: BFS 구현 (최단경로, 레벨탐색, 이분그래프)",
    "□ 문제 4: 경로 탐색 (사이클, 위상정렬, 지름, 중심점)",
    "□ 문제 5: 연결성 분석 (단절점, 다리, 밀도, 군집계수)",
    "□ 문제 6: 실전 응용 (미로, 소셜네트워크)"
]

for item in checklist:
    print(f"  {item}")

print("\n💡 그래프 마스터 포인트:")
tips = [
    "🎯 표현법: 인접리스트 vs 인접행렬 (상황에 따라 선택)",
    "🔍 DFS: 재귀/스택, 경로탐색, 사이클검사, 연결성분",
    "🌐 BFS: 큐, 최단경로, 레벨탐색, 이분그래프",
    "⏱️ 시간복잡도: DFS/BFS 모두 O(V + E)",
    "🔄 백트래킹: 모든 경로 찾기, 조합 탐색",
    "📊 응용분야: 지도, SNS, 웹, 게임, AI"
]

for tip in tips:
    print(f"  {tip}")

print("\n🚀 다음 단계 예고:")
next_steps = [
    "⚖️ 가중치 그래프: 다익스트라, 벨만-포드, 플로이드-워셜",
    "🌳 최소신장트리: 크루스칼, 프림 알고리즘",
    "🔗 네트워크 플로우: 최대유량, 최소비용",
    "🎯 고급 그래프: 강연결성분, 2-SAT",
    "🏆 Phase 5 최종 프로젝트: 알고리즘 종합 시뮬레이터"
]

for step in next_steps:
    print(f"  {step}")

print("\n✨ 그래프 기초 실습 준비 완료!")
print("🏆 이제 직접 구현해서 그래프 알고리즘 전문가가 되어보세요!")
print("\n🎯 그래프 실습 완료!")
print("다음은 Phase 5 총정리와 최종 프로젝트가 기다리고 있습니다! 🚀")