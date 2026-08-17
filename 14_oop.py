# Object-Oriented Programming in Python


# 1. Class and Object

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Nahid", 22)

student1.display()


# 2. Multiple Objects

student2 = Student("Rahim", 21)
student3 = Student("Karim", 23)

student2.display()
student3.display()


# 3. Inheritance

class Person:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)


class Student2(Person):

    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def show_student(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)


student4 = Student2("Nahid", "CSE101")

student4.show_student()


# 4. Encapsulation

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)

print("Balance:", account.get_balance())


# 5. Polymorphism

class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# 6. Method Overriding

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog2(Animal):

    def sound(self):
        print("Dog barks")


animal = Animal()
dog2 = Dog2()

animal.sound()
dog2.sound()
