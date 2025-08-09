# 🎯 스택 실습 문제

print("=== 📚 스택 실습 문제 ===")
print("스택 클래스를 활용해서 문제를 해결해보세요!")

# 스택 클래스 (이미 완성된 것 사용)
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

print("\n" + "="*50)

# 문제 1: 문자열 뒤집기
print("📝 문제 1: 스택을 사용해서 문자열 뒤집기")
print("입력: 'hello' → 출력: 'olleh'")
print("힌트: 문자를 하나씩 스택에 넣고, 하나씩 빼면서 새 문자열 만들기")

def reverse_string(text):
    """스택을 사용해서 문자열 뒤집기"""
    # 여기에 코드 작성하세요!
    stack = Stack()
    for char in text:
        stack.push(char)
    
    # TODO: text의 각 문자를 스택에 push
    
    # TODO: 스택에서 문자를 하나씩 pop해서 결과 문자열 만들기
    result = ""
    while not stack.is_empty():
        result += stack.pop()

    return result

# 테스트
test_text = "hello"
result = reverse_string(test_text)
print(f"입력: '{test_text}' → 출력: '{result}'")
print(f"정답: {'olleh' == result}")

print("\n" + "="*50)

# 문제 2: 계산기 (간단한 수식 계산)
print("📝 문제 2: 스택으로 간단한 계산기 만들기")
print("입력: '3 4 +' → 출력: 7")
print("설명: 후위표기법(Postfix) 계산기")
print("- 숫자는 스택에 저장")
print("- 연산자(+, -, *, /)가 나오면 스택에서 숫자 2개 꺼내서 계산")

def postfix_calculator(expression):
    """후위표기법 계산기"""
    stack = Stack()
    tokens = expression.split()  # 공백으로 분리
    
    print(f"계산할 식: {expression}")
    
    for token in tokens:
        print(f"현재 토큰: '{token}'", end=" ")
        
        if token.isdigit():  # 숫자인지 확인
            stack.push(token)
            # TODO: 숫자면 스택에 push
            print(f"→ 숫자를 스택에 저장")
        
        elif token in ['+', '-', '*', '/']:
            second_digit = int(stack.pop())
            first_digit = int(stack.pop())

            if token == '+':
                result = first_digit + second_digit
            elif token == '-':
                result = first_digit - second_digit
            elif token == '*':
                result = first_digit * second_digit
            elif token == '/':
                result = first_digit / second_digit
            stack.push(result)
            # TODO: 연산자면 스택에서 숫자 2개 pop해서 계산
            # 주의: 순서 중요! 두 번째로 pop한 게 첫 번째 피연산자
            print(f"→ 연산자, 계산 수행: {first_digit} {token} {second_digit} = {result}" )
        
        else:
            print(f"→ 알 수 없는 토큰!")
    
    # TODO: 최종 결과 반환 (스택에 남은 마지막 값)
    return result

# 테스트
test_expressions = [
    "3 4 +",      # 3 + 4 = 7
    "5 2 -",      # 5 - 2 = 3  
    "6 2 /",      # 6 / 2 = 3
    "2 3 * 4 +",  # (2 * 3) + 4 = 10
]

for expr in test_expressions:
    result = postfix_calculator(expr)
    print(f"결과: {result}")
    print("-" * 30)

print("\n" + "="*50)

# 문제 3: 실행 취소(Undo) 기능
print("📝 문제 3: 실행 취소 기능 구현하기")
print("텍스트 에디터의 Undo 기능을 스택으로 만들어보세요")

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = Stack()
        # TODO: undo를 위한 스택 생성
        
    def add_text(self, new_text):
        """텍스트 추가"""
        
        self.undo_stack.push(self.text)
        self.text += new_text
        # TODO: 현재 상태를 스택에 저장 (undo를 위해)
        # TODO: 새 텍스트 추가
        print(f"텍스트 추가: '{new_text}' → 현재: '{self.text}'")
    
    def undo(self):
        """실행 취소"""
        if self.undo_stack.is_empty():
            print("더 이상 실행 취소할 것이 없습니다!")
            return
        
        self.text = self.undo_stack.pop()
        # TODO: 스택에서 이전 상태 복원
        print(f"실행 취소 → 현재: '{self.text}'")
    
    def show_history(self):
        """히스토리 보기"""
        temp_stack = Stack()
        items = []
        # TODO: 스택의 내용 보여주기
        print("히스토리:")
        print(f"현재: '{self.text}'")

        while not self.undo_stack.is_empty():
            item = self.undo_stack.pop() 
            items.append(item)
            temp_stack.push(item)

        for i, item in enumerate(reversed(items)):
            print(f"  {i+1}. '{item}'")

        while not temp_stack.is_empty():
            self.undo_stack.push(temp_stack.pop()) 

       

