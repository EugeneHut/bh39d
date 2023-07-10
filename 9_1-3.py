class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        is_baby_seat = 'есть' if self.is_baby_seat else 'отсутствует'
        return f'Автомобиль {self.color} цвета, на {self.count_passenger_seats} места, детское сидение {is_baby_seat}.'


class Taxi:
    def __init__(self, cars: list):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool):
        for car in self.cars:
            if count_passengers <= car.count_passenger_seats and is_baby == car.is_baby_seat:
                car.is_busy = True
                return car
        return None


class Category:
    categories = []

    @classmethod
    def add(cls, name: str):
        if name in cls.categories:
            raise ValueError("Такая категория уже есть!")
        else:
            cls.categories.append(name)
            return cls.categories.index(name)

    @classmethod
    def get(cls, index: int):
        if cls.categories[index]:
            return cls.categories[index]
        else:
            raise IndexError("Такой категроии нет!")

    @classmethod
    def delete(cls, index: int):
        if index < len(cls.categories):
            del cls.categories[index]

    @classmethod
    def update(cls, index: int, new_name: str):
        if new_name in cls.categories:
            raise ValueError("Такая категория ужу есть!")
        elif index < len(cls.categories):
            cls.categories[index] = new_name
        else:
            cls.categories.append(new_name)


kia = Car('белого', 4, True)
print(kia)
