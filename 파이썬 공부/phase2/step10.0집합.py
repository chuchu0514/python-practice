# 집합

grades = {85, 90, 78, 90, 85, 92, 78 }
print(grades)

students_math = {"철수", "영희", "민수", "지은"}
students_english = {"영희", "민수", "수진", "태호"}

# 1
print(students_math & students_english)
# 2
print(students_math - students_english)
# 3
print(students_math | students_english)

language = set()

language.update(["python", "java", "c++"])

language.discard("java")

# 1


# 🎯 Phase 2-4: 집합(Set) 완전 가이드

print("=== 🎯 집합(Set) 완전 가이드 ===")

# 1. 집합 만들기
print("1. 집합 만들기")
numbers = {1, 2, 3, 4, 5}
fruits = {"사과", "바나나", "포도"}
mixed = {1, "안녕", 3.14, True}
empty_set = set()  # 주의: {}는 빈 딕셔너리!

print(f"숫자 집합: {numbers}")
print(f"과일 집합: {fruits}")
print(f"섞인 집합: {mixed}")
print(f"빈 집합: {empty_set}")

print("\n⚠️ 주의: {}는 빈 딕셔너리, 빈 집합은 set()!")

# 리스트에서 집합 만들기
duplicate_list = [1, 2, 2, 3, 3, 3, 4, 5]
unique_set = set(duplicate_list)
print(f"중복 리스트: {duplicate_list}")
print(f"중복 제거 집합: {unique_set}")

print("\n" + "="*40)

# 2. 집합의 특징
print("2. 집합의 핵심 특징")

print("✅ 특징 1: 중복 허용 안 함")
test_set = {1, 2, 2, 3, 3, 3}
print(f"중복 있는 집합: {test_set}")  # 중복 자동 제거!

print("\n✅ 특징 2: 순서 없음")
set1 = {3, 1, 4, 2}
set2 = {1, 2, 3, 4}
print(f"집합1: {set1}")
print(f"집합2: {set2}")
print(f"같은 집합인가? {set1 == set2}")  # True!

print("\n✅ 특징 3: 인덱싱 불가능")
colors = {"빨강", "파랑", "노랑"}
print(f"색깔 집합: {colors}")
# print(colors[0])  # ❌ 에러! 순서가 없어서 인덱싱 불가

print("\n" + "="*40)

# 3. 집합에 요소 추가/제거
print("3. 집합 요소 추가/제거")
animals = {"고양이", "강아지"}
print(f"초기 동물: {animals}")

# add - 요소 하나 추가
animals.add("햄스터")
print(f"햄스터 추가: {animals}")

# 이미 있는 요소 추가 (무시됨)
animals.add("고양이")
print(f"고양이 재추가: {animals}")  # 변화 없음

# update - 여러 요소 추가
animals.update(["토끼", "금붕어", "앵무새"])
print(f"여러 동물 추가: {animals}")

# remove - 요소 제거 (없으면 에러)
animals.remove("금붕어")
print(f"금붕어 제거: {animals}")

# discard - 요소 제거 (없어도 에러 안 남)
animals.discard("사자")  # 없지만 에러 안 남
print(f"사자 제거 시도: {animals}")

# pop - 임의 요소 제거 및 반환
removed = animals.pop()
print(f"임의 제거: {animals}, 제거된 동물: {removed}")

# clear - 모든 요소 제거
test_set = {1, 2, 3}
test_set.clear()
print(f"모든 요소 제거: {test_set}")

print("\n" + "="*40)

# 4. 집합 연산 (수학의 집합과 동일!)
print("4. 집합 연산 (수학과 동일!)")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"집합 A: {set_a}")
print(f"집합 B: {set_b}")

# 합집합 (Union)
union1 = set_a | set_b
union2 = set_a.union(set_b)
print(f"합집합 A ∪ B: {union1}")

# 교집합 (Intersection)
intersection1 = set_a & set_b
intersection2 = set_a.intersection(set_b)
print(f"교집합 A ∩ B: {intersection1}")

# 차집합 (Difference)
difference1 = set_a - set_b
difference2 = set_a.difference(set_b)
print(f"차집합 A - B: {difference1}")
print(f"차집합 B - A: {set_b - set_a}")

# 대칭차집합 (Symmetric Difference)
sym_diff1 = set_a ^ set_b
sym_diff2 = set_a.symmetric_difference(set_b)
print(f"대칭차집합 A ⊕ B: {sym_diff1}")

print("\n" + "="*40)

# 5. 집합 관계 확인
print("5. 집합 관계 확인")

big_set = {1, 2, 3, 4, 5, 6}
small_set = {2, 3, 4}
other_set = {7, 8, 9}

print(f"큰 집합: {big_set}")
print(f"작은 집합: {small_set}")
print(f"다른 집합: {other_set}")

# 부분집합 확인
print(f"작은 집합이 큰 집합의 부분집합? {small_set.issubset(big_set)}")
print(f"큰 집합이 작은 집합을 포함? {big_set.issuperset(small_set)}")

# 교집합이 있는지 확인
print(f"큰 집합과 작은 집합이 겹치나? {big_set.isdisjoint(small_set) == False}")
print(f"큰 집합과 다른 집합이 안 겹치나? {big_set.isdisjoint(other_set)}")

print("\n" + "="*40)

# 6. 집합과 반복문
print("6. 집합과 반복문")
programming_languages = {"Python", "Java", "JavaScript", "C++", "Go"}

