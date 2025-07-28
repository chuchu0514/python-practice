# 딕셔너리

# 1번 문제
my_info = {"name": "추진성", "age": 25, "hobby": "노래"}

# 2번 문제
menu = {"pizza": 15000, "burger": 8000, "coke": 2000}
print(menu["pizza"])
menu["pasta"] = 12000

# 3번 문제
print(menu.keys())

# 4번문제

print(menu.get("pasta"))

if "pasta" in menu:
    print("있어요")
else:
    print("없어요")  