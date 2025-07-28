# 반복문2
# 1번 문제: 1부터 10까지 합
sum_total = 0
for i in range(1, 11):
    sum_total += i
print(sum_total)

# 2번 문제: 입력받은 수까지의 곱(팩토리얼)
n = int(input("정수를 입력하세요(팩토리얼 계산): "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

# 3번 문제: 구구단 2단
for i in range(1, 10):
    print(f"2 * {i} = {2 * i}")

# 4번 문제: 1~100까지 짝수만 출력 (while문)
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
    









