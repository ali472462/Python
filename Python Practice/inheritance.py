
"""
class animal:
    def __init__(self, habitat):
        self.habitat = habitat
    def display(self):
        print(self.habitat)

    def eat(self):
        print("Eats Accordingly")

class dog(animal):
    def __init__(self, habitat):
        super().__init__(habitat)
    def eat(self):
        print(f"Eat Meat")

a=animal(f"Animals")
a.display()
a.eat()

d=dog("Dogs")
d.display()
d.eat()


class teacher:
    def __init__(self,Department):
        self.dep=Department
    def qualification(self):
        print("Must be MS Qualfied")
    def display(self,):
        print(self.dep)
class student(teacher):
    def __init__(self,Department):
        super().__init__(Department)
    def Section(self):
        print("Section 'A'")
class Youtuber(student,teacher):
    def __init__(self,Department):
        super().__init__(Department)
    def Neche(self):
        print("Cooking Channel")
t=teacher("Physics")
t.qualification()
t.display()
s=student("Computer")
s.Section()
s.qualification()
s.display()
y=Youtuber("Computer","Physics")
y.Neche()
y.Section()
y.display()

"""
class Teacher:
    def teachers_action(self):
        print("I can teach")


class Engineer:
    def Engineers_action(self):
        print("I can code")


class Youtuber:
    def youtubers_action(self):
        print("I can code and teach")


class Person(Teacher, Engineer, Youtuber):
    pass


coder = Person()
coder.teachers_action()
coder.Engineers_action()
coder.youtubers_action()