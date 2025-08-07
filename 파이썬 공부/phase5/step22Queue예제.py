# 📚 스택(Stack) 자료구조 완전 가이드

print("=== 📚 스택이란 무엇인가? ===")
print("스택 = 접시 쌓기!")
print("- Last In First Out (LIFO)")
print("- 마지막에 넣은 것이 먼저 나옴")
print("- 위에서만 넣고 빼기 가능")

print("\n" + "="*40)

# 1. 가장 간단한 스택 - 리스트로 만들기
print("1. 가장 간단한 스택 만들기")

stack = []  # 빈 스택

print(f"초기 스택: {stack}")

# 스택에 데이터 추가 (push)
stack.append("첫 번째 책")
print(f"첫 번째 책 추가: {stack}")

stack.append("두 번째 책")
print(f"두 번째 책 추가: {stack}")

stack.append("세 번째 책")
print(f"세 번째 책 추가: {stack}")

print(f"현재 스택 상태: {stack}")
print(f"맨 위에 있는 책: {stack[-1]}")  # 마지막 원소 = 맨 위

# 스택에서 데이터 제거 (pop)
removed = stack.pop()
print(f"{removed} 제거됨: {stack}")

removed = stack.pop()
print(f"{removed} 제거됨: {stack}")

removed = stack.pop()
print(f"{removed} 제거됨: {stack}")

print(f"모든 책 제거 후: {stack}")

print("\n" + "="*40)

# 2. 제대로 된 스택 클래스 만들기
print("2. 스택 클래스 만들기")

class Stack:
    def __init__(self):
        """스택 초기화"""
        self.items = []
        print("📚 새로운 스택이 만들어졌습니다!")
    
    def push(self, item):
        """스택에 원소 추가 (위에 올리기)"""
        self.items.append(item)
        print(f"🔼 '{item}' 추가됨: {self.items}")
    
    def pop(self):
        """스택에서 원소 제거 (위에서 빼기)"""
        if self.is_empty():
            print("❌ 스택이 비어있어서 뺄 수 없습니다!")
            return None
        
        item = self.items.pop()
        print(f"🔽 '{item}' 제거됨: {self.items}")
        return item
    
    def peek(self):
        """맨 위 원소 확인하기 (빼지는 않음)"""
        if self.is_empty():
            print("❌ 스택이 비어있습니다!")
            return None
        return self.items[-1]
    
    def is_empty(self):
        """스택이 비었는지 확인"""
        return len(self.items) == 0
    
    def size(self):
        """스택 크기 확인"""
        return len(self.items)
    
    def show(self):
        """스택 상태 예쁘게 보여주기"""
        if self.is_empty():
            print("📭 빈 스택")
            return
        
        print("📚 현재 스택 상태:")
        for i in range(len(self.items) - 1, -1, -1):  # 위에서부터 보여주기
            if i == len(self.items) - 1:
                print(f"   [{self.items[i]}] ← 맨 위")
            else:
                print(f"   [{self.items[i]}]")
        print("   ^^^^^^^ 바닥")

# 스택 테스트해보기
print("\n=== 스택 클래스 테스트 ===")
my_stack = Stack()

print("\n--- 데이터 추가하기 ---")
my_stack.push("바닥 접시")
my_stack.push("중간 접시")
my_stack.push("맨 위 접시")

print(f"\n맨 위 접시 확인: {my_stack.peek()}")
print(f"스택 크기: {my_stack.size()}")

print("\n스택 상태 보기:")
my_stack.show()

print("\n--- 데이터 빼기 ---")
my_stack.pop()
my_stack.show()

my_stack.pop()
my_stack.show()

my_stack.pop()
my_stack.show()

# 빈 스택에서 빼기 시도
my_stack.pop()

print("\n" + "="*40)

# 3. 실생활 예시 - 브라우저 뒤로가기
print("3. 실생활 예시: 브라우저 뒤로가기")

