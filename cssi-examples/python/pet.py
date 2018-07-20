# Dictionary
dog = {
    "name": "Doggy McDogface",
    "breed": "Terrier",
    "age": 2,
    "hungry": True,
    "sleepy": False
}

# Object - designing a template for an object
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.needs_a_walk = True
        self.is_sleepy = False

    def feed(self):
        self.is_hungry = False
        print("Nomnomnom")

    def walk(self):
        if self.needs_a_walk and not self.is_sleepy:
            self.needs_a_walk = False
            self.is_sleepy = True
            print("WalkaWalkaWalka")

    # Write a function to let your dog sleep + wake up refreshed and hungry
    def sleep(self):
        self.is_sleepy = False
        self.is_hungry = True

dog1 = Dog("Doggy McDogface", 2)
dog2 = Dog("Buster", 1)

dog1.name = "Ruff"

print(dog1.name)
print("%s is %s years old" % (dog1.name, dog1.age))
print(type(dog1))

dog1.feed()
dog1.walk()
dog1.walk()
print dog1.is_hungry
