my_set = set()
my_set2 = set()

for i in range(1, 31):
    my_set2.add(i)

while True:
    try:
        student = int(input())
        my_set.add(student)

    except EOFError:
        break

my_set3 = my_set2 - my_set
result = sorted(list(my_set3))
print(result[0])
print(result[1])


