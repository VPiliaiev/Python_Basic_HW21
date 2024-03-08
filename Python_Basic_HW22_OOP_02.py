from Python_Basic_HW21_OOP_Second_Version import Auto
import time


class Truck(Auto):
    def __init__(self, brand, age, mark, color=None, weight=None, max_load=None):
        super().__init__(brand, age, mark)
        self.color = color
        self.weight = weight
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)
        return self.max_load


class Car(Auto):
    def __init__(self, brand, age, mark, color=None, weight=None, max_speed=None):
        super().__init__(brand, age, mark)
        self.color = color
        self.weight = weight
        self.max_speed = max_speed

    def move(self):
        print(f'max speed is {self.max_speed}')
        super().move()

flatbed_truck = Truck('Toyota', 2005, 'family', 'White', None, 1000)
tanker_truck = Truck('Volvo', 2007, 'tanker', 'red', None, 2000)
flatbed_truck.move()
flatbed_truck.load()
print('max load Flatbed truck: ', flatbed_truck.load())

tanker_truck.move()
tanker_truck.load()
print('max load Tanker truck: ', tanker_truck.load())

sedan = Car('BMW', 2020, 'sedan', 'yellow', None, 180)
van = Car('Ford', 2019, 'van', 'black', None, 200)
sedan.move()
print('max speed sedan', sedan.max_speed)
van.move()
print('max speed van', van.max_speed)