# 테스트
print("\n=== 텍스트 에디터 테스트 ===")
editor = TextEditor()

editor.add_text("안녕")
editor.add_text("하세요")
editor.add_text("!")
editor.show_history()

print("\n--- 실행 취소 테스트 ---")
editor.undo()  # "!" 제거
editor.undo()  # "하세요" 제거
editor.undo()  # "안녕" 제거
editor.undo()  # 더 이상 취소할 것 없음

print("\n" + "="*50)

# 문제 4: 웹브라우저 개선하기
print("📝 문제 4: 웹브라우저에 '앞으로가기' 기능 추가")
print("뒤로가기는 있는데, 앞으로가기도 만들어보세요!")

class AdvancedBrowser:
    def __init__(self):
        self.current_page = "홈페이지"
        self.frontstack = Stack()
        self.backstack = Stack()
        # TODO: 뒤로가기용 스택
        # TODO: 앞으로가기용 스택
        print(f"🌐 브라우저 시작: {self.current_page}")
    
    def visit(self, page):
        """새 페이지 방문"""
        self.backstack.push(self.current_page)
        while not self.frontstack.is_empty():
            self.frontstack.pop()
        # TODO: 현재 페이지를 뒤로가기 스택에 저장
        # TODO: 새 페이지 방문 시 앞으로가기 스택 비우기
        self.current_page = page
        print(f"🔗 {page} 방문")
    
    def back(self):
        """뒤로가기"""
        if self.backstack.is_empty():
            print("❌ 더 이상 뒤로 갈 페이지가 없습니다!")
            return
        self.frontstack.push(self.current_page)
        self.current_page = self.backstack.pop()
        print(f"현재 페이지:{self.current_page}")
        # TODO: 뒤로가기 구현
        # TODO: 현재 페이지를 앞으로가기 스택에 저장
        print(f"⬅️ 뒤로가기")
    
    def forward(self):
        """앞으로가기"""
        if self.frontstack.is_empty():
            print("❌ 더 이상 앞으로 갈 페이지가 없습니다!")
            return
        self.backstack.push(self.current_page)
        self.current_page = self.frontstack.pop()
        print(f"현재 페이지:{self.current_page}")
        # TODO: 앞으로가기 구현
        # TODO: 현재 페이지를 뒤로가기 스택에 저장  
        print(f"➡️ 앞으로가기")

# 테스트
print("\n=== 고급 브라우저 테스트 ===")
browser = AdvancedBrowser()

browser.visit("네이버")
browser.visit("구글") 
browser.visit("유튜브")

print("\n--- 뒤로가기 ---")
browser.back()  # 유튜브 → 구글
browser.back()  # 구글 → 네이버
browser.back()
browser.back()

print("\n--- 앞으로가기 ---")
browser.forward()  # 네이버 → 구글
browser.forward()  # 구글 → 유튜브
browser.forward()
browser.forward()

print("\n" + "="*50)

print("🎯 실습 완료 후 체크리스트:")
checklist = [
    "✅ 문제 1: 문자열이 올바르게 뒤집어졌나요?",
    "✅ 문제 2: 후위표기법 계산이 정확한가요?", 
    "✅ 문제 3: Undo 기능이 제대로 동작하나요?",
    "✅ 문제 4: 뒤로가기/앞으로가기가 정상인가요?"
]

for item in checklist:
    print(item)

print("\n💡 막히는 부분이 있으면 언제든 질문하세요!")
print("📚 스택의 LIFO 원리를 잘 활용하는 게 핵심입니다!")