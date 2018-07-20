#!/usr/bin/python

print("Hello World")

i = 0
while i < 3:
    num = int(input("Enter a number: "))
    if num > 0:
        print("This number is positive.")
    elif num < 0:
        print("This number is negative.")
    else:
        print("This number is zero.")
    i += 1

greeting = "Hello and welcome to my home!"
for letter in greeting:
    print(letter.upper())

for i in range(5):
    print(i)

for i in range(5, 10):
    print(i)

# The last parameter goes by whatever you want

for i in range(5, 10, 2):
    print(i)

google_age = 1.7
print("My Google-age is %s" % google_age)

def greetSecretAgent(first_name, last_name):
    print("%s. %s, %s" % (last_name, first_name , last_name))

greetSecretAgent("Areeta", "Wong")

if greetSecretAgent("a", "b") is None:
    print("????")

def secretAgentGreeting(first_name, last_name):
    return "%s. %s, %s" % (last_name, first_name , last_name)

print(secretAgentGreeting("Areeta", "Wong"))

greeting = secretAgentGreeting("Areeta", "Wong")
print(greeting)
