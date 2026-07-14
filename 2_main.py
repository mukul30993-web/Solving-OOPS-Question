class car:

    def _init_(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print("Brand :",self.brand)
        print("Model :", self.model)
        print("Year :", self.year)

    def start_engine(self):
        print(self.brand, "Engine Started")

car1 = car("Toyota", "Fortuner", 2024)

car1.display_detail()

car1.startengine()

print(car1.Brand)
print(car1.model)
print(car1.yearr)