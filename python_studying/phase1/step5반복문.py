# 반복문

num=int(input("숫자를 입력하세요: "))

if(num%2==0):
    print("Even")
else:
    print("Odd")

a, b, c=map(int, input("세 정수를 입력하세요").split())

if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
elif(c>a and c>b):
    print(c)
else:print("제일 큰 수가 없음")
