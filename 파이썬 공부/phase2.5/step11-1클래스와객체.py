class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"멍멍! 나는 {self.name}야!")

    def birthday(self):
        self.age += 1
        print(f"{self.name}가 {self.age}살이 되었어요!")

my_dog = Dog("초코", 2)
my_dog.bark()
my_dog.birthday()

class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("출발합니다.")
        
class Car(Vehicle):
    def honk(self):
        print("빵빵")

class Bicycle(Vehicle):
    def ring_bell(self):
        print("띠링")

car = Car("좋은차")
print(f"{car.name}")