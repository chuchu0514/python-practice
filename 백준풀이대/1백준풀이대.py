# 🎮 미로 탈출 게임 - 시연용 버전

print("=== 🎮 미로 탈출 게임 시연 ===")
print("컴퓨터가 자동으로 미로를 탐색합니다!")
print()

# 간단한 스택 클래스
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# 미로 게임 클래스
class MazeDemo:
    def __init__(self):
        # 간단한 미로 (# = 벽, 공백 = 길, S = 시작, E = 출구)
        self.maze = [
            ['#', '#', '#', '#', '#', '#', '#'],
            ['#', 'S', ' ', '#', ' ', ' ', '#'],
            ['#', '#', ' ', '#', ' ', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', '#', '#'],
            ['#', ' ', '#', '#', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', 'E', '#'],
            ['#', '#', '#', '#', '#', '#', '#']
        ]
        
        self.rows = len(self.maze)
        self.cols = len(self.maze[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.path_stack = Stack()
        self.step_count = 0
        
        # 시작점과 출구 찾기
        self.start = None
        self.end = None
        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 'S':
                    self.start = (i, j)
                elif self.maze[i][j] == 'E':
                    self.end = (i, j)
    
    def show_maze(self, current_pos=None):
        """미로를 화면에 출력"""
        print("현재 미로 상태:")
        for i in range(self.rows):
            for j in range(self.cols):
                if current_pos and (i, j) == current_pos:
                    print('@', end='')  # 현재 탐색 위치
                elif self.visited[i][j] and self.maze[i][j] not in ['S', 'E']:
                    print('*', end='')   # 방문한 곳
                elif self.maze[i][j] == '#':
                    print('#', end='')   # 벽
                elif self.maze[i][j] == 'S':
                    print('S', end='')   # 시작점
                elif self.maze[i][j] == 'E':
                    print('E', end='')   # 출구
                else:
                    print(' ', end='')   # 빈 공간
            print()  # 줄바꿈
        print()
    
    def get_neighbors(self, pos):
        """현재 위치에서 갈 수 있는 방향들 반환"""
        row, col = pos
        neighbors = []
        
        # 상하좌우 4방향 체크
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            # 범위 체크
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                # 벽이 아니고, 아직 방문하지 않은 곳
                if self.maze[new_row][new_col] != '#' and not self.visited[new_row][new_col]:
                    neighbors.append((new_row, new_col))
        
        return neighbors
    
    def solve_step_by_step(self):
        """단계별로 미로 탐색 (DFS 방식)"""
        print("🎯 미로 탐색 시작!")
        print("Enter 키를 눌러서 한 스텝씩 진행하세요...\n")
        
        # 시작점부터 시작
        self.path_stack.push(self.start)
        
        while not self.path_stack.is_empty():
            current_pos = self.path_stack.pop()
            row, col = current_pos
            
            # 이미 방문한 곳이면 스킵
            if self.visited[row][col]:
                continue
            
            # 현재 위치 방문 표시
            self.visited[row][col] = True
            self.step_count += 1
            
            # 화면 출력
            print(f"🔍 Step {self.step_count}: 위치 ({row}, {col}) 탐색 중...")
            print(f"📚 스택 크기: {self.path_stack.size()}")
            self.show_maze(current_pos)
            
            # 출구 도달 체크
            if current_pos == self.end:
                print("🎉 축하합니다! 출구를 찾았습니다!")
                print(f"총 {self.step_count}번의 탐색으로 출구 발견!")
                return True
            
            # 갈 수 있는 방향들 찾기
            neighbors = self.get_neighbors(current_pos)
            
            if neighbors:
                print(f"🧭 갈 수 있는 방향: {len(neighbors)}개")
                # 모든 방향을 스택에 추가 (나중에 추가한 것부터 탐색)
                for neighbor in neighbors:
                    self.path_stack.push(neighbor)
            else:
                print("🚫 막다른 길! 되돌아갑니다... (백트래킹)")
            
            input("Enter를 눌러서 계속...") # 사용자 입력 대기
            print("-" * 40)
        
        print("😢 출구를 찾을 수 없습니다!")
        return False

# 게임 실행
def main():
    game = MazeDemo()
    
    print("🎮 게임 설명:")
    print("- S = 시작점")  
    print("- E = 출구")
    print("- # = 벽")
    print("- @ = 현재 탐색 위치")
    print("- * = 이미 방문한 곳")
    print()
    
    print("초기 미로:")
    game.show_maze()
    
    input("게임을 시작하려면 Enter를 누르세요...")
    print()
    
    # 미로 탐색 시작
    game.solve_step_by_step()

if __name__ == "__main__":
    main()