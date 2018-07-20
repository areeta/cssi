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

    # Main constructor
    def __init__(self, name, age):
        # Objects has properties
        self.name = name
        self.age = age
        self.is_hungry = True
        self.needs_a_walk = True
        self.is_sleepy = False

    def __str__(self):
        return "%s who is %s" % (self.name, self.age)

    # Objects has methods
    def feed(self):
        self.is_hungry = False
        self.needs_a_walk = True
        print("Nomnomnom")

    def walk(self):
        if self.needs_a_walk and not self.is_sleepy:
            self.needs_a_walk = False
            self.is_sleepy = True
            print("WalkaWalkaWalka")

    # Write a function to let your dog sleep + wake up refreshed and hungry
    def sleep(self):
        if self.is_sleepy == True:
            self.is_sleepy = False
            self.is_hungry = True
            print("ZzzZZzzZZ")

    def play(self, other_dog):
        print("%s is playing with %s." % (self.name, other_dog.name))

dog1 = Dog("Doggy McDogface", 2)
dog2 = Dog("Buster", 1)

dog1.name = "Ruff"

print(dog1.name)
print("%s is %s years old" % (dog1.name, dog1.age))
print(type(dog1))

dog1.feed()
dog1.walk()
dog1.walk()
dog1.sleep()
dog1.feed()
dog1.walk()
dog1.sleep()

print dog1.is_hungry
print(dog1)
print(dog2)

dog1.play(dog2)
dog2.play(dog1)
