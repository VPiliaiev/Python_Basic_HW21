class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def birthday(self):
        self.age += 1
        print(f'Now the car is {self.age} years old')

    def stop(self):
        print('stop')


car_1 = Auto('Toyota', 1999, 'Carola', 'black', 1000)

car_1.move()
car_1.birthday()
car_1.stop()

print(car_1.brand)
print(car_1.age)
print(car_1.color)
print(car_1.mark)

car_2 = Auto('Mercedes', 2002, 'C200', 'white', 1500)


print(car_2.brand)
print(car_2.age)
print(car_2.color)
print(car_2.mark)

car_2.move()
car_2.birthday()
car_2.stop()
