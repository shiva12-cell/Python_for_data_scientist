from datetime import datetime

class Person:
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob  # datetime object
        self.country = country

    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.dob.year

        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        return age

    def greet(self):
        age = self.calculate_age()
        print(f"Hello, my name is {self.name}. I am {age} years old and I live in {self.country}.")

# 💬 Input
name = input("Enter your name: ")
dob_str = input("Enter your DOB (YYYY-MM-DD): ")
country = input("Enter your country: ")

# Convert DOB to datetime
dob = datetime.strptime(dob_str, "%Y-%m-%d")

# 🎯 Create object and greet
person = Person(name, dob, country)
person.greet()