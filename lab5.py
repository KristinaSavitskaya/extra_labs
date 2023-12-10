class Engine:

    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company

    def __str__(self) -> str:
        return f'Мотор: {self.power} л.с., {self.company}'

class Person:
    def __init__(self, full_name: str, age: int):
        self.full_name = full_name
        self.__age = age

    def __str__(self) -> str:
        return f'Водитель: {self.full_name}'

class Driver(Person):

    def __init__(self, person: Person, experience: int):
        self.person = person
        self.experience = experience

    def __str__(self) -> str:
        return f'{self.person}, Стаж вождения: {self.experience}'

class Car:
    
    def __init__(self, carClass: str, weight: int, engine: Engine, driver: Driver, marka: str):
        self.carClass = carClass
        self.weight = weight
        self.engine = engine
        self.driver = driver
        self.marka = marka

    def __str__(self) -> str:
        return f'Марка: {self.marka}, Класс: {self.carClass}, Вес: {self.weight}, {self.driver}, {self.engine}'

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turnRight(self):
        print("Поворот направо")

    def turnLeft(self):
        print("Поворот налево")

class Lorry(Car):

    def __init__(self, carClass: str, weight: int, engine: Engine, driver: Driver, marka: str, carrying: int):
        super().__init__(carClass, weight, engine, driver, marka)
        self.carrying = carrying

    def __str__(self) -> str:
        return f'{super().__str__()}, Грузоподъемность: {self.carrying} кг'

class SportCar(Car):
    def __init__(self, carClass: str, weight: int, engine: Engine, driver: Driver, marka: str, speed: int):
        super().__init__(carClass, weight, engine, driver, marka)
        self.speed = speed

    def __str__(self) -> str:
        return f'{super().__str__()}, Скорость: {self.speed} км/ч'

Ivan = Person(full_name = 'Иван Иванов', age = 30)
driver_car = Driver(person = Ivan, experience = 5)
engine_car = Engine(power = 200, company = 'Toyota')
car = Car(carClass = 'Седан', weight = 1500, engine = engine_car, driver = driver_car, marka = 'Toyota Camry')

Petr = Person(full_name = 'Петр Петров', age = 35)
driver_lorry = Driver(person = Petr, experience = 10)
engine_lorry = Engine(power = 300, company = 'Volvo')
lorry = Lorry(carClass = 'Грузовик', weight = 8000, engine = engine_lorry, driver = driver_lorry, marka = 'Volvo FH', carrying = 5000)

Anna = Person(full_name = 'Анна Сидорова', age = 30)
driver_sportcar = Driver(person = Anna, experience = 3)
engine_sportcar = Engine(power = 400, company = 'Ferrari')
sportcar = SportCar(carClass = 'Спорткар', weight = 1500, engine = engine_sportcar, driver = driver_sportcar, marka = 'Ferrari 488', speed = 1500)

print(car)

print('\nИнформация о грузовике:')
print(lorry)

print('\nИнформация о спорткаре:')
print(sportcar)

print()
car.start()
car.turnRight()
car.turnLeft()
car.stop()