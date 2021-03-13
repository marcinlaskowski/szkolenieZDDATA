"""
Stwórz klasę Pojazd z atrybutami: kolor, cena. Klasę Samochód  i Rower, obie dziedziczące po klasie Pojazd.
Stwórz kilka obiektów klasy Samochód i Rower. Stwórz listę pojazdy, w której znajdą się stworzone obiekty.
Wśród wszystkich pojazdów znajdź najdroższy pojazd, wypisz średnią cenę samochodu.

"""


class Vehicle:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def __str__(self):
        return f"{self.color} - {self.price}"


class Car(Vehicle):
    pass


class Bicycle(Vehicle):
    pass


if __name__ == "__main__":
    car1 = Car("szary", 20000)
    car2 = Car("czerwony", 30000)
    car3 = Car("zielony", 15000)
    bicycle1 = Bicycle("niebieski", 1000)
    bicycle2 = Bicycle("żółty", 2000)

    vehicles = [car1, car2, car3, bicycle1, bicycle2]

    max_price = 0
    max_price_vehicle = None

    for vehicle in vehicles:
        print(vehicle.price, vehicle.color)

        if vehicle.price > max_price:
            max_price = vehicle.price
            max_price_vehicle = vehicle

    print("Najdroższy pojazd", max_price_vehicle.color, max_price_vehicle.price)
    print(f"Najdroższy pojazd - {max_price_vehicle.color} {max_price_vehicle.price}")
    print("Najdroższy pojazd", max_price_vehicle)

    # Wypisz średnią cenę samochodu.
    car_price_sum = 0
    car_numbers = 0

    for vehicle in vehicles:
        print(vehicle)
        print(type(vehicle))

        print(isinstance(vehicle, Vehicle))
        print(isinstance(vehicle, Car))
        print(isinstance(vehicle, Bicycle))

        if isinstance(vehicle, Car):
            car_price_sum = car_price_sum + vehicle.price
            car_numbers += 1

    print(f"Średnia: {round(car_price_sum / car_numbers, 2)}")

    # 2
    # Przykład Piotra:
    # sum([item.price for item in vehicles if isinstance(item, Car)]) / len([item for item in vehicles if isinstance(item, Car)])

    car_prices = [vehicle.price for vehicle in vehicles if isinstance(vehicle, Car)]
    print(car_prices)
    print(sum(car_prices) / len(car_prices))
    print(round(sum(car_prices) / len(car_prices), 2))
