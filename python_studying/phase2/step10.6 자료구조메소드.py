# step_list_tuple_dict_set.py
# 📚 리스트 / 튜플 / 딕셔너리 / 집합 완전 가이드 + 실습


print("=== 📚 Python 기초: 리스트 / 튜플 / 딕셔너리 / 집합 메서드 정리 ===")
print()

# ----------------------------------------
# 1) 리스트 (list)
# ----------------------------------------
print("1) 리스트 (list) — 변경 가능, 순서 있음, 중복 허용")
print()

def demo_list():
    lst = [3, 1, 4]
    print("초기:", lst)

    lst.append(9)     # 리스트 뒤에 값 추가
    print("append(9):", lst)

    lst.extend([2, 7])  # 여러 값을 한 번에 뒤에 추가
    print("extend([2,7]):", lst)

    lst.insert(1, 8)  # 인덱스 1 위치에 값 삽입
    print("insert(1,8):", lst)

    lst.remove(4)     # 값 4를 리스트에서 제거(첫 번째 등장만)
    print("remove(4):", lst)

    last = lst.pop()  # 마지막 요소 꺼내고 삭제
    print("pop():", last, "=>", lst)

    first = lst.pop(0)  # 인덱스 0 요소 꺼내고 삭제
    print("pop(0):", first, "=>", lst)

    print("index(8):", lst.index(8))  # 값 7이 처음 나타나는 위치 반환
    print("count(3):", lst.count(3))  # 값 3의 개수 세기

    copy_lst = lst.copy()  # 리스트 복사(얕은 복사)
    print("copy():", copy_lst)

    copy_lst.reverse()  # 리스트 순서 뒤집기
    print("reverse():", copy_lst)

    copy_lst.sort()     # 리스트 정렬
    print("sort():", copy_lst)

print("--- 리스트 데모 ---")
demo_list()
print("\n" + "="*50 + "\n")

# ----------------------------------------
# 2) 튜플 (tuple)
# ----------------------------------------
print("2) 튜플 (tuple) — 변경 불가, 순서 있음")
print()

def demo_tuple():
    t = (1, 2, 3, 2)
    print("튜플:", t)

    print("count(2):", t.count(2))  # 값 2가 몇 개 있는지
    print("index(3):", t.index(3))  # 값 3이 처음 나타나는 위치

    # 튜플은 변경할 수 없으므로 리스트로 바꿔서 수정
    lst = list(t)      # 튜플 → 리스트 변환
    lst.append(9)      # 값 추가
    t2 = tuple(lst)    # 다시 튜플로 변환
    print("변경 예시 (list 변환 후 append):", t2)

print("--- 튜플 데모 ---")
demo_tuple()
print("\n" + "="*50 + "\n")

# ----------------------------------------
# 3) 딕셔너리(dict)
# ----------------------------------------
print("3) 딕셔너리 (dict) — 키:값 매핑")
print()

def demo_dict():
    d = {"a": 1, "b": 2}
    print("초기 dict:", d)

    d["c"] = 3   # 키 'c'에 값 3 추가(또는 수정)
    print("d['c']=3 ->", d)

    print("get('x', 0):", d.get("x", 0))  
    # key 'x'가 없으면 기본값 0 반환 (에러 안 남)

    print("keys():", list(d.keys()))        # 키 목록 반환
    print("values():", list(d.values()))    # 값 목록 반환
    print("items():", list(d.items()))      # (키, 값) 튜플 목록

    popped = d.pop("b")  # key 'b'를 제거하고 그 값을 반환
    print("pop('b'):", popped, "->", d)

    d.update({"a": 10, "d": 4})  
    # 다른 dict 내용을 현재 dict에 덮어쓰기(병합)
    print("update({'a':10, 'd':4}):", d)

    item = d.popitem()  
    # 마지막으로 추가된 (키,값) 쌍 삭제하고 반환
    print("popitem():", item, "->", d)

    val = d.setdefault("e", 99)  
    # 'e' 키가 없으면 값 99 넣고 반환. 있으면 기존 값 반환
    print("setdefault('e',99):", val, "->", d)

print("--- 딕셔너리 데모 ---")
demo_dict()
print("\n" + "="*50 + "\n")

# ----------------------------------------
# 4) 집합 (set)
# ----------------------------------------
print("4) 집합 (set) — 중복 없음, 순서 없음")
print()

def demo_set():
    s = {1, 2, 3}
    t = {3, 4, 5}
    print("s:", s)
    print("t:", t)

    s.add(6)         # 요소 추가
    print("add(6):", s)

    s.discard(10)    # 없으면 무시하고 넘어감 (에러 없음)
    print("discard(10):", s)

    # s.remove(10)  # 요소 없으면 KeyError 발생 → discard와 차이!

    print("union:", s.union(t))                        # 합집합
    print("intersection:", s.intersection(t))          # 교집합
    print("difference (s - t):", s.difference(t))      # 차집합
    print("symmetric_difference:", s.symmetric_difference(t))  # 대칭차집합

    print("issubset/issuperset:", {3}.issubset(s), s.issuperset({3}))
    # 부분집합인지 / 포함하는 집합인지 확인

print("--- 집합 데모 ---")
demo_set()
print("\n" + "="*50 + "\n")

# ----------------------------------------
# 실습 문제
# ----------------------------------------
print("🔧 실습 문제 (직접 풀어보세요!)")
print()

print("A) 리스트에서 중복 제거 & 정렬하여 반환")
print("B) (이름, 나이) 튜플 리스트에서 가장 나이가 많은 사람 찾기")
print("C) 딕셔너리에서 값이 가장 작은 키 찾기")
print("D) 집합에서 대칭차집합 구하기(메서드로)")
print()

print("--- 정답 예시 (참고용) ---")

def solve_A(lst):
    return sorted(set(lst))  # set으로 중복 제거 후 정렬

def solve_B(tuples):
    return max(tuples, key=lambda x: x[1])  # age 기준으로 max

def solve_C(d):
    return min(d, key=lambda k: d[k])  # 값 기준으로 최소 key

def solve_D(a, b):
    return a.symmetric_difference(b)  # 대칭차집합

print("A:", solve_A([3,1,2,3,2]))
print("B:", solve_B([("A",20),("B",25),("C",22)]))
print("C:", solve_C({"x":5, "y":2, "z":9}))
print("D:", solve_D({1,2,3}, {3,4,5}))


