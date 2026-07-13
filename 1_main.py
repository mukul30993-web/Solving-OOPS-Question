class student:
    def __init__(self,name,age ):
        self.name = name
        self.age = age

    def display(self):
        print("student Name =",self.name)
        print("student Name=",self.age)
    
student = student ("Mukul", 21)

student.display()

