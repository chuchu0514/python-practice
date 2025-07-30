# 모듈 사용법 기초

print("=== 1. 내장 모듈 사용하기 ===")

# math 모듈 전체 가져오기
import math

print(f"원주율: {math.pi}")
print(f"16의 제곱근: {math.sqrt(16)}")
print(f"3의 2제곱: {math.pow(3, 2)}")
print(f"올림: {math.ceil(3.2)}")
print(f"내림: {math.floor(3.8)}")

print("\n=== 2. 특정 함수만 가져오기 ===")

# random 모듈에서 특정 함수들만
from random import randint, choice, shuffle

print(f"1~10 랜덤: {randint(1, 10)}")
print(f"리스트에서 랜덤 선택: {choice(['사과', '바나나', '포도'])}")

my_list = [1, 2, 3, 4, 5]
shuffle(my_list)  # 리스트 섞기
print(f"섞인 리스트: {my_list}")

print("\n=== 3. 모듈에 별명 주기 ===")

import datetime as dt

now = dt.datetime.now()
print(f"현재 시간: {now}")
print(f"올해: {now.year}")

print("\n=== 4. 모든 함수 가져오기 (비추천) ===")

# from math import *  # 모든 함수 가져오기
# print(sqrt(25))  # math. 없이 바로 사용
# ↑ 이름 충돌 가능성 때문에 비추천

print("\n=== 5. 자주 쓰는 내장 모듈들 ===")

# os 모듈 - 운영체제 관련
import os
print(f"현재 폴더: {os.getcwd()}")

# sys 모듈 - 시스템 관련  
import sys
print(f"Python 버전: {sys.version}")

print("\n=== import 방법 정리 ===")
print("1. import 모듈명        → 모듈명.함수() 로 사용")
print("2. from 모듈명 import 함수명 → 함수() 바로 사용")  
print("3. import 모듈명 as 별명   → 별명.함수() 로 사용")
print("4. from 모듈명 import *   → 모든 함수 바로 사용 (비추천)")

print("\n=== 실습: 숫자야구에 쓸 random 연습 ===")
from random import randint, sample

# 1~9에서 중복없이 3개 뽑기 (숫자야구용!)
numbers = sample(range(1, 10), 3)
print(f"숫자야구 정답 후보: {numbers}")

# 각 자리수 뽑기
digit1 = randint(1, 9)
digit2 = randint(0, 9) 
digit3 = randint(0, 9)
print(f"개별 뽑기: {digit1}{digit2}{digit3}")

print("\n=== 다음: 직접 모듈 만들어보기! ===")
print("다른 .py 파일을 만들어서 import 해볼 거예요!")