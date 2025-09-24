lst = [1, 2, 3]

# ✅ 추가
lst.append(4)        # 뒤에 추가: [1, 2, 3, 4]
lst.insert(0, 0)     # 특정 위치에: [0, 1, 2, 3, 4]   (어디에,무엇을)
lst.extend([5, 6])   # 리스트 통째로: [0, 1, 2, 3, 4, 5, 6]

# ❌ 제거
lst.remove(2)        # 값으로 제거: [0, 1, 3, 4, 5, 6]
lst.pop()           # 마지막 제거: [0, 1, 3, 4, 5] (6 반환)
lst.pop(0)          # 인덱스로 제거: [1, 3, 4, 5] (0 반환)
lst.clear()         # 전체 삭제: []

# 🔍 확인
len(lst)            # 길이
2 in lst            # 포함 여부 (True/False)
lst.index(3)        # 값의 인덱스 찾기
lst.count(1)        # 값의 개수

tup = (1, 2, 3)

# ❌ 추가/제거 불가능! (Immutable)
# tup.append(4)     # AttributeError!
# tup.remove(2)     # AttributeError!

# ✅ 읽기만 가능
print(tup[0])       # 1 (인덱스 접근)
len(tup)            # 3
2 in tup            # True (포함 여부)
tup.index(2)        # 1 (인덱스 찾기)
tup.count(1)        # 1 (개수 세기)

# 🔄 새로 만들기만 가능
new_tup = tup + (4, 5)  # (1, 2, 3, 4, 5)

dic = {'a': 1, 'b': 2}

# ✅ 추가/수정
dic['c'] = 3         # 새 키: {'a': 1, 'b': 2, 'c': 3}
dic.update({'d': 4}) # 딕셔너리 통째로
dic.setdefault('e', 5)  # 없으면 추가, 있으면 무시

# dic = {'a': 1, 'b': 2}

# result1 = dic.setdefault('a', 999)  # 'a' 이미 있음 → 기존 값 유지
# print(dic)     # {'a': 1, 'b': 2} ← 'a'는 여전히 1!
# print(result1) # 1 ← 기존 값 반환

# result2 = dic.setdefault('c', 3)    # 'c' 없음 → 새로 추가  
# print(dic)     # {'a': 1, 'b': 2, 'c': 3}
# print(result2) # 3 ← 새로 추가된 값 반환

# ❌ 제거
dic.pop('a')         # 키로 제거: {'b': 2, 'c': 3, 'd': 4, 'e': 5} (1 반환)
del dic['b']         # 키로 삭제: {'c': 3, 'd': 4, 'e': 5}
dic.clear()          # 전체 삭제: {}

# 🔍 확인/가져오기
dic.keys()           # dict_keys(['c', 'd', 'e']) - 키들
dic.values()         # dict_values([3, 4, 5]) - 값들  
dic.items()          # dict_items([('c', 3), ('d', 4), ('e', 5)]) - 쌍들
dic.get('f', 0)      # 키 없으면 기본값 반환: 0
'c' in dic           # True (키 존재 여부)

s = {1, 2, 3}

# ✅ 추가
s.add(4)            # 원소 추가: {1, 2, 3, 4}
s.update([5, 6])    # 여러 원소: {1, 2, 3, 4, 5, 6}

# ❌ 제거
s.remove(2)         # 값으로 제거: {1, 3, 4, 5, 6} (없으면 에러!)
s.discard(7)        # 값으로 제거: {1, 3, 4, 5, 6} (없어도 에러 안 남)
s.pop()            # 임의 원소 제거 (뭐가 나올지 모름)
s.clear()          # 전체 삭제: set()

# 🔍 확인
len(s)             # 길이
2 in s             # 포함 여부

from collections import deque
q = deque([1, 2, 3])

# ✅ 추가
q.append(4)         # 오른쪽 추가: deque([1, 2, 3, 4])
q.appendleft(0)     # 왼쪽 추가: deque([0, 1, 2, 3, 4])

# ❌ 제거
q.pop()            # 오른쪽 제거: deque([0, 1, 2, 3]) (4 반환)
q.popleft()        # 왼쪽 제거: deque([1, 2, 3]) (0 반환)

# 🔍 확인
len(q)             # 길이
2 in q             # 포함 여부
q[0]               # 인덱스 접근 가능

lst = [1, 2]
lst.append([3, 4])    # [1, 2, [3, 4]] ← 리스트 통째로 하나 추가
lst.extend([3, 4])    # [1, 2, 3, 4] ← 원소들을 개별적으로 추가
lst.insert(1, 99)     # [1, 99, 2] ← 특정 위치에 추가

lst = [1, 2, 3, 2]
lst.remove(2)         # [1, 3, 2] ← 첫 번째 2만 제거
val = lst.pop(1)      # [1, 2], val=3 ← 인덱스로 제거하고 값 반환
del lst[0]            # [2] ← 인덱스로 제거, 값 반환 안 함

dic = {'a': 1}
print(dic['b'])       # KeyError! 💥
print(dic.get('b'))   # None (에러 안 남)
print(dic.get('b', 0)) # 0 (기본값)

