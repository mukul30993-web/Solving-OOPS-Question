class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.__year = year

    def show_info(self):
        print("Brand:", self.brand)
        print("Year:", self.__year)


class Car(Vehicle):

    def __init__(self, brand, year, fuel):
        super().__init__(brand, year)
        self.fuel = fuel

    def start(self):
        print(self.brand, "Car Started")

    def show_info(self):
        super().show_info()
        print("Fuel:", self.fuel)


class Bike(Vehicle):

    def __init__(self, brand, year, cc):
        super().__init__(brand, year)
        self.cc = cc

    def start(self):
        print(self.brand, "Bike Started")

    def show_info(self):
        super().show_info()
        print("CC:", self.cc)


car = Car("Toyota", 2024, "Petrol")
bike = Bike("Royal Enfield", 2023, 350)

car.show_info()
car.start()

print()

bike.show_info()
bike.start()

print()
print("Car Brand:", car.brand)
print("Bike CC:", bike.cc)