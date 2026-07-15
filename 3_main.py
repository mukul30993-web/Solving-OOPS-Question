class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        print("Name:", self.name)
        print("Breed:", self.breed)

    def speak(self):
        print(self.name, "barks")


dog = Dog("Tommy", "Labrador")

dog.display()

dog.speak()

print(dog.name)
print(dog.breed)