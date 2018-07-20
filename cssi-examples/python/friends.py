my_name = "Areeta"

friend1 = "Jess"
friend2 = "Julia"
friend3 = "Ciera"
friend4 = "Matthew"
friend5 = "William"
friend6 = "Katy"
friend7 = "Logan"

print("My name is " + my_name + " and my friends are " + friend1 + ", " + friend2 + ", " + friend3 + ", and " + friend4)

print(
    "My name is %s and my friends are %s, %s, %s, and %s." %
    (my_name, friend1, friend2, friend3, friend4)
)

# Arrays
friends = ["Matthew", "Rachel", "Julia","Jess",
           "William", "Katy", "Logan"]

# Array functions
friends.append("Areeta")
friends.insert(1, "Brian")
friends.remove("Rachel")

print(range(len(friends)))

print("My name is %s and I have %s friends"
     % (my_name, len(friends)))

print("My friends are: "),

for i in range(len(friends)):
    if i == 0:
        print(friends[0]),
    else:
        print("and " + friends[i]),