class Browser:
    def __init__(self):
        self.history = Stack()
        self.current_page = "홈페이지"
        print(f"🌐 브라우저 시작: {self.current_page}")
    
    def visit(self, page):
        """새 페이지 방문"""
        self.history.push(self.current_page)  # 현재 페이지를 기록에 저장
        self.current_page = page
        print(f"🔗 {page} 방문")
        print(f"   현재 페이지: {self.current_page}")
    
    def back(self):
        """뒤로가기"""
        if self.history.is_empty():
            print("❌ 더 이상 뒤로 갈 페이지가 없습니다!")
            return
        
        previous_page = self.history.pop()
        print(f"⬅️ 뒤로가기: {self.current_page} → {previous_page}")
        self.current_page = previous_page

# 브라우저 테스트
print("\n=== 브라우저 시뮬레이션 ===")
browser = Browser()

browser.visit("네이버")
browser.visit("구글")
browser.visit("유튜브")
browser.visit("깃허브")

print("\n--- 뒤로가기 테스트 ---")
browser.back()  # 깃허브 → 유튜브
browser.back()  # 유튜브 → 구글  
browser.back()  # 구글 → 네이버
browser.back()  # 네이버 → 홈페이지
browser.back()  # 더 이상 갈 곳 없음

print("\n" + "="*40)

# 4. 실전 문제 - 괄호 검사기
print("4. 실전 문제: 괄호 짝 맞추기")

def check_parentheses(expression):
    """괄호가 올바르게 짝지어졌는지 검사"""
    stack = Stack()
    
    print(f"\n🔍 검사할 문자열: '{expression}'")
    
    for i, char in enumerate(expression):
        print(f"  {i+1}번째 문자: '{char}'", end=" ")
        
        if char == '(':
            stack.push('(')
            print("→ 여는 괄호 저장")
        elif char == ')':
            if stack.is_empty():
                print("→ ❌ 닫는 괄호인데 짝이 없음!")
                return False
            stack.pop()
            print("→ 닫는 괄호, 짝 맞춤!")
        else:
            print("→ 괄호가 아님, 무시")
    
    if stack.is_empty():
        print("✅ 모든 괄호가 올바르게 짝지어졌습니다!")
        return True
    else:
        print("❌ 짝 맞지 않는 괄호가 있습니다!")
        return False

# 괄호 검사 테스트
test_cases = [
    "()",           # 올바름
    "((()))",       # 올바름
    "(()())",       # 올바름
    "(()",          # 틀림 - 여는 괄호가 많음
    "())",          # 틀림 - 닫는 괄호가 많음
    ")(",           # 틀림 - 순서가 틀림
    "(a + b) * c",  # 올바름 - 다른 문자 포함
]

print("\n=== 괄호 검사 테스트 ===")
for expression in test_cases:
    result = check_parentheses(expression)
    print("-" * 30)

print("\n" + "="*40)

# 5. 스택의 특징 정리
print("5. 📋 스택의 특징 정리")

features = [
    "✅ LIFO (Last In, First Out) - 나중에 들어간 게 먼저 나옴",
    "✅ push() - 데이터 추가 (맨 위에)",
    "✅ pop() - 데이터 제거 (맨 위에서)",
    "✅ peek() - 맨 위 데이터 확인 (제거하지 않음)",
    "✅ is_empty() - 비었는지 확인",
    "✅ size() - 크기 확인"
]

for feature in features:
    print(f"  {feature}")

print(f"\n💡 스택 활용 예시:")
use_cases = [
    "🌐 브라우저 뒤로가기/앞으로가기",
    "↩️ 함수 호출 스택 (Call Stack)",
    "🔄 실행취소(Undo) 기능",
    "📝 수식 계산 (후위표기법)",
    "🔍 괄호/태그 매칭 검사",
    "🧠 재귀 함수 처리"
]

for use_case in use_cases:
    print(f"  {use_case}")

print(f"\n🎯 스택 마스터 포인트:")
tips = [
    "📌 리스트의 append()와 pop()을 사용하면 쉽게 구현",
    "📌 [-1]로 맨 위 원소 확인 가능",
    "📌 빈 스택에서 pop() 시도 시 에러 처리 중요",
    "📌 실생활 예시로 이해하면 쉬움 (접시 쌓기, 책 쌓기 등)"
]

for tip in tips:
    print(f"  {tip}")

print("\n✅ 스택 기초 완전 마스터!")