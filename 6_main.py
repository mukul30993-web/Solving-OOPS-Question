class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.__age)


class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(self.name, "is studying", self.course)

    def display(self):
        self.show()
        print("Course:", self.course)


student = Student("Mukul", 21, "Python")

student.display()
student.study()

print(student.name)
print(student.course)