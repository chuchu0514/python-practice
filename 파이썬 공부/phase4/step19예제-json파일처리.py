# 📊 JSON 파일 처리 완전 가이드

import json
import datetime

print("=== 📊 JSON 파일 처리 완전 가이드 ===")

# 1. JSON이 뭔가요?
print("1. JSON이란?")
print("JSON = JavaScript Object Notation")
print("= 딕셔너리를 파일로 저장하는 표준 형식!")

# 딕셔너리 예시
student = {
    "name": "진성",
    "age": 25,
    "major": "컴퓨터공학",
    "scores": {
        "수학": 85,
        "영어": 92,
        "과학": 78
    },
    "hobbies": ["코딩", "게임", "독서"],
    "graduated": False
}

print(f"\n딕셔너리: {student}")

print("\n" + "="*50)

# 2. 딕셔너리를 JSON 파일로 저장하기
print("2. 딕셔너리 → JSON 파일 저장")

# JSON 파일로 저장
with open('student.json', 'w', encoding='utf-8') as file:
    json.dump(student, file, ensure_ascii=False, indent=2) #indent는 들여쓰기 

print("✅ student.json 파일로 저장 완료!")

# JSON 파일 내용 확인
print("\n📄 생성된 JSON 파일 내용:")
with open('student.json', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

print("\n💡 특징:")
print("- 사람이 읽기 쉬움")
print("- 구조가 명확함") 
print("- 들여쓰기로 예쁘게 정리됨")

print("\n" + "="*50)

# 3. JSON 파일에서 딕셔너리로 불러오기
print("3. JSON 파일 → 딕셔너리 불러오기")

with open('student.json', 'r', encoding='utf-8') as file:
    loaded_student = json.load(file)

print(f"불러온 데이터: {loaded_student}")
print(f"타입: {type(loaded_student)}")
print(f"이름: {loaded_student['name']}")
print(f"수학 점수: {loaded_student['scores']['수학']}")

print("\n" + "="*50)

# 4. JSON 옵션들 설명
print("4. JSON 저장 옵션들")

sample_data = {
    "한글": "안녕하세요",
    "English": "Hello", 
    "numbers": [1, 2, 3],
    "nested": {"key": "value"}
}

print("옵션별 저장 결과:")

# 옵션 1: 기본 저장 (한글 깨짐)
with open('option1.json', 'w', encoding='utf-8') as file:
    json.dump(sample_data, file)
print("✅ option1.json: 기본 저장 (한 줄, 한글 유니코드)")

# 옵션 2: 한글 정상 출력
with open('option2.json', 'w', encoding='utf-8') as file:
    json.dump(sample_data, file, ensure_ascii=False)
print("✅ option2.json: 한글 정상 출력")

# 옵션 3: 예쁘게 정렬 (들여쓰기)
with open('option3.json', 'w', encoding='utf-8') as file:
    json.dump(sample_data, file, ensure_ascii=False, indent=2)
print("✅ option3.json: 예쁘게 들여쓰기")

# 옵션 4: 키 정렬까지
with open('option4.json', 'w', encoding='utf-8') as file:
    json.dump(sample_data, file, ensure_ascii=False, indent=2, sort_keys=True)
print("✅ option4.json: 키까지 정렬")

print("\n💡 추천 옵션:")
print("json.dump(data, file, ensure_ascii=False, indent=2)")

print("\n" + "="*50)

# 5. 실전 예제: 설정 파일 관리
print("5. 실전 예제: 프로그램 설정 파일")

# 프로그램 설정 데이터
config = {
    "app_name": "진성의 학습 도우미",
    "version": "1.0.0",
    "user_settings": {
        "theme": "dark",
        "language": "ko",
        "auto_save": True,
        "save_interval": 300  # 5분
    },
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "learning_db"
    },
    "features": ["auto_backup", "cloud_sync", "offline_mode"]
}

# 설정 저장
def save_config(config_data, filename="config.json"):
    """설정을 JSON 파일로 저장"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(config_data, file, ensure_ascii=False, indent=2)
        print(f"✅ 설정이 {filename}에 저장되었습니다.")
    except Exception as e:
        print(f"❌ 설정 저장 실패: {e}")

# 설정 불러오기
def load_config(filename="config.json"):
    """JSON 파일에서 설정 불러오기"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"❌ {filename} 파일을 찾을 수 없습니다.")
        return None
    except json.JSONDecodeError:
        print(f"❌ {filename} 파일이 손상되었습니다.")
        return None
    except Exception as e:
        print(f"❌ 설정 불러오기 실패: {e}")
        return None

# 테스트
save_config(config)
loaded_config = load_config()

if loaded_config:
    print("📋 불러온 설정:")
    print(f"앱 이름: {loaded_config['app_name']}")
    print(f"테마: {loaded_config['user_settings']['theme']}")
    print(f"자동 저장: {loaded_config['user_settings']['auto_save']}")

