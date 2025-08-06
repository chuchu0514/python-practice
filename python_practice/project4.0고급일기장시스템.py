import json
import datetime

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def get_multiline_input():
    print("내용을 입력하세요 (빈 줄 입력시 종료):")
    lines = []
    while True:
        line = input()
        if line == "":  # 빈 줄이면 종료
            break
        lines.append(line)
    return "\n".join(lines)

def write_diary():
    try:
        with open('file_storage/diary.json', 'r', encoding='utf-8')as file:
            record = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        record = {}
    except Exception as e:
        print(f"오류가 발생하였습니다{e}")
        return

    while True:
        date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
        if validate_date(date):
            if date in record:
                print(f"⚠️ {date} 일기가 이미 있습니다.")
                print(f"기존 제목: {record[date]['제목']}")
                overwrite = input("덮어쓰시겠습니까? (y/n): ")
                if overwrite.lower() != 'y':
                    print("일기 작성을 취소합니다.")
                    return
                else:
                    break
            else:
                break
        else:
            print("❌ 올바른 날짜 형식이 아닙니다! (예: YYYY-MM-DD)")
    title = input("제목을 입력하세요: ")
    content = get_multiline_input()
    record[date] = {
        "날짜" : date,
        "제목" : title,
        "내용" : content
    }
    try:
        with open('file_storage/diary.json', 'w', encoding='utf-8')as file:
            json.dump(record, file, ensure_ascii=False, indent=2)
            print("✅ 일기가 저장되었습니다!")
    except Exception as e:
        print(f"❌ 저장 실패: {e}")

        

    
def diary_list():
    try:
        with open('file_storage/diary.json', 'r', encoding='utf-8')as file:
            record = json.load(file)
    except FileNotFoundError:
        print("📋 작성된 일기가 없습니다.")
        return
    
    if not record:  # 빈 딕셔너리 체크
        print("📋 작성된 일기가 없습니다.")
        return
    
    print("\n📔 === 일기 목록 ===")
    pass

def menu():
    print("1. 일기 쓰기")
    print("2. 일기 목록")
    print("3. 종료")
    choice = input("입력: ")
    return choice

def main():
    while True:
        choice = menu()
        if choice == '1':
            write_diary()
        elif choice == '2':
            pass
        elif choice == '3':
            break
        else:
            print("올바른 수를 입력해주세요.")

if __name__ == "__main__":
    main()
    print("종료합니다.")