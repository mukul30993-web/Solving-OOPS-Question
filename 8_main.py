class Employee:

    company = "OpenAI"

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.__salary)
        print("Company:", Employee.company)

    def increase_salary(self, amount):
        self.__salary += amount

    def get_salary(self):
        return self.__salary


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)

    def manage(self):
        print(self.name, "is managing", self.department)


emp = Manager("Mukul", 50000, "IT")

emp.display()

emp.manage()

emp.increase_salary(5000)

print("Updated Salary:", emp.get_salary())

print(emp.name)

print(Employee.company)