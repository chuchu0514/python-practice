# 📁 파일 추가 모드 (append) 완전 가이드

print("=== 📝 파일 모드 비교 ===")

# 1. 'w' 모드 - 기존 내용 삭제하고 새로 쓰기
print("1. 'w' 모드 테스트")
with open('test_write.txt', 'w', encoding='utf-8') as file:
    file.write("첫 번째 내용\n")

with open('test_write.txt', 'w', encoding='utf-8') as file:
    file.write("두 번째 내용\n")  # 첫 번째 내용이 사라짐!

with open('test_write.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(f"'w' 모드 결과: {repr(content)}")  # "두 번째 내용\n"만 남음

print("\n" + "="*40)

# 2. 'a' 모드 - 기존 내용 뒤에 추가
print("2. 'a' 모드 테스트")
with open('test_append.txt', 'w', encoding='utf-8') as file:
    file.write("첫 번째 내용\n")

with open('test_append.txt', 'a', encoding='utf-8') as file:  # append 모드!
    file.write("두 번째 내용\n")  # 첫 번째 내용 뒤에 추가!

with open('test_append.txt', 'a', encoding='utf-8') as file:
    file.write("세 번째 내용\n")  # 계속 추가!

with open('test_append.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(f"'a' 모드 결과: {repr(content)}")  # 모든 내용이 누적됨

print("\n" + "="*40)

# 3. 실전 예시: 로그 파일 만들기
print("3. 실전 예시: 로그 파일")

import datetime

def write_log(message):
    """로그 메시지를 파일에 추가"""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{current_time}] {message}\n"
    
    with open('app.log', 'a', encoding='utf-8') as file:
        file.write(log_entry)

# 로그 기록해보기
write_log("프로그램 시작")
write_log("사용자 로그인: 진성")
write_log("파일 처리 완료")
write_log("프로그램 종료")

# 로그 파일 읽어보기
print("\n📋 로그 파일 내용:")
try:
    with open('app.log', 'r', encoding='utf-8') as file:
        logs = file.read()
        print(logs)
except FileNotFoundError:
    print("로그 파일이 없습니다.")

print("\n" + "="*40)

# 4. 파일이 없을 때 'a' 모드의 동작
print("4. 파일이 없을 때 'a' 모드")

# 존재하지 않는 파일에 'a' 모드로 쓰기
with open('new_file_append.txt', 'a', encoding='utf-8') as file:
    file.write("새 파일에 첫 번째 내용\n")

print("✅ 파일이 없어도 'a' 모드는 새로 생성해줍니다!")

# 확인해보기
with open('new_file_append.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(f"새 파일 내용: {repr(content)}")

print("\n" + "="*40)

# 5. 실전 활용: 방문자 기록 시스템
print("5. 실전 활용: 방문자 기록 시스템")

def record_visitor(name):
    """방문자를 기록"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = f"{timestamp} - {name}님이 방문하셨습니다.\n"
    
    with open('visitors.txt', 'a', encoding='utf-8') as file:
        file.write(record)
    
    print(f"✅ {name}님의 방문이 기록되었습니다.")

def show_visitors():
    """방문자 목록 보기"""
    try:
        with open('visitors.txt', 'r', encoding='utf-8') as file:
            visitors = file.read()
            print("📋 방문자 기록:")
            print(visitors)
    except FileNotFoundError:
        print("아직 방문자가 없습니다.")

# 테스트
record_visitor("진성")
record_visitor("철수") 
record_visitor("영희")

print()
show_visitors()

print("\n" + "="*40)

# 6. 파일 모드 정리표
print("6. 📚 파일 모드 완전 정리")

modes_info = {
    'r': "읽기 전용 (파일이 없으면 에러)",
    'w': "쓰기 전용 (기존 내용 삭제, 없으면 생성)",
    'a': "추가 전용 (기존 내용 뒤에 추가, 없으면 생성)",
    'r+': "읽기+쓰기 (파일이 있어야 함)",
    'w+': "읽기+쓰기 (기존 내용 삭제, 없으면 생성)",
    'a+': "읽기+추가 (기존 내용 뒤에 추가, 없으면 생성)"
}

for mode, description in modes_info.items():
    print(f"'{mode}': {description}")

print("\n💡 가장 많이 사용하는 모드:")
print("✅ 'r': 파일 읽기")
print("✅ 'w': 파일 새로 쓰기") 
print("✅ 'a': 파일에 내용 추가")