print("\n" + "="*50)

# 6. 실전 예제: 사용자 데이터 관리
print("6. 실전 예제: 사용자 데이터베이스")

# 사용자 데이터베이스
users_db = {
    "users": [
        {
            "id": 1,
            "username": "jinsung",
            "email": "jinsung@example.com",
            "profile": {
                "name": "진성",
                "age": 25,
                "interests": ["프로그래밍", "게임", "음악"]
            },
            "created_at": "2024-01-15",
            "last_login": "2024-08-04",
            "is_active": True
        },
        {
            "id": 2,
            "username": "alice",
            "email": "alice@example.com", 
            "profile": {
                "name": "앨리스",
                "age": 23,
                "interests": ["독서", "요리", "여행"]
            },
            "created_at": "2024-02-20",
            "last_login": "2024-08-03",
            "is_active": True
        }
    ],
    "total_users": 2,
    "last_updated": "2024-08-04 15:30:00"
}

# 사용자 데이터 저장
with open('users.json', 'w', encoding='utf-8') as file:
    json.dump(users_db, file, ensure_ascii=False, indent=2)

print("✅ 사용자 데이터베이스 저장 완료!")

# 특정 사용자 찾기
def find_user_by_username(username):
    """사용자명으로 사용자 찾기"""
    try:
        with open('users.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        for user in data['users']:
            if user['username'] == username:
                return user
        return None
    except Exception as e:
        print(f"❌ 사용자 검색 실패: {e}")
        return None

# 테스트
user = find_user_by_username("jinsung")
if user:
    print(f"👤 찾은 사용자: {user['profile']['name']}")
    print(f"📧 이메일: {user['email']}")
    print(f"🎯 관심사: {', '.join(user['profile']['interests'])}")

print("\n" + "="*50)

# 7. JSON vs TXT 비교
print("7. JSON vs TXT 파일 비교")

# TXT 방식 (비추천)
txt_data = """진성,25,컴퓨터공학,85,92,78"""

print("❌ TXT 방식:")
print(f"데이터: {txt_data}")
print("문제점:")
print("- 구조 파악 어려움")
print("- 데이터 타입 구분 불가") 
print("- 중첩 데이터 표현 어려움")
print("- 파싱 복잡함")

print("\n✅ JSON 방식:")
json_data = {
    "name": "진성",
    "age": 25,
    "major": "컴퓨터공학", 
    "scores": {"수학": 85, "영어": 92, "과학": 78}
}
print(f"데이터: {json.dumps(json_data, ensure_ascii=False, indent=2)}")
print("장점:")
print("- 구조 명확함")
print("- 데이터 타입 보존")
print("- 중첩 구조 자연스럽게 표현")
print("- 파싱 간단함")

print("\n" + "="*50)

# 8. 주의사항과 에러 처리
print("8. JSON 주의사항과 에러 처리")

print("⚠️ JSON에서 지원하지 않는 파이썬 타입들:")

# 날짜 객체 (에러 발생)
problematic_data = {
    "name": "테스트",
    "date": datetime.datetime.now(),  # 이건 JSON으로 저장 안됨!
    # "set": {1, 2, 3},  # 집합도 안됨!
    # "tuple": (1, 2, 3)  # 튜플도 안됨!
}

print("❌ 지원 안되는 타입들:")
print("- datetime 객체")
print("- set (집합)")
print("- tuple (튜플 → 리스트로 변환됨)")
print("- 함수, 클래스")

# 안전한 저장 방법
safe_data = {
    "name": "테스트",
    "date": datetime.datetime.now().isoformat(),  # 문자열로 변환
    "numbers": [1, 2, 3],  # 리스트 사용
    "coordinates": [10, 20]  # 튜플 대신 리스트
}

print("\n✅ 안전한 저장:")
with open('safe_data.json', 'w', encoding='utf-8') as file:
    json.dump(safe_data, file, ensure_ascii=False, indent=2)
print("날짜를 문자열로 변환해서 저장!")

print("\n" + "="*50)

# 9. 마무리 팁
print("9. 💡 JSON 활용 팁")

tips = [
    "✅ 설정 파일: config.json",
    "✅ 사용자 데이터: users.json", 
    "✅ 게임 세이브: save_game.json",
    "✅ API 응답 저장: api_cache.json",
    "✅ 로그 데이터: logs.json"
]

for tip in tips:
    print(f"  {tip}")

print(f"\n🎯 JSON 마스터 공식:")
print("1. 딕셔너리 만들기")
print("2. json.dump(data, file, ensure_ascii=False, indent=2)")
print("3. json.load(file)로 불러오기")
print("4. try-except로 안전하게 처리")

print("\n✅ JSON 기초 완전 마스터!")