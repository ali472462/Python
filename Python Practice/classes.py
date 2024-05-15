"""
class Student:
    def __init__(self,n,f):
        self.Name=n
        self.Function=f

    def do_work(self):
        if self.Function=="obedient":
            print(f"{self.Name},u should Work hard")
        elif self.Function=="average":
            print(f"{self.Name} Should Focus On Online Skills")

    def speak(self):
        print(f"{self.Name} Says, How are U?")

Ali = Student("Ali Hassan","average")
Ali.do_work()
Ali.speak()

Haider = Student("Haider Ali","obedient")
Haider.do_work()
Haider.speak()

class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")


# Creating a emp instance of Employee class
emp = Employee(1, "coder")

emp.display()

del emp.id
try:
    print(emp.id)
except AttributeError as e:
    print("Emp id Does'nt Exist",type(e).__name__)

del emp
try:
    print(emp)
except NameError as e:
    print("Emp does'nt Exist",type(e).__name__)
"""
class Employee:
    def __init__(self,id,name):
        self.Name=name
        self.Id=id
    def display(self):
        print(f"ID: {self.Id} Name: {self.Name}")
emp=Employee(1,"Ali")
emp.display()

del emp.Id
try:
    print(emp.Id)
except AttributeError as e:
    print("Emp.Id Object Doest Exist",type(e).__name__)
del emp
try:
    print(emp)
except NameError as e:
    print("Emp Object Doest Exist",type(e).__name__)

