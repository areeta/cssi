#!/usr/bin/python

print("Hello World")

# i = 0
# while i < 3:
#     num = int(input("Enter a number: "))
#     if num > 0:
#         print("This number is positive.")
#     elif num < 0:
#         print("This number is negative.")
#     else:
#         print("This number is zero.")
#     i += 1

# greeting = "Hello and welcome to my home!"
# for letter in greeting:
#     print(letter.upper())

# for i in range(5):
#     print(i)

# for i in range(5, 10):
#     print(i)

# The last parameter goes by whatever you want

for i in range(5, 10, 2):
    print(i)

my_name = "Areeta"
friend1 = "Jess"
friend2 = "Julia"
friend3 = "Ciera"
friend4 = "Matthew"

print("My name is " + my_name + " and my friends are " + friend1 + ", " + friend2 + ", " + friend3 + ", and " + friend4)

print(
    "My name is %s and my friends are %s, %s, %s, and %s." %
    (my_name, friend1, friend2, friend3, friend4)
)

google_age = 1.7
print("My Google-age is %s" % google_age)
