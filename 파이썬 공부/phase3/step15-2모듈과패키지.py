from math import sqrt, sin, cos, pow

print(sqrt(25))
print(sin(1))
print(cos(25))
print(pow(3, 2))

import random

print(f"주사위 굴리기:{random.randint(1, 6)}")

lotto = set()
while True:
    
    lotto_num = random.randint(1, 45)
    lotto.add(lotto_num)
    if len(lotto) == 6:
        break

print(f"로또 번호:{sorted(lotto)}")


import datetime

today = datetime.date.today()
birthday = datetime.date(today.year, 5, 22)

# 생일 지났으면 내년으로
if today > birthday:
    birthday = datetime.date(today.year + 1, 5, 22)

days_left = (birthday - today).days
print(f"생일까지 {days_left}일!")