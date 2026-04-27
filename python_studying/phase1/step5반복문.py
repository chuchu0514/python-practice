# 반복문

num=int(input("숫자를 입력하세요: "))

if(num%2==0):
    print("Even")
else:
    print("Odd")

a, b, c=map(int, input("세 정수를 입력하세요").split()) #map은 리스트의 각 요소에 함수적용(int)

#input().split()
# "1 2 3" 입력 → ["1", "2", "3"]  문자열 리스트

#map(int, ["1", "2", "3"])
# int 함수를 각 요소에 적용 → [1, 2, 3]  정수 리스트

#a, b, c = [1, 2, 3]
# 언패킹 → a=1, b=2, c=3

if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
elif(c>a and c>b):
    print(c)
else:print("제일 큰 수가 없음")