print("프로그래밍 언어들:")
for language in programming_languages:
    print(f"- {language}")

# enumerate도 가능 (하지만 순서는 의미 없음)
print("\n번호와 함께:")
for i, language in enumerate(programming_languages, 1):
    print(f"{i}. {language}")

print("\n" + "="*40)

# 7. 실전 예제 1: 중복 제거
print("7. 실전 예제 1: 중복 제거")

# 투표 결과에서 참여자 명단 (중복 제거)
votes = ["김철수", "이영희", "김철수", "박민수", "이영희", "최지영", "김철수"]
print(f"투표 기록: {votes}")

# 중복 제거
unique_voters = set(votes)
print(f"참여자 명단: {unique_voters}")
print(f"총 참여자 수: {len(unique_voters)}")

# 다시 리스트로 변환 (필요시)
voter_list = list(unique_voters)
print(f"리스트로 변환: {voter_list}")

print("\n" + "="*40)

# 8. 실전 예제 2: 공통 관심사 찾기
print("8. 실전 예제 2: 공통 관심사 찾기")

# 친구들의 취미
alice_hobbies = {"독서", "영화감상", "요리", "등산", "게임"}
bob_hobbies = {"게임", "축구", "독서", "음악감상", "여행"}
charlie_hobbies = {"독서", "요리", "사진", "등산", "드라마"}

print(f"Alice 취미: {alice_hobbies}")
print(f"Bob 취미: {bob_hobbies}")
print(f"Charlie 취미: {charlie_hobbies}")

# 모든 사람의 공통 취미
common_all = alice_hobbies & bob_hobbies & charlie_hobbies
print(f"\n셋 다 공통 취미: {common_all}")

# Alice와 Bob의 공통 취미
common_ab = alice_hobbies & bob_hobbies
print(f"Alice-Bob 공통 취미: {common_ab}")

# Alice만의 독특한 취미
alice_unique = alice_hobbies - bob_hobbies - charlie_hobbies
print(f"Alice만의 취미: {alice_unique}")

# 전체 취미 목록
all_hobbies = alice_hobbies | bob_hobbies | charlie_hobbies
print(f"전체 취미 목록: {all_hobbies}")

print("\n" + "="*40)

# 9. 실전 예제 3: 권한 관리 시스템
print("9. 실전 예제 3: 권한 관리 시스템")

# 사용자별 권한
admin_permissions = {"read", "write", "delete", "admin", "execute"}
editor_permissions = {"read", "write", "edit"}
viewer_permissions = {"read"}

print(f"관리자 권한: {admin_permissions}")
print(f"편집자 권한: {editor_permissions}")
print(f"뷰어 권한: {viewer_permissions}")

def check_permission(user_permissions, required_permissions):
    """필요한 권한이 있는지 확인"""
    return required_permissions.issubset(user_permissions)

# 권한 확인
required_for_edit = {"read", "write"}
required_for_delete = {"read", "write", "delete"}

print(f"\n편집 권한 확인:")
print(f"관리자: {check_permission(admin_permissions, required_for_edit)}")
print(f"편집자: {check_permission(editor_permissions, required_for_edit)}")
print(f"뷰어: {check_permission(viewer_permissions, required_for_edit)}")

print(f"\n삭제 권한 확인:")
print(f"관리자: {check_permission(admin_permissions, required_for_delete)}")
print(f"편집자: {check_permission(editor_permissions, required_for_delete)}")

print("\n" + "="*40)

# 10. 성능 비교: 집합 vs 리스트
print("10. 성능 비교: 집합 vs 리스트")

import time

# 큰 데이터 준비
big_list = list(range(10000))
big_set = set(range(10000))
search_target = 9999

print("10,000개 데이터에서 9999 찾기:")

# 리스트에서 검색
start_time = time.time()
result_list = search_target in big_list
list_time = time.time() - start_time

# 집합에서 검색
start_time = time.time()
result_set = search_target in big_set
set_time = time.time() - start_time

print(f"리스트 검색 시간: {list_time:.6f}초")
print(f"집합 검색 시간: {set_time:.6f}초")
print(f"집합이 약 {list_time/set_time:.0f}배 빠름!")

print("\n💡 집합의 장점: 검색이 매우 빠름!")

print("\n" + "="*40)

# 11. 집합 활용 팁
print("11. 집합 활용 팁")

print("✅ 집합을 언제 사용할까?")
print("- 중복을 제거하고 싶을 때")
print("- 빠른 검색이 필요할 때")
print("- 집합 연산 (교집합, 합집합 등)이 필요할 때")
print("- 고유한 요소들만 관리할 때")

print("\n🎯 실제 사용 예시:")

# 태그 시스템
post1_tags = {"python", "프로그래밍", "초보자", "튜토리얼"}
post2_tags = {"python", "웹개발", "flask", "프로그래밍"}

# 공통 태그 찾기
common_tags = post1_tags & post2_tags
print(f"공통 태그: {common_tags}")

# 고유 방문자 추적
visitors_today = {"user1", "user2", "user3", "user1", "user2"}  # 중복 자동 제거
print(f"오늘 방문자: {len(visitors_today)}명")

# 블랙리스트 검사
blacklist = {"spam@example.com", "fake@test.com"}
user_email = "user@gmail.com"
if user_email not in blacklist:
    print(f"{user_email}은 허용된 사용자")

print("\n" + "="*40)
print("✅ 집합 완전 정복!")
print("🎯 핵심: 중복 없는 고유 요소들의 빠른 집합 연산!")