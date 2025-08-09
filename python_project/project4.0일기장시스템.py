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
        date = input("날짜를 입력하세요 (YYYY-MM-DD),'q'를 입력시 퇴장합니다.: ")
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
        elif date == 'q':
            return
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
    else:
        print("\n📔 === 일기 목록 ===")
        for date, diary in record.items():
            print(f"{date}: {diary['제목']}") 
        choice = input("원하는 날짜를 입력하세요('q'를 입력시 퇴장):")
        if choice == 'q':
            return            
        elif validate_date(choice):
            if choice in record:  # ✅ 키 존재 여부 확인 추가
                print(f"\n📖 {choice} 일기:")
                print(f"제목: {record[choice]['제목']}")
                print(f"내용:\n{record[choice]['내용']}")  # ✅ 'content' → '내용'
                choice_del = input("삭제를 원할시 d를 입력하세요(아니라면 아무 입력): ")
                if choice_del.lower() == 'd':
                    confirm = input("정말 삭제하시겠습니까? (y/n): ")
                    if confirm.lower() == 'y':
                        deleted_diary = record.pop(choice)
                        try:
                            with open('file_storage/diary.json', 'w', encoding='utf-8') as file:
                                json.dump(record, file, ensure_ascii=False, indent=2)
                                print(f"✅ '{deleted_diary['제목']}' 일기가 삭제되었습니다.")
                        except Exception as e:
                                print(f"❌ 삭제 실패: {e}")
                    elif confirm.lower() == 'n':
                                print("삭제가 취소되었습니다.")
                                return
                    else:
                        print("올바른 값을 넣어주세요.")

            else:
                print("❌ 해당 날짜의 일기가 없습니다.")
        else:
            print("❌ 올바른 날짜 형식이 아닙니다!")
    
    
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
            diary_list()
        elif choice == '3':
            break
        else:
            print("올바른 수를 입력해주세요.")

if __name__ == "__main__":
    main()
    print("종료합니다.")