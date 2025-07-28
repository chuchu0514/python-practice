# 집합

grades = {85, 90, 78, 90, 85, 92, 78 }
print(grades)

students_math = {"철수", "영희", "민수", "지은"}
students_english = {"영희", "민수", "수진", "태호"}

# 1
print(students_math & students_english)
# 2
print(students_math - students_english)
# 3
print(students_math | students_english)

language = set()

language.update(["python", "java", "c++"])

language.discard("java")

# 1
