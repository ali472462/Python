""""
Num1=input("Enter first Number=")
Num1=float(Num1)
Num2=input("Enter Second Number=")
Num2=float(Num2)
try:
    Div=Num1/Num2
except Exception as e:
    print('Exception Occured :',type(e).__name__)
    Div=None
print(Div)


# for making exception just make subclass of Exception
class adultException(Exception):
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if int(self.age) >= 18:
            raise adultException
        else:
            return self.age

    def display(self):
        try:
            print(f"age -> {self.get_minor_age()}")
        except adultException:
            print("Person is an adult")
        finally:
            print(f"name -> {self.name}")


# No exception
Person("Bhavin", 17).display()

# AdultException is raised
Person("Dhaval", 23).display()

Person("ali",33).display()
"""

class AdultException(Exception):
    pass

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
    def get_minor_age(self):
        if self.age >=18:
           raise AdultException
        else:
            return self.age
        pass
    def display_person(self):
        try:
            print(f"age -> {self.get_minor_age()}")
        except AdultException:
            print("Person is an adult")
        finally:
            print(f"name -> {self.name}")
p=Person("Ali",21).display_person()
p=Person("Hassan",11).display_person()
