class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return "Woof!"

    def run(self):
        return f"{self.name} is running!"