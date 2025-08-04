from random import randint, sample

def roll_dice():
    return randint(1, 6)

def flip_coin():
    return "앞면" if randint(0, 1) else "뒷면" 

def generate_baseball_numbers():
    while True:
        numbers = sample(range(0, 10), 3)
        if numbers[0] != 0:  
            result = str(numbers[0]) + str(numbers[1]) + str(numbers[2])
            return result

def generate_4digit_numbers():
    while True:
        numbers = sample(range(0, 10), 4)
        if numbers[0] != 0:  
            result = str(numbers[0]) + str(numbers[1]) + str(numbers[2]) + str(numbers[3])
            return result

def generate_lotto():
    """로또 번호 6개 생성 (1~45)"""
    return sorted(sample(range(1, 46), 6))

def random_choice(choices):
    """리스트에서 랜덤하게 하나 선택"""
    return choices[randint(0, len(choices) - 1)]

# 모듈 정보
__version__ = "1.0"
__author__ = "진성"