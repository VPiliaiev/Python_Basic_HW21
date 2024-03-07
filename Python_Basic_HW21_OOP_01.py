class Auto:
    brand = None
    age = None
    color = None
    mark = None
    weight = None

    def move(self):
        print('move')

    def birthday(self):
        self.age += 1
        print(f'Now the car is {self.age} years old')

    def stop(self):
        print('stop')


car_1 = Auto()
car_1.brand = 'Toyota'
car_1.age = 1999
car_1.color = 'red'
car_1.mark = 'Carola'

car_1.move()
car_1.birthday()
car_1.stop()

print(car_1.brand)
print(car_1.age)
print(car_1.color)
print(car_1.mark)

car_2 = Auto()
car_2.brand = 'Mercedes'
car_2.age = 2002
car_2.color = 'blue'
car_2.mark = 'C200'

print(car_2.brand)
print(car_2.age)
print(car_2.color)
print(car_2.mark)

car_2.move()
car_2.birthday()
car_2.stop()
