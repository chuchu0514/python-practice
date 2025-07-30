import math_utils

print("\\n--- Math Utils 테스트 ---")
print(f"10 + 5 = {math_utils.add(10, 5)}")
print(f"10 - 3 = {math_utils.subtract(10, 3)}")
print(f"4 × 7 = {math_utils.multiply(4, 7)}")
print(f"15 ÷ 3 = {math_utils.divide(15, 3)}")
print(f"15 ÷ 0 = {math_utils.divide(15, 0)}")
print(f"2^5 = {math_utils.power(2, 5)}")

# game_utils 테스트
import game_utils

print("\\n--- Game Utils 테스트 ---")
print(f"주사위: {game_utils.roll_dice()}")
print(f"동전: {game_utils.flip_coin()}")
print(f"숫자야구: {game_utils.generate_baseball_numbers()}")
print(f"로또: {game_utils.generate_lotto()}")
print(f"랜덤 선택: {game_utils.random_choice(['사과', '바나나', '포도'])}")


print("\n=== 모듈 만들기 핵심 포인트 ===")

print("✅ 모듈 = 그냥 .py 파일!")
print("✅ 함수들을 정의하면 다른 파일에서 import 가능")
print("✅ 같은 폴더에 있어야 import 됨")
print("✅ 파일명이 모듈명이 됨 (math_utils.py → math_utils)